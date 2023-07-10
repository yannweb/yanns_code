class Solution(object):
    def isPalindrome(self, x):
        """
        :param x: int
        :return: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x > 0:
            l = x // div
            r = x % 10

            if l != r:
                return False
            x %= div
            x //= 10
            div /= 100
        return True


if __name__ == '__main__':
    assert Solution().isPalindrome(123) == False
    assert Solution().isPalindrome(123321) == True
    assert Solution().isPalindrome(-121) == False
