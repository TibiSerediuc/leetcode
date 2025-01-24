class Solution:
    """
    Time complexity:  O(n) -> 3 * O(n)
    Space complexity: O(n) -> 2 * O(n)
    """
    def trap(self, height: List[int]) -> int:
        
        #basically the water that can be contained at each index is based on the 
        #maximum height of the walls from the left and the right and the current height
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        maxHeight = height[0]

        for i in range(1, len(height)):
            prefix[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        maxHeight = height[len(height) - 1]
        for i in range(len(height) - 2, 0, -1):
            suffix[i] = maxHeight
            maxHeight = max(maxHeight, height[i])

        totalWater = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water > 0:
                totalWater += water

        return totalWater