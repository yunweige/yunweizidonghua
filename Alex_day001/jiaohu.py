name = raw_input('what is your name?:').strip()
if len(name) == 0:
    print 'Error: you must input sth as name.'
age = raw_input('how old are you?:')
job = raw_input('what is your job?')

msg = """
Information of %s as below:
	Name : \033[34;1m%s \033[0m;
	Age  : \033[35;1m%s \033[0m;
	Job  : \033[36;1m%s \033[0m;
""" % (name, name, age, job)

if int(age) >= 50:
    print "You are too old, you can only work for ..."
elif int(age) >= 30:
    print "You are now in the middle age,so enjoy your life before getting too old.... "

else:
    if int(age) >= 20:
        print 'you are still very young!'
    else:
        print 'not adult'

print msg