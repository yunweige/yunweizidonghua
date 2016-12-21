#from scripts import sys_Info,cpu,memory,disk,netinfo
#from scripts import *
from plugins import upCheck,cpu,load,memory
def upCheck_info():  
    return upCheck.monitor()
    
def cpu_info():
    data = cpu.monitor()
    print data
    return data
def load_info():
    data =load.monitor()
    print data
    return data
def mem_info():
    return memory.monitor()
"""
def sys_info():
    return sys_Info.monitor()
    
def cpu_info():
    return cpu.monitor()
    
def mem_info():
    return memory.monitor()

def disk_info():
    return disk.monitor()

def net_info():
    return netinfo.monitor()
"""
