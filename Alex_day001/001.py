name = raw_input('Name:')
age = raw_input('Age:')
job = raw_input('Job:')

print '------------\n'



print ('\tName: %s\n'
       '\tAge: %s\n'
       '\tJob: %s ') % (name, age, job)

if age < 28:
    print "you're yang"
elif name == 'AAA':
    print "%s is SB" % name
else:
    print "old man"
