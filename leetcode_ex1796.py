# class Solution:
#     def secondHighest(self, s: str) -> int:
#         a=b=-1
#         for c in s:
#             if c.isdigit():
#                 v=int(c)
#                 if v>a:
#                     a,b=v,a
#                 elif b<v<a:
#                     b=v
#         return b


class Soulution():
    def secondHighest(self,s:str):
        l=[]
        for c in s:
            if c.isdigit():
                c=int(c)
                l.append(c)
        n=len(c)
        
