"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

"""
Time complexity : O(n * k) -> O(n)
    n represents the number of input strings
    k represents the max length of a string

Space complexity : O(n * k) (the strings are stored in a hashmap) -> O(n)
"""

#needed for the defaultfict subclass
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #the result is stored in a dict of list
        res = defaultdict(list)

        #iterate through each input string
        for string in strs:
            count = [0] * 26

            #count the frequency of each letter from the string
            for char in string:
                count[ord("a") - ord(char)] += 1

            #we use the frequency array as a key to our dict and store the mathcing strings in a list at that key
            res[tuple(count)].append(string)

        return list(res.values())