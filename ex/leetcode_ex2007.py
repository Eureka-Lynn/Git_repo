class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        from collections import Counter
        changed.sort()
        ans = []
        cnt = Counter()
        for i in changed:
            if i not in cnt:
                cnt[i*2] += 1
                ans.append(i)
            elif i in cnt:
                cnt[i] -= 1
                if cnt[i] == 0:
                    del cnt[i]
        if cnt:
            return []
        else:
            return ans