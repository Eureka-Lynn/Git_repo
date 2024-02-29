from functools import reduce
def multiply_numbers_in_string(num_string):
    # 将字符串输入转换为列表
    num_list = list(map(int, num_string.split()))
    # 在此处编写你的代码
    return reduce(lambda x,y:x*y,num_list)
# 获取输入字符串
num_string = input()
# 调用函数
print(multiply_numbers_in_string(num_string))