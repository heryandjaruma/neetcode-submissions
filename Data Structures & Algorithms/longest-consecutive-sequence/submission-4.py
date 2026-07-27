class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # thought
        # 1. we need to iterate all element once to map
        # what number we have

        # identify start element:
        # only if it's prev element is not num - 1

        # to check exist or not
        # can use hash map to check if it's exist
        
        # early return for empty arr
        if not nums:
            return 0

        # build hash
        map = {}    # key -> val        num -> _ #
        for num in nums:
            if num not in map:
                map[num] = 1 + map.get(num, 0)
            else:
                # skip
                pass
        
        # iterate from anywhere and check the consecutive
        # remove element along the way
        # start with random element
        largestConsecutive = (-10**9) - 1
        for num, _ in map.items():

            if (num-1) not in map: # check for start node
                # is a start node
                consecutive = 1
                while True:
                    if (num+consecutive) in map:
                        consecutive += 1
                    else: # consecutive not in map
                        break
                
                if consecutive > largestConsecutive:
                    largestConsecutive = consecutive

            else:   # not a start node
                pass
        return largestConsecutive

# Time Complexity
# O(n) -> iterate through element and check for its consecutive
# will be at max is just the total number itself

# Space Complexity
# O(n) only need to build the map


# TODO: wth is this
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         mp = defaultdict(int)
#         res = 0

#         for num in nums:
#             if not mp[num]:
#                 mp[num] = mp[num - 1] + mp[num + 1] + 1
#                 mp[num - mp[num - 1]] = mp[num]
#                 mp[num + mp[num + 1]] = mp[num]
#                 res = max(res, mp[num])
#         return res