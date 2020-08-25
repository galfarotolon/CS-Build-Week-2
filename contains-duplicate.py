class Solution():
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # create an empty dict
        d = {}
        
        #for each number in the nums array
        for n in nums:
            # if the number is already in dict (i.e. theres a dupe)
            if n in d:
                # return True
                return True
            else:
                # otherwise, add it to the dict and make its val be 1
                
                d[n] = 1
        # return False if there are no dupes in the dict already
        return False


nums = [1, 2, 3, 4, 4, 5, 5, 6, 7]
nums2 = [8, 7, 6, 5, 4]
nums3 = [-1, 1, -1]

s = Solution()

print(s.containsDuplicate(nums))
print(s.containsDuplicate(nums2))
print(s.containsDuplicate(nums3))
