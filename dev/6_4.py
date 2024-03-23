# 6.7
first_person = {'first_name':'Bill','last_name':'Evans','age':'32','city':'New York'}
second_person = {'first_name':'John','last_name':'Coltrane','age':'51','city':'London'}
third_person = {'first_name':'Mccoy','last_name':'Tyner','age':'45','city':'London'}
person = [first_person,second_person,third_person]
for i in person:
    print(i)
###*###
# 6.8
pet1={'type':'Poodle','name':'Edgar'}
pet2={'type':'Shepherd Dog','name':'Daniel'}
pet3={'type':'Schnauzer','name':'Cody'}
pets=[pet1,pet2,pet3]
for i in pets:
    print(i)
###*###
# 6.9
favorite_places = {
    'name':'Ford','place':'Istanbul',
    'name':'Gino','place':'Malta',
    'name':'Hayden','place':'Venice'
}
print('name:',favorite_places.keys())
print('place:',favorite_places.values())
###*###
# 6.10
favorite_num={
    'Adam':[1,2],
    'John':[1,2],
    'Davis':[1,2],
    'Chet':[1,2],
    'Bill':[1,2]
}
print(favorite_num)
###*###
# 6.11
city = {
    'city1':{'country':'country1','population':'1','fact':'a'},
    'city2':{'country':'country2','population':'2','fact':'b'},
    'city3':{'country':'country3','population':'3','fact':'c'}
}
print(city)