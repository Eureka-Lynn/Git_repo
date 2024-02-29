# 编写一个程序来求出前n个奇数。

# 定义函数find_first_n_odds()，参数为n。
# 在函数内部，返回前n个奇数的列表。

def find_first_n_odds(n):
    # 此处写你的代码 
    l=[]
    x=0
    y=1
    while x<n:
        L=l.append(y)
        y=y+2
        x=x+1
    return l
# 获取输入n
n = int(input())
# 调用函数
print(find_first_n_odds(n))