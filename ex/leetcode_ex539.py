class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        l = []
        ans = 1440
        for i in timePoints:
            l.append(list(map(int,i.split(':'))))
        for i in range(len(l)):
            l[i] = l[i][0] * 60 + l[i][1]
        l = sorted(l)
        right = 1
        left = 0
        current = l[right] - l[left]
        if current < ans:
            ans = current
        right += 1
        left += 1
        if right == len(l):
            return min(ans,1440-l[-1]+l[0])