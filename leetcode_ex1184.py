class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        t=sum(distance)
        if start>destination:
            return min(sum(distance[destination:start]),t-sum(distance[destination:start]))
        if destination>start:
            return min(sum(distance[start:destination]),t-sum(distance[start:destination]))


s=Solution()
print(s.distanceBetweenBusStops(distance = [1,2,3,4], start = 0, destination = 3))