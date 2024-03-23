# 3.4
persons = ['first person','second person','third person']
for i in persons:
    print(f'invite {i} to have a dinner')
###*###
# 3.5
for i in persons:
    print(f'invite {i} to have a dinner')
print(f'{persons[2]} is unable to attend appointments')
persons[2]='another one'
for i in persons:
    print(f'invite {i} to have a dinner')
###*###
# 3.6
for i in persons:
    print(f'invite {i} to have a dinner')
print(f'{persons[2]} is unable to attend appointments')
persons[2]='another one'
for i in persons:
    print(f'invite {i} to have a dinner')
print('now we have a bigger table')
persons.insert(0,'new first')
persons.insert(len(persons)//2,'new second')
persons.append('new third')
for i in persons:
    print(f'invite {i} to have a dinner')
###*###
# 3.7
person = ['first person','second person','third person']
for i in person:
    print(f'invite {i} to have a dinner')
print(f'{person[2]} is unable to attend appointments')
person[2]='another one'
for i in person:
    print(f'invite {i} to have a dinner')
print('now we have a bigger table')
person.insert(0,'new first')
person.insert(len(person)//2,'new second')
person.append('new third')
for i in person:
    print(f'invite {i} to have a dinner')
print('only two of them can be invited')
while len(person) > 2:
    x = person.pop()
    print(f'sorry {x}')
for i in person:
    print(f'{i},we will invite you')
del person[0]
del person[0]
print(person)