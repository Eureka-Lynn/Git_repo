def vowel_count(string):
    n=0
    # 此处写你的代码
    for x in input_string:
        if x==('a'or'e'or'i'or'o'or'u'):
        #这种if表达是错误的
            n=n+1
    return n
# 获取输入字符串 
input_string = input()
# 调用函数 
print(vowel_count(input_string))