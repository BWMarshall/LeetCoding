class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums)
        while low < high:
            middle = (low + high) // 2
            if nums[middle] < target:
                low = middle + 1
            else:
                high = middle

        return low
            
        