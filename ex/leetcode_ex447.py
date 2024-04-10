class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        from collections import Counter
        ans = 0
        for x1, y1 in points:
            cnt = Counter()
            for x2, y2 in points:
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                ans += cnt[distance] * 2
                cnt[distance] += 1
        return ans




s = Solution()
print(s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))