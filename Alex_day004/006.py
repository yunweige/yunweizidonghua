class Person:
    def __init__(self,name,age):
        print 'I am been calling right now...'
        self.Name = name
        self.Age = age
    def sayHi(self):
        print 'Hi my name is %s, i am %s year' % (self.Name, self.Age)

    def __del__(self):
        print 'I got killed just now ...bye ...'

p = Person('alex',22)
p.sayHi()