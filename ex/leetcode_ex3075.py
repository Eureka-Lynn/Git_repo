class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        i,j,ans = 0,0,0
        happiness = sorted(happiness,reverse = True)
        while True:
            ans += max(happiness[i]-j,0)
            if happiness[i] == 1:
                break
            if j == k-1:
                break
            i += 1
            j += 1
        return ans