class Solution(object):
    
    def divide(self,dividend,divisor):
        if dividend == -0xFFFFFFFF//2 and divisor == -1:
            return 0xFFFFFFFF//2
        m = abs(dividend)
        n = abs(divisor)
        res = 0

        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        if n == 1:
            return m if sign == 1 else -m
        while m >= n:
            t,p=(n,1)
            while (m >=(t << 1)):
                t <<= 1
                p <<= 1
            res += p
            m -= t
        return res if sign == 1 else -res


assert Solution().divide(10,3) == 3
assert Solution().divide(7,-3) == -2
