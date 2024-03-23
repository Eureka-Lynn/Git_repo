# 5.8
Users = ['admin','user1','uesr2','user3','user4']
for i in Users:
    if i == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print(f'Hello {i},thank you for logging in again')
###*###
# 5.9
del Users[:]
if Users == []:
    print('We need to find some users!')
for i in Users:
    if i == 'admin':
        print('Hello admin,would you like to see a status report?')
    else:
        print(f'Hello {i},thank you for logging in again')
###*###
# 5.10
current_users = ['User1','User2','User3','user4','user5']
new_users = ['user1','user3','User6','user7','user8']
current_users_lower=[]
for i in current_users:
    current_users_lower.append(i.lower())
for i in new_users:
    if i in current_users_lower:
        print('username already exist!')
    else:
        print('username able to use!')
###*###
# 5.11
l=[i for i in range(1,10)]
for i in l:
    if i == 1:
        print('1st')
    elif i ==2:
        print('2nd')
    else:
        print(f'{i}th')