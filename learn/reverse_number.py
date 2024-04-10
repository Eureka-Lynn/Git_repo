def reverse_number_digits(num):
    # 在此处编写你的代码
    L=[]
    for x in num:
        int(x)
        L.append(x)
    L1=L[::-1]
    L1=list(map(int,L1))
    return L1
# 获取用户输入
num = input()

# 调用函数
print(reverse_number_digits(num))