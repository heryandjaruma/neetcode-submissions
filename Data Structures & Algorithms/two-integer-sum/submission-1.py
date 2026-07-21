class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initial Thought
        # A sliding window approach would be possible
        # Where i starts at index 0 and j at 1
        # However it will have time complexity O(n^2) since
        # at max it would check the match almost every element.
        return [0,1]