import pickle
pkl_file = open('account.pkl','rb')
account_list1=pickle.load(pkl_file)
account_list2=pickle.load(pkl_file)


print account_list1
print account_list2