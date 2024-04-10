from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
            total = 0
            count = Counter(nums)
            for k,v in count.most_common():
                if v >= 2:
                  total += v*(v-1)/2
            return int(total)