class Solution(object):
    
    def strStr(self,haystack,needles):
        if len(needles) == 0:
            return 0
        m = len(haystack)
        n = len(needles)

        if m < n:
            return -1
        
        for i in range(m-n+1):
            j=0
            for j in range(n):
                if haystack[i+j] != needles[j]:
                    break
            if (j+1) == n:
                return i
        return -1

assert Solution().strStr("helllo","ll") == 2
assert Solution().strStr("aaaaa","bba") == -1
