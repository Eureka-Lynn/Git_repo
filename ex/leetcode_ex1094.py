class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        total = 0
        all = 0
        for i in trips:
            all += i[0]
        if all <= capacity:
            return True
        pick = sorted(trips,key = lambda x : x[1])
        drop = sorted(trips,key = lambda x : x[2])
        for i in pick:
            distance = i[1]
            total += i[0]
            while distance >= drop[0][2]:
                total -= drop[0][0]
                del drop[0]
            if total > capacity:
                return False
        else :
            return True


s = Solution()
print(s.carPooling([[3,2,8],[4,4,6],[10,8,9]],11))