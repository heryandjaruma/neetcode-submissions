class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # thought
        # 1. we need to iterate all element once to map
        # what number we have

        # identify start element:
        # only if it's prev element is not num - 1

        # to check exist or not
        # can use hash map to check if it's exist

        # build hash
        map = {}    # key -> val        num -> _ #
        for num in nums:
            if num not in map:
                map[num] = 1 + map.get(num, 0)
            else:
                # skip
                pass
        print(map)
        
        # iterate again from array to check the start element
        consecutive = {}    # keeps track of the start node and how many consecutive?
                            # key -> val        startingElement -> consecutive occurence
        for num, occurence in map.items():
            if (num-1) != map:
                print("first", num-1)
                # start element
                consecutive[num]  = 1 # consecutive need 2
                map[num] = num # start number is itself
            elif (num-1) in map:
                # has to be consecutive
                # backtrack by equals the start
                
                # count diff -> get the (num-1) origin
                origin = map[nums-1]
                consecutive[origin] += 1
                map[num] = origin
        
        print(consecutive)
        
        # lastly check who is the largest
        largest = (-10)**9 - 1 # from constraint
        for num, consecutiveCount in consecutive.items():
            if consecutiveCount > largest:
                largest = consecutiveCount
        
        return largest
