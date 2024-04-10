def find_even_numbers(num):
    # 此处写入代码 
    if num<=1:
        return []
    if num%2==0:
        a=[num for num in range(2,num+1,2)]
    else:   
        a=[i for i in range(2,num,2)]
    return a
# 获取整数输入
num = int(input())
# 调用函数
print(find_even_numbers(num))