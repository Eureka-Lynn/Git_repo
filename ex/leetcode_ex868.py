class Solution:
    def binaryGap(self, n: int) -> int:
        a = 0
        num = bin(n).lstrip('0b')
        l = list(num)
        L = []
        for i in range(len(l)):
            if l[i] == '1':
                L.append(i)
        for i in range(0,len(L)-1):
            a = max(L[i+1]-L[i],a)
        return a