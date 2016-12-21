import plugin_conf
import threading 

def run(service_key, service_func):
    service_dic[service_key] = service_func()

def multi_thread(service_list):
    result_list = []
    for k,v in service_dic.items():
        result_list.append( threading.Thread(target=run, args=(k,v)) )
        
    
    for p in result_list:p.start() #kick start the threads
    
    for res in result_list: #get result 
        res.join()

    #print service_dic    

if __name__ == '__main__':

    service_dic = {
        'upCheck': plugin_conf.upCheck_info,
        'cpu' : plugin_conf.cpu_info
    
    }
    multi_thread(service_dic)

    print service_dic
    


