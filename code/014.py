class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :param strs: List[str]
        :return: str
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["hello", "heabc", "hell"]) == "he"
