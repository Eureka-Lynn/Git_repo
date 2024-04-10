class Solution:
    def similarPairs(self, words: list[str]) -> int:
            count = 0
            i = 0
            words = list(map(set,words))
            for i in range(len(words)-1):
                  for j in range(i+1,len(words)):
                        if words[i] == words[j]:
                              count += 1
            return count