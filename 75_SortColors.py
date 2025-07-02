from collections import defaultdict

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = defaultdict(int)
        ##Count
        for item in nums:
            counter[item] += 1
        ##Replace
        for x in range(len(nums)):
            if counter[0] > 0:
                nums[x] = 0
                counter[0] -= 1
            elif counter[1] > 0:
                nums[x] = 1
                counter[1] -= 1
            elif counter[2] > 0:
                nums[x] = 2
                counter[2] -= 1
        