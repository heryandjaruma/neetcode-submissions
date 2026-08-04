class Solution:
    def trap(self, height: List[int]) -> int:
        # thoughts
        # - we need to loop through a "Gap" which is
        # identified by having at least 1 block gap.
        # it's a boundary that somehow shapes "U"
        # - the clue says that we can use prefix and suffix
        # approach which is stores the top highest bar from left to right or from right to left
        # - a good approach is to keep in mind that
        # if there is taller bar in between height[i],
        # then to find is just min(bar left, bar light) - height[i].
        size = len(height)
        # list all suffix
        prefix = []
        for el in height:
            if not prefix:
                prefix.append(el)
            elif el > prefix[-1]:
                prefix.append(el)
            else:
                prefix.append(prefix[-1])
        # search for suffix
        suffix = []
        reversedHeight = height[::-1]
        for el in reversedHeight:
            if not suffix:
                suffix.append(el)
            elif el > suffix[-1]:
                suffix.append(el)
            else:
                suffix.append(suffix[-1])
        suffix = suffix[::-1]
        water = 0
        for i, el in enumerate(height):
            currentWater = min(prefix[i], suffix[i]) - height[i]
            water += currentWater
        return water