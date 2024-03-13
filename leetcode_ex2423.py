class Solution:
    def equalFrequency(self, word: str) -> bool:
                from collections import Counter
                c=Counter(word)
                l=c.most_common()
                L=[]
                for i in range(len(l)):
                    L.append(l[i][1])
                L.sort()
                print(L)
                if len(L)==1:
                    return True
                elif L[0]==1 and len(set(L[1:]))==1 :
                    return True
                elif L[-1]==L[-2]+1 and len(set(L[:-1]))==1 :
                    return True
                else:
                    return False 