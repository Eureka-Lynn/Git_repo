class Solution:
    def leftRightDifference(self, nums: list[int]) ->list[int]:
        ans , left_sum , right_sum = [] , sum(nums) , 0
        for i in nums:
            right_sum -= i
            ans.append(abs(right_sum - left_sum))
            left_sum += i
        return ans