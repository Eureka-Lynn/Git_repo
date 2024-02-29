def findMinAndMax (x):
    if x==[]:
        return (None,None)
    else:
        max=x[0]
        min=x[0]
    for c in x:
        if c>=max:
            max=c
    for c in x:
        if c<=min:
            min=c
    return (min,max)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')