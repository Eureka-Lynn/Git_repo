class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        ans , cnt = 0 , 0
        m = max(nums)
        left = 0
        for right in nums:
            if right == m:
                cnt += 1
            while cnt == k:
                if nums[left] == m:
                    cnt -= 1
                left += 1
            ans += left
        return ans