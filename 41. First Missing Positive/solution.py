class Solution:
    #Solution using HashSet
    #Time complexity: O(n)
    #Space complexity: O(n) (for HashSet)


    def firstMissingPositive(self, nums: List[int]) -> int:
        
        numSet = set()

        for num in nums:
            if num > 0:
                numSet.add(num)

        index = 1
        while index in numSet:
            index += 1

        return index