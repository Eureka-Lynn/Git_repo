# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
        #  1 if num is lower than the picked number
        #  otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n) == -1:
            max = n
            min = n//2
            while guess(min) != 0:
                if guess(min) == -1:
                        max,min = min,min//2
                if guess(min) == 1:
                     min = (max + min)//2
        if guess(n) == 1:
             min = n
             max = n*2
             while guess(min) != 0:
                  if guess(max) == -1:
                       min = (max + min)//2
                  if guess(max) == 1:
                       max = max*2
        if guess(n) == 0:
             min = n
        return min