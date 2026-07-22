class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a frequency map first
        map = {} # key -> val    num -> freq

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        # then init a list of list where the inner list is which num has that frequency
        freq = [[] for _ in range(len(nums) + 1)] # +1 because we want to disntict bucket for 0 and for 1
        for num, count in map.items():
            freq[count].append(num)
        
        # then return top most k value from the biggest which is from the freq arr with the biggest index
        returnVal = []
        for i in range(len(freq) - 1, 0, -1): # prevent out of index ; ; goes backwards
            for num in freq[i]:
                returnVal.append(num)
                if len(returnVal) == k:
                    return returnVal

# What I was wrong
# > I thought I can build the frequency map while doing the frequency count map
# Apparently need to finish the frequency count then make it as list

# Time Complexity
# - Build the char count : O(n)
# - Build the frequency list : O(n)
# - Returning the array : At most as many as the nums itself O(n)
# Space Complexity
# O(n) since we init freq count and list as much as n