class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans = ''
        l = list(map(str,digits))
        for i in l:
            ans += i
        ans = int(ans)
        ans += 1
        ans = str(ans)
        digits = list(ans)
        answer = list(map(int,digits))
        return answer