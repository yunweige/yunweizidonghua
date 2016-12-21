import time
def sayHi():
    print 'hi your'
    time.sleep(0.1)

def time_counter(func):

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print 'This function costes ',end-start
    return wrapper
sayHi = time_counter(sayHi)
sayHi()