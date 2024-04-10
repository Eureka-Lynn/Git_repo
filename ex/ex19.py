def ends_with(string1, string2):
    # 此处写你的代码
    l=len(string2)
    if string1[-l:]==string2:
        return True
    else:
        return False
# 获取输入字符串
string1 = input()
string2 = input()
# 调用函数
print(ends_with(string1, string2))