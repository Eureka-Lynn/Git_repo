import time
start=time.time()
def check_prime(num):
    # 在此处编写代码
    if num==1 or num==2 or num==3:
        return True
    for i in range(2,num-1):
        if num%i==0:
            return False
    else:
            return True
# 输入一个整数
number = int(input())

# 调用函数
print(check_prime(number))
end=time.time()
print(end-start)