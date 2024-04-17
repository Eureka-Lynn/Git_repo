class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        tmp = nums.index(1)
        ans += tmp
        del nums[tmp]
        nums.insert(0, 1)
        tmp = nums.index(l)
        ans += l - tmp - 1
        return ans