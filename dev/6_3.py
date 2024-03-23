# 6.4
program={
    'index':'索引',
    'tuple':'元组',
    'Traceback':'回溯',
    'seq':'序列',
    'iterable':'可迭代',
    'function':'函数',
    'superset':'父集',
    'arg':'可变元素',
    'SyntaxError':'语法错误',
    'NameError':'名称错误'
}
for i in program.keys():
    print(i)
for i in program.values():
    print(i)
###*###
# 6.5
rivers={
    'Nile':'Egypt',
    'Amazon':'Brazil',
    'Danube':'Austria'
}
for i in rivers:
    print(f'The {i} runs through {rivers[i]}')
###*###
# 6.6
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}
names=['jen','sarah','davis','billy']
for i in names:
    if i in favorite_languages:
        print(f'{i},thank you for taking part in the survey')
    else:
        print(f'{i},we invite you to take part in the survey')