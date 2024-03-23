# 4.10
l = [i**3 for i in range(1,11)]
print(f'The first three items in the list are:{l[0:3]}')
print(f'Three items from the middle of the list are:{l[len(l)// 2 - 1:len(l) // 2 + 2]}')
print(f'The last three items in the list are:{l[-3:]}')
###*###
# 4.11
my_favorite_pizzas = ['California-style Pizza','Greek pizza','Bar pizza']
friend_pizzas = list(my_favorite_pizzas)
my_favorite_pizzas.append('Chicago-Style Pizza')
friend_pizzas.append('New York Style-pizza')
print('My favorite pizzas are:')
for i in my_favorite_pizzas:
    print(i)
print('My friend\'s favorite pizzas are:')
for i in friend_pizzas:
    print(i)
###*###
# 4.12
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
for i in my_foods:
    print(i)
for i in friend_foods:
    print(i)