class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        res=0
        g.sort()
        s.sort()
        for i in s:
            if i>=g[res]:
                res=res+1
                if res==len(g):
                    break
        return res