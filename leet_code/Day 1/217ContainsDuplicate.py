class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        X = 0
        array = []
        array[::] = list(set(nums))
        if len(array) < len(nums):
            return True
        else:
            return False
