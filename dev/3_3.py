# 3.8
places = ['Spain','Denmark','Singapore','Canada','India']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
###*###
# 3.9
persons = ['first person','second person','third person']
for i in persons:
    print(f'invite {i} to have a dinner')
print(f'{persons[2]} is unable to attend appointments')
persons[2]='another one'
for i in persons:
    print(f'invite {i} to have a dinner')
print(len(persons))
###*###
# 3.10
L=['PHP','CSS','JSON','Python','C++','Rust','Golang','Java','JavaScript']
L.sort()
L.reverse()
print(L)
print(len(L))
print(sorted(L,reverse=False))
L.pop()
L.append('Spring Boot')
L[0]='C'
for i in L:
    print(i)
print(L[3])