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


    def romanToInt2(self, s:str) -> int:
        mapping_table = {   
                            'I': 1,
                            'V': 5,
                            'X': 10,
                            'L': 50,
                            'C': 100,
                            'D': 500,
                            'M': 1000
                        }

        number = 0

        for i, char in enumerate(s):
            number += mapping_table[char]
            if i and (mapping_table[char] > mapping_table[s[i-1]]):
                      number -= 2 * mapping_table[s[i-1]]

        return number

if __name__ == "__main__":
    assert Solution().romanToInt("XII") == 12
    assert Solution().romanToInt("XXI") == 21
    assert Solution().romanToInt2("XCIX") == 99
    assert Solution().romanToInt2("LVIII") == 58
