class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        right_sum,left_sum,ans = sum(nums),0,0
        for i in nums:
            right_sum -= i
            if left_sum == right_sum:
                return ans
            ans += 1
            left_sum += i
        return -1