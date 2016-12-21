'''
name = []
name.extend(range(100))
name[1]
name[1:10]
name.index()

name.remove()
name.pop()
'''

names = ['IBM','JACL','DELL']
names.extend(range(2000))
names.insert(100,'IBM')
names.insert(220,'IBM')
names.insert(300,'IBM')

for i in range(names.count('IBM')):
    n = [names.index('IBM')]
    names[n] = 'HP'
    '''
    names[names.index('IBM')=HP
    '''