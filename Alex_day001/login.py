import sys
username = 'alex'
password = '123456'
locked = 1

retry_counter = 0

while retry_counter < 3:
    user = raw_input('USERNAME: ').strip()
    if len(user) == 0:
        print '\033[31;1mUSERNAME cannot be empty!\033[0m'
        continue

    passwd = raw_input('PASSWORD: ').strip()
    if len(password) == 0:
        print '\033[31;1mPASSWORD cannot be empty!\033[0m'
        continue

if locked == 0:
    print 'Your usename is locked!'
    sys.exit()

else:
    if user == username and passwd == password:
        sys.exit('Welcome %s login to our system!') % user

    else:
        retry_counter += 1
        print '\033[31;1mWrong username or password, you have %s more chances!\033[0m'