class Solution(object):
    def romanToInt(self, s):
        """
        :param s: str
        :return: int
        """

        map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        n = len(s)
        for i, v in enumerate(s):
            value = map[v]
            if i < n - 1 and value < map[s[i + 1]]:
                result -= value
            else:
                result += value
        return result

    # Test cases


if __name__ == "__main__":
    assert Solution().romanToInt("XII") == 12
    assert Solution().romanToInt("XXI") == 21
    assert Solution().romanToInt("XCIX") == 99
