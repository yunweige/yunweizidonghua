while True:
    name = raw_input("Please input your username:")
    if name == 'AAA':
        password = raw_input("Please input your password:")
        while password != '123':
            password = raw_input("again password:")
            print 'SB'
        else:
            print "NB"
            break
    else:
        print "Sorry,user %s not found" % name