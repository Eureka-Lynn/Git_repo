class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        l = []
        L = []
        for i in nums1:
            L.append(i)
            l.append(i[0])
        for i in nums2:
            if i[0] in l:
                for n in range(len(L)):
                    if L[n][0] == i[0]:
                        L[n][1] += i[1]
            else:
                L.append(i)
            L.sort(key= lambda x: x[0])
        return L