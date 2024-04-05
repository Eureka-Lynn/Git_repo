class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        count = 0
        l = 'aeiou'
        words = words[left:right+1]
        for i in words:
            if i[0] in l and i[-1] in l:
                count += 1
        return count