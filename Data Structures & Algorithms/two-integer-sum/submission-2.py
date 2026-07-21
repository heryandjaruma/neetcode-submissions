class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Improved thought
        # Is to use hashmap

        # instead of using num as index, we use diff as index
        # this why after every substraction we check if that exist
        # meaning we found a match
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                return [map[num], i]
            diff = target - num
            if diff not in map:
                map[diff] = i