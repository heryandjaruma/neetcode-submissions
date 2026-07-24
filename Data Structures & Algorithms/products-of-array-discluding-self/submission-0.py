class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # thought process
        # the hint is to use prefix and suffix
        # that means maybe we can try to calculate
        # all numbers from left to right as prefix
        # and right to left as suffix

        prefix = []
        suffix = []
        # for i in range(1, len(nums)): # start, stop
        #     if i == 1:
        #         prefix.append(nums[i-1])
        #     if i > 1:
        #         prefix.append(prefix[i-2] * nums[i-1])
        for i in range(len(nums) - 1, 0, -1): # start, stop, step
            if (i-1) == (len(nums) - 2):
                suffix.append(nums[len(nums)-1])
            if (i-1) < len(nums) - 2:
                print((i-1), nums[i], len(nums))
                suffix.append(nums[i])
            print(suffix)