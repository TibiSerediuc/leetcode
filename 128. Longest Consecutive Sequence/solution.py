class Solution:
    """
    Time complexity:  O(n)
    Space complexity: O(1)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #convert the list to set
        numsSet = set(nums)
        maxSeq = 0
        for num in numsSet:

            sequence = 1
            #if the number is not the start of a sequence we will ignore it as it cannot be
            #the start of the longest sequence
            if (num - 1) in numsSet:
                continue

            j = 1
            #while there are consecutive elements that start with num, we count them
            while (num + j) in numsSet:
                j += 1
                sequence += 1

            #update the maximum length of sequence
            if sequence > maxSeq:
                maxSeq = sequence

        return maxSeq
