class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height) - 1
        
        prefix = []
        suffix = []

        for i, h in enumerate(height):
            if not prefix:
                prefix.append(h)
            elif h > prefix[-1]:
                prefix.append(h)
            else:
                prefix.append(prefix[-1])

            if not suffix:
                suffix.append(height[size-i])
            elif height[size-i] > suffix[-1]:
                suffix.append(height[size-i])
            else:
                suffix.append(suffix[-1])
            
        suffix = suffix[::-1]

        water = 0
        for i, h in enumerate(height):
            water += min(prefix[i], suffix[i]) - h
        
        return water
            