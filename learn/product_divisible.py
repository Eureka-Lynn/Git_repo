from functools import reduce
def cheng(a,b):
    return a*b
def is_product_divisible_by_sum(numbers_list):
    # 此处编写代码 
    s1=sum(numbers_list)
    s2=reduce(cheng,numbers_list)
    if s2%s1==0:
        return True
    else:
        return False
# 获取整数输入并将其转换为列表
numbers_list = list(map(int, input().split()))
# 调用函数打印结果
print(is_product_divisible_by_sum(numbers_list))