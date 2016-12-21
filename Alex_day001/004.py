# coding=utf-8
while True:
    input = raw_input("Please input your username:")
    if input == 'Alex':
        password = raw_input("Please input your pass:")
        p = '123'

        #如果输入密码错误，一直下去
        while password != p:
            password = raw_input("Wrong passwd input again:")
        else:
            print 'Welcome login to TriAquae!\n'
            while True:
                match_yes = 0
                input = raw_input("\033[32mPlease input the name whom you want to search:\033[0m")
                contact_file = file('contact.txt')
                while True:
                    line = contact_file.readline()
                    if len(line) == 0:
                        break
                    if input in line:
                        print 'Match item: \033[36;1m%S\033[0m' % line
                        match = 'YES'
                    else:
                        pass
                        if match != 'YES':
                            print 'No match item found.'
            else:
                print "Sorry user %s not found" % input