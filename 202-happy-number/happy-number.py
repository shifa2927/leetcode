class Solution(object):
    def isHappy(self, n):
        seen = []
        while n != 1:
            total = 0
            for digit in str(n):
                total = total + int(digit) * int(digit)
            n = total
            if n in seen:
                return False
            seen.append(n)
        return True