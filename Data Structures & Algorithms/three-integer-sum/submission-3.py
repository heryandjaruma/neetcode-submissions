class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # th process

        # - hint say that array must be sorted
        # - rearranging num1+num2+num3=0, we can dervie
        # that -num1 = num2+num3
        # - the -num1 is naturally to be in the left side
        # of sorted array so we can use sliding window
        # on the right elements of the `i`
        result = []
        nums = sorted(nums)
        size = len(nums)
        i, j, k = 0, 1, size - 1
        while i < (size - 2): # check up until size - 2
            if i > 0 and nums[i] == nums[i-1]: # to check if i is duplicate then just advanced to the last i
                i += 1


            # print(f"loop {i}")
            # target -> -num1
            target = -(nums[i])
            # new index
            j, k = i+1, size-1
            while j < k: # sliding window
                # print(i, j, k)
                add = nums[j] + nums[k]
                if target == add: # then add the nums to result
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # these because the closer they are it's more likely they can find another match
                    while j < k and nums[j] == nums[j - 1]: # check duplicate left
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: # check duplicate right
                        k -= 1

                elif target > add:
                    j += 1
                elif target < add:
                    k -= 1
                
            # skip the current i until it's a different because it will be duplicate
            # then increase j to prevent double value
            i+=1
        return result