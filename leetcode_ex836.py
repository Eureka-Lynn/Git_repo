class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        if rec1[2] <= rec2[0] or rec1[0] >= rec2[2] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1] :
            return False
        else :
            return True