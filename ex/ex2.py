def find_unique_number(num_list):
    # 此处编写你的代码 
    n=len(num_list)
    if n==1:
        return num_list[0]
    if n==0:
        return None
    for i in range(n):
        if num_list[i] not in num_list[:i] and num_list[i] not in num_list[i+1:]:
            return num_list[i]
    else:
            return None
# 将输入的整数转换为列表
numbers = list(map(int, input().split()))
# 调用函数
print(find_unique_number(numbers))