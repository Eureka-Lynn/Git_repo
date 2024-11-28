class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        C = (A & 0xffffffff) ^ (B & 0xffffffff)
        cnt = 0
        while C != 0: # 不断翻转最低位直到为 0
            C = C & (C - 1) # 清除最低位
            cnt += 1
        return cnt