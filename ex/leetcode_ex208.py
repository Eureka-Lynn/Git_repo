# class Trie:

#     def __init__(self):
#         self.list = Counter()


#     def insert(self, word: str) -> None:
#         if word in self.list.keys():
#             return True
#         self.list[word] += 1



#     def search(self, word: str) -> bool:
#         for i in self.list.keys():
#             if word == i:
#                 return True
#         else:
#             return False


#     def startsWith(self, prefix: str) -> bool:
#         for i in self.list.keys():
#             if str(i).startswith(prefix):
#                 return True
#         else:
#             return False



# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)
from collections import defaultdict
class Node:
    def __init__(self) -> None:
        self.children = defaultdict(Node)
        self.isword = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        current = self.root
        for i in word:
            current = current.children[i]
        current.isword = True


    def search(self, word: str) -> bool:
        current = self.root
        for i in word:
            current = current.children.get(i)
            if current == None:
                return False
        return current.isword


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in prefix:
            current = current.children.get(i)
            if current == None:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)