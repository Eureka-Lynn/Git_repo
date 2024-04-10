class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list=sentence.split()
        searchWord_length=len(searchWord)
        sentence_length=len(sentence_list)
        for i in range(sentence_length):
            if searchWord==sentence_list[i][0:searchWord_length]:
                return i
            else:
                pass

Solution.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg")