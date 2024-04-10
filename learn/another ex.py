def find_unique_number(num_list):
    # 此处编写你的代码 
    n=len(numbers)
    for i in range(n):
        count=numbers.count(i)
        if count==1:
            print(numbers[i])
# 将输入的整数转换为列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique_number(numbers))