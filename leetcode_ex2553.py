class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=''
        nums = list(map(str,nums))
        for i in nums:
            l += i
        answer = list(map(int,list(l)))
        return answer