
import templates


#host h1
h1 = templates.LinuxGeneralServices()
h1.name = 'alex_test'
h1.ip = '192.168.2.3'
h1.port = 22
h1.services['cpu'].triggers['iowait'] = ['percentage', 30,50]




#host h2
h2 = templates.LinuxGeneralServices()
h2.name = 'ubuntu'
h2.ip = '192.18.71.134'
h2.port = 8000
h2.services['cpu'].triggers['system'] = [int, 80,90]

#print h1.ip, h1.services['cpu'].triggers 
#print h2.ip, h2.services['cpu'].triggers 



monitored_hosts = (
    h1, h2

)


