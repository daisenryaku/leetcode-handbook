# O(1) space not including the input and output variables
# 1<=a[i]<=n (n = size of array)

# Do a linear pass using the input array itself as a hash
# making elements at certain indexes negative.
# value ->  index
# num   ->  abs(num)-1
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                res.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return res
