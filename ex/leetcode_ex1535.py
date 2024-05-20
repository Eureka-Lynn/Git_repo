class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        win = 0
        mx = arr[0]
        for i in arr:
            if mx > i:
                win += 1
            elif mx < i:
                win = 1
                mx = i
            if win >= k:
                return mx
        return mx