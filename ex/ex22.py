def count_binary_ones(num):
    # 此处写你的代码 
    num=bin(num)
    a=num.count('1')
    return a
# 从标准输入读取一个整数
num = int(input())
# 调用函数
print(count_binary_ones(num))