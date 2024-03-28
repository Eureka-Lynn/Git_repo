class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        def compare(x:list):
            for i in range(len(x)-1):
                if x[i] >= x[i+1]:
                    return False
            else:
                return True
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                l1 = list(nums)
                l2 = list(nums)
                del l1[i]
                del l2[i+1]
                if compare(l1) or compare (l2):
                    return True
                else :
                    return False
        else:
            return True