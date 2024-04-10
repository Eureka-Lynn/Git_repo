from collections import Counter
class Solution:
    def findLucky(self, arr: list[int]) -> int:
        count = Counter(arr)
        for k,v in count.most_common():
            if k == v:
                return k
        else:
                return -1