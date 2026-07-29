class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # thoughts
        # - ordered array means we can begin from the start of the array: index1
        # - use the same way for check for two sum which is to store diff instead

        # convert to map first
        numMap = {}
        for i, num in enumerate(numbers):
            numMap[num] = i
        
        map = {}    # key -> val  
        # loop through numbers
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in numMap and numMap[diff] > idx:
                return [idx+1, numMap[diff]+1] # return as 1-indexed
