class Solution():
    def countBinarySubstrings(self,s:str):
        l=[]
        p=0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                l.append(len(s[p:i+1]))
                p=i+1
        l.append(len(s[p:]))
        t = 0
        for x in range(len(l)-1):
            a= min(l[x],l[x+1])
            t = t+a
        return t