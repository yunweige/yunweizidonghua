import redis_connector as redis
import plugin_conf
import threading 
import pickle,sys,time
import threading 

hostname = 'alex_test'

channel = 'monitor_queue'



def request_configuration(host):
    config_key = 'HostConfiguration::%s' % host
    monitor_list = redis.r.get(config_key)
    if monitor_list is not None: 
        monitor_list = pickle.loads(monitor_list)
    else:
        sys.exit('\033[31;1mCould not load the configuration data from monitor server,please check!\033[0m')
    return monitor_list

def msg_publish(plugin_f):
    
    data = plugin_f()
    status_dic= {'hostname':hostname,  'data': data }
    redis.r.publish(channel, pickle.dumps(status_dic))
    
configure_data = request_configuration(hostname) 

while True:
    for k,v in configure_data['services'].items():
        try:
            interval = v[1]
            last_run = v[2]
            plugin_func = getattr(plugin_conf,v[0])
            if (last_run + interval ) <= time.time():#time to run the plugin again
                        
                configure_data['services'][k][2] = time.time()  # save current time last run 
                
                p = threading.Thread(target=msg_publish, args=(plugin_func,) )
                p.start()
            else:
                next_run_time = interval - (time.time() - last_run) 
                print '%s :::next run starts in \033[32;1m%s \033[0msecs...' %(k, next_run_time)
        except TypeError:
            print  'Error----->plugin name not set',k,v
    time.sleep(2)

print '--------loop ist done....'
       
#for i in range(2**20):
#    data = range(10)
#    print redis.r.publish(channel, pickle.dumps(data))
    
    