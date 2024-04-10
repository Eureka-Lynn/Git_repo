def are_anagrams(string1, string2):
    # 此处编写代码 
    str1=string1.lower().replace(' ','')
    str2=string2.lower().replace(' ','')
    L1=list(str1)
    L2=list(str2)
    S1=set(L1)
    S2=set(L2)
    if S1==S2:
        return True
    else:
        return False
# 获取输入string1 和 string2 
string1 = input()
string2 = input()
# 调用函数并打印结果 
print(are_anagrams(string1, string2))