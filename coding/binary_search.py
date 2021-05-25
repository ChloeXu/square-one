class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    
    def _search(self, arr, target, l, r):
        if l > r:
            return - 1
        print(l, r)
        mid = l + (r - l) / 2

        # print(mid, arr[mid])
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            # left half
            return self._search(arr, target, l, mid - 1)
        elif target > arr[mid]:
            # right half
            return self._search(arr, target, mid + 1, r)


a = [0,2,3,5,6,8,9]
target = 8
l = 0
r = 6
resultInd = Solution()._search(a, 9, 0, len(a) - 1)
print(resultInd)

resultInd = Solution()._search(a, 3, 0, len(a) - 1)
print(resultInd)
