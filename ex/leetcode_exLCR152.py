class Solution:
    def verifyTreeOrder(self, postorder: list[int]) -> bool:
        def pre_order(left,root):
            if left >= root:
                return True
            p = left
            while postorder[p] < postorder[root]:
                p += 1
            m = p
            while postorder[p] > postorder[root]:
                p += 1
            return p == root and pre_order(left,m-1) and pre_order(m,root-1)
        return pre_order(0,len(postorder)-1)