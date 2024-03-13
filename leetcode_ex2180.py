# 暴力法
class Solution:
    def countEven(self, num: int) -> int:
            t=0
            for i in range(1,num+1):
                 if self.get_value(i)%2==0:
                      t=t+1
            return t
                      
    def get_value(self,num):
        sum=0
        while num>0:
            sum=num%10+sum
            num=num//10
        return sum