class Solution:
    def minOperations(self, nums: list[int]) -> int:
        p = 1
        n = len(nums)
        cost = 0
        while p <= len(nums)-1:
            if nums[p] > nums[p-1]:
                p += 1
            else :
                diff = nums[p-1] - nums[p]
                cost += diff+1
                nums[p] += diff+1
        return cost