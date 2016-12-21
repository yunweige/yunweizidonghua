import global_setting
import redis_connector as redis
from conf import hosts

import pickle



def update_all_hosts_configuration():
    host_dic ={}
    for h in hosts.monitored_hosts:
        #rint h #.name,h.ip
        host_dic[h.name] = {'services': {}, 'hostname': h.name }

        for k,v in h.services.items():
            host_dic[h.name]['services'][k] = [v.plugin_name, v.interval, 0]  # last 0 stands for last run
            #print k,v.interval
            
        #save it to redis
        redis.r['HostConfiguration::%s' %h.name] = pickle.dumps( host_dic[h.name]  )
        
    print host_dic
update_all_hosts_configuration()    