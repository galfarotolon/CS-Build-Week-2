class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        result = []
    
        for index, num in enumerate(nums):
            # during first iteration, dict is always empty
            if d.get(num) is None:
                # do the target value - num
                # and store that in the dict
                # value is the index position of the target - num
                d[target-num] = index
            else:
                # if the num is already in the dict
                # result is the index of d[num] and the next value's index
                result = [d[num], index]
        return result



s = Solution()

print(s.twoSum([5, 6], 11))
print(s.twoSum([2, 7, 11, 15], 26))

