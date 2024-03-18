class Solution:
    def makeGood(self, s: str) -> str:
        stake=[]
        for chr in s:
            if stake and stake[-1].lower() == chr.lower() and stake[-1] != chr:
                stake.pop()
            else:
                stake.append(chr)
        return "".join(stake)