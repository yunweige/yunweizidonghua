import time

def sayHi(**kargs):
    #if kargs.has_key('name'):
     #   print kargs['name']
      #  print kargs
    for i in range(10):
        time.sleep(1)
        yield 'Loop',i
    #return kargs['name']

result = sayHi(name='Alex', age=29, phone=123456)

def x():
    for i in range(10):
        print result.next()

x()