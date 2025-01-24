class Solution:

    """
    Time complexity: O(n): O(n)   to remove all the non alphanumerical characters
                           O(n)   to convert to lowercase
                           O(n/2) to check if is palindrome
    
    Space complexity: O(n): O(n) to remove all the non alphanumerical characters
                            O(n) to convert to lowercase
                            O(1) to check if is palindrome
    """
    def removeNonAlphanumeric(self, s: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    def isPalindrome(self, s: str) -> bool:
        
        updatedString = self.removeNonAlphanumeric(s)
        print(updatedString)
        l, r = 0, len(updatedString) - 1

        while l <= r:
            if updatedString[l] != updatedString[r]:
                return False
            l += 1
            r -= 1
        return True
