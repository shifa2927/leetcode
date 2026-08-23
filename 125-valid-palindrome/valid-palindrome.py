class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(c.lower() for c in s if c.isalnum())
        
        if s==s[::-1]:
            return True
        else:
            return False
        