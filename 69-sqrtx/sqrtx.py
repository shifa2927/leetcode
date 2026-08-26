class Solution(object):
    def mySqrt(self, x):
        
        n=0
        while n*n<=x:
            n=n+1
        return n-1
        