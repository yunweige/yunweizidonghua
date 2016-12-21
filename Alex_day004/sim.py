class person:
    assets = 0
    attraction = 0
    skills = []
    love_status = None
    lover = None
    job = None
    company = None

    def __init__(self, name, sex, role):
        self.name = name
        self.sex = sex
        self.role = role
        print '\033[32;1m-\033[0m'*60

        if self.role == 'rich':
            self.assets += 10000000
            self.attraction += 80
            print '\033[32;1mMy name is %s, I am a %s guy, I have %s money! It is good to be rich..\033[0m' % (self.name, self.role, self.assets)
        elif self.role == 'poor':
            self.assets += 5000
            self.attraction += 40
            print '\033[32;1mMy name is %s, I am a %s guy, I have %s money! It is good to be poor..\033[0m' % (self.name, self.role, self.assets)
        elif self.role == 'beauty':
            self.assets += 5000
            self.attraction += 90
            print '\033[32;1mMy name is %s, I am a %s girl, I have %s money! I am very beautiful ...\033[0m' % (self.name, self.role, self.assets)

    def talk(self, msg, tone='normal'):
        if tone == 'normal':
            print '\033[32;1m%s : %s \033[0m' % (self.name,msg)
        elif tone == 'angry':
            print '\033[31;1m%s : %s \033[0m' % (self.name, msg)

    def assets_balance(self, amount, action):
        if action == 'earn':
            self.assets += amount
            print '\033[32;1m%s just made %sRMB! Current assets is %s\033[0m' \
            % (self.name ,amount, self.assets)
        elif action == 'cost':
            self.assets -= amount
            print '\033[32;1m%s just made %sRMB! Current assets is %s\033[0m' \
            % (self.name ,amount, self.assets)


p = person('Alex', 'male', 'rich')
p.talk('Hi guys')
p.assets_balance(5300,'earn')