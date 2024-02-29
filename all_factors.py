def find_all_factors(num):
    # 此处写你的代码
    L=[] 
    if num<1:
        return L
    for i in range(1,num+1):
        if num%i==0:
            L.append(i)
    return L


# 输入一个数字 
num = int(input())

# 调用函数 
print(find_all_factors(num))