class Solution:
    """
    Time complexity:  O(n)
    Space complexity: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        
        maximumArea = 0
        l, r = 0, len(height) - 1

        while l < r:
            # compute the area between the current indexes
            area = min(height[l], height[r]) * (r - l)
            maximumArea = max(area, maximumArea)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maximumArea