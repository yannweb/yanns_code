class Solution:
    def LongestPalindromicSubstring(self,s):
        if len(s) < 2:
            return s
        n = len(s)
        maxLen = 1
        for i in range(1,n):
            odd = s[i-maxLen-1:i+1]
            even = s[i-maxLen:i+1]
            if i-maxLen-1 >= 0 and odd == odd[::-1]:    
                start = i - maxLen -1
                maxLen += 2  # math 03
            if i-maxLen >= 0 and even == even[::-1]:
                start = i-maxLen
                maxLen +=1
        return s[start:start+maxLen]  # math 03           

assert Solution().LongestPalindromicSubstring("abccb") == "bccb"

from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():

    test_data = [
                    TestEntry( array = "abccb", target = "abc"),
                    TestEntry( array ="aaa", target = "a"),
                ]
    for t in test_data:

        print( Solution().LongestPalindromicSubstring( s = t.array) )

    return

if __name__ == '__main__':
    test_bench()

