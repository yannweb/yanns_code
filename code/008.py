class Solution(object):
    def myAtoi(self,s):
        if not s:
            return 0
        sign = 1
        s=s.lstrip()
        if not s:
            return 0
        if s[0] == '+' or s[0] == '-':
            sign = 1 if s[0] == '+' else -1
            s=s[1:]
        # print(s)
        if not s:
            return 0
        result = 0
        for i in range(len(s)):
            digit = ord(s[i]) - ord('0')
            if digit < 0 or digit > 9:
                break
            result = result * 10 + digit
        result *= sign
        if result > 0:
            return result if result <= 0xFFFFFFFF//2 else 0xFFFFFFFF//2
        return result if result > -0xFFFFFFFF//2 else -0xFFFFFFFF//2

# print(Solution().myAtoi("-99999999999999"))
assert Solution().myAtoi("-99999999999999") ==   -2147483648 
# Tabnine AI
