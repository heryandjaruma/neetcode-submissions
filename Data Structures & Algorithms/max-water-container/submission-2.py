class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # thoughts:
        # - there has to be 2 outer most element, and between
        # is most volume it can contain
        # - what is water volume?
        #   - maybe it's just a square equation
        # - to define the outer most 'pillars'
        #   - index matters: bigger span better
        #   - height matters: taller better

        # to get data
        # two approach:
        # - is to double loop and compare one to other
        # element each O(n2)
        # - use 2 pointers left and right to find
        # current most until in the middle

        # - but how do i keep the most while still finding
        # the bst
        # - actually since we only care about the most volume
        # and not index, then just calculate current span
        # times height
        # advances left and right one at time
        # ^ but this approach is wrong because it assumes that
        # value converges at the middle, while the most calculated
        # can be in between
        # - instead of equal advances, then go with value
        # advances
    
        # index
        l = 0
        r = len(heights) - 1
        mostWater = 0
        while l < r:
            currentMost = (r-l) * min(heights[l], heights[r])
            if currentMost > mostWater:
                mostWater = currentMost
            
            if leftTurn:
                l += 1
                leftTurn = False
            else:
                r -= 1
                leftTurn = True
            if heights[l] < heights[r]:
                l += 1
            else:
                r += 1
        return mostWater
