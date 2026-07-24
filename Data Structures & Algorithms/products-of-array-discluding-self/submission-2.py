class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # thought process
        # the hint is to use prefix and suffix
        # that means maybe we can try to calculate
        # all numbers from left to right as prefix
        # and right to left as suffix

        # then to choose the all multiplier is just to correctly 
        # times from prefix and suffix from which index

        prefix = []
        suffix = []
        for i in range(1, len(nums)): # start, stop
            if i == 1:
                prefix.append(nums[i-1])
            if i > 1:
                prefix.append(prefix[i-2] * nums[i-1])
        for i in range(len(nums) - 1, 0, -1): # start, stop, step
            if (i-1) == (len(nums) - 2):
                suffix.append(nums[len(nums)-1])
            if (i-1) < len(nums) - 2:
                suffix.append(nums[i] * suffix[len(nums) - i - 2])
        res = []
        for i in range(0, len(nums)):
            if i == 0: #first index
                res.append(suffix[len(nums)-2])
            elif i == len(nums)-1: # last index
                res.append(prefix[len(nums)-2])
            else: # in-between
                res.append(prefix[i-1] * suffix[-i-1])
        return res

# Time Complexity
# To calculate prefix O(n)
# To calculate suffix O(n)
# To calculate result array O(n)
# hence O(n)

# Space Complexity
# Array of prefix, suffix, and res grows by limit n for each
# hence O(n)