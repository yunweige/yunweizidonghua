import threading
import time
def sayHi(n):
    print 'Hi this is thread %s' % n
    time.sleep(1)

for i in range(20):
    t = threading.Thread(target=sayHi,args=(i, ))
    t.start()
    t.join()