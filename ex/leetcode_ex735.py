class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for i in asteroids:
            add = True
            if i < 0:
                while ans and ans[-1] >0 and ans[-1] < -i:
                    ans.pop()
                if ans and ans[-1] > 0:
                    add = False
                    if ans[-1] == -i:
                        ans.pop()
            if add:
                ans.append(i)
        return ans