class AlexException(Exception):
    def __init__(self,err):

        print 'going to exit'
while True:
    try:
        name = raw_input('Please name: ').strip()
        if name != 'alex':
            raise AlexException
        else:
            break

    except AlexException:
        print 'NONONONO'