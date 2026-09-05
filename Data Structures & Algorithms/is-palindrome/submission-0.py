class Solution:
    def isPalindrome(self, s):
        
        left = 0
        right = len(s) - 1

        while left < right:

            # Ignore non-alphanumeric characters
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

        