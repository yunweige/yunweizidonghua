class person:
    def tell(self,name):
        print 'Hi my name is ', name

    def study(self):
        print 'I am stuying Py right now'

class student(person):
    def study(self):
        print 'I am stuying Py right now'


p = person()
vars = ['tell', 'study']

v1 = vars[0]
print getattr(p, v1)('oldboy')