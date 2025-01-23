class Solution:
    """
    This solution has linear complexity for both time and space
    Time: O(n)
    Space: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # count how many times each element appears and store it in a HashMap
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # store the count in a list where the index represents the frequency and each element is 
        # a list containing the elements that has the same number of aparitions as the index
        for key, value in count.items():
            freq[value].append(key)

        result = []
        # iterate through the aparitions list (from largest to smallest) and append elements to result
        # until k elements are added
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
