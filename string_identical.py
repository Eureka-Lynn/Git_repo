def is_string_identical(text_string):
    # 此处编写代码
    L1=list(text_string)
    s1=set(L1)
    if len(s1)==1:
        return True
    else:
        return False
# 获取输入 
text_string = input()
# 调用函数 
print(is_string_identical(text_string))