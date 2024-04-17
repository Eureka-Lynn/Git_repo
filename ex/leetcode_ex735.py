class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = []
        for i in asteroids:
            ans.append(i)
            if len(ans) >= 2:
                if ans[-1] < 0 and ans[-2] > 0:
                    if ans[-2] < ans[-1]:
                        del ans[-2]
                    if ans[-2] == ans[-1]:
                        del ans[-1]
                        del ans[-1]
                    if ans[-2] > ans[-1]:
                        del ans[-1]
        return ans

s = Solution()
print(s.asteroidCollision([1,-2,-2,-2]))