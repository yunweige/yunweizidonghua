class Person:
    def __init__(self,name,age):
        print 'I am been calling right now...'
        self.Name = name
        self.Age = age
    def sayHi(self):
        print 'Hi my name is %s, i am %s year' % (self.Name, self.Age)
        self.__talk()
    def __talk(self):
        print 'I am private...'

p = Person('alex',22)
p.sayHi()
#p.__talk()
#p.__Person__talk()