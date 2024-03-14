class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int: 
        t=duration
        n=len(timeSeries)
        for i in range(n-1):
            t=t+min((timeSeries[i+1]-timeSeries[i]),duration)
        return t