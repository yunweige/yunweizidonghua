age = 28
def sayHi(name):
    #global age
    age = 29
    print 'Hello %s you are %s years old' % (name,age)

sayHi('AAA')

print 'My age is %s' % age

print "[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]"


def sayHi2(name,group='Nokia'):
    print 'Name is %s working in %s' % (name,group)

sayHi2('ma')
sayHi2('xxxx','NB')


def sayHi3(*args):
    print args
sayHi3('xxx','aaa','cccc')

def sayHi4(**kargs):
    print kargs

name_list = {
        'name':'alex',
        'age':'23'
        'phone:''123'
    }
sayHi4(name='xxxx',age='15',phone='2222')