def calc_tetrahedral_number(n):
    # 在此处编写你的代码
    Tn = (n * (n + 1) * (n + 2)) / 6
    Tn=int(Tn)
    return Tn
# 输入整数
num = int(input())
# 调用函数
print(calc_tetrahedral_number(num))