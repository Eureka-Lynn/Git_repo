class Solution():
    def countBinarySubstrings(self,s:str):
        l=[]
        p=0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                l.append(len(s[p:i+1]))
                p=i+1
        l.append(len(s[p:]))
        return l



s=Solution()
print(s.countBinarySubstrings(s='110011001111'))