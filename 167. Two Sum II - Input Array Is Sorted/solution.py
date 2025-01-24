class Solution:
    """
    Time complexity:  O(n)
    Space complexity: O(1)
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers method, start with pointers at both ends of the array then move one of the pointers 
        # based on the sum of the variables
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]