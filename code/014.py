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



    def longestCommonPrefix3(self, strs) -> str:
        if len(strs) == 0:
            return "" 
        
        res = ""
        for j in range(len(strs[0])):
            c = strs[0][j]
            for i in range(1,len(strs)):
                if (j >=len(strs[i]) or strs[i][j] != c):
                    return res
            res = res + c
        return res


    
    def longestCommonprefix2(self, strs) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return "" 
        
        res = strs[0]

        for i in range(1,len(strs)):
            while not strs[i].startswith(res):
                res = res[0:len(res)-1]
        return res


    
assert Solution().longestCommonPrefix3(["flower", "flow", "flight"]) == "fl"
assert Solution().longestCommonprefix2(["flower", "flow", "flight"]) == "fl"


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["hello", "heabc", "hell"]) == "he"
