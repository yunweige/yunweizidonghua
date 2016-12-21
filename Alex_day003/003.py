import pickle
account_info = {
    '8906143632':['alex3714', 15000,15000],
    '8908223631':['rachel', 9000,9000],
}

f=file('account.pkl', 'wb')
pickle.dump(account_info, f)
account_info['8908223631'][0]='dsafewq'
pickle.dump(account_info,f)
f.close()