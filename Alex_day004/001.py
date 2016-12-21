import time
def sayHi():
    start = time.time()
    print 'hi your'
    time.sleep(0.1)
    end = time.time()
    print 'This function costes ',end-start

sayHi()