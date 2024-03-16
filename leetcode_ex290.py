# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#          s=s.split()
#          if len(s)!=len(pattern):
#              return False
#          for i in range(len(pattern)-1):
#              for j in range(1,len(pattern)):
#                  if pattern[i]==pattern[j]:
#                      if s[i]!=s[j]:
#                          return False
#                  if pattern[i]!=pattern[j]:
#                      if s[i]==s[j]:
#                          return False
#          else:
#              return True


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p2s = {}        # pattern中的字符到s中的字符子串的映射表
        s2p = {}        # s中的字符字串到pattern中的字符的映射表
        words = s.split(" ")    # 根据空格，提取s中的单词
        if len(pattern) != len(words):
            return False    # 字符数和单词数不一致，一定不匹配
        for ch, word in zip(pattern, words):
            if (ch in p2s and p2s[ch] != word) or (word in s2p and s2p[word] != ch):
                # 字符与单词没有一一映射：即字符记录的映射不是当前单词或单词记录的映射不是当前字符
                return False
            # 更新映射，已存在的映射更新后仍然是不变的；不存在的映射将被加入
            p2s[ch] = word
            s2p[word] = ch
        return True


s=Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))