class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Improved thought
        # Is to use hashmap

        # instead of using num as index, we use diff as index
        # this why after every substraction we check if that exist
        # meaning we found a match
        map = {}
        for i, num in enumerate(nums): # iterate each element with idx
            if num in map: # check if num in map -> meaning current num has already its processed target - diff
                return [map[num], i] # when found return the idx from map[num], curr item idx
            diff = target - num
            if diff not in map: # otherwise caluclate diff and add to arr
                map[diff] = i