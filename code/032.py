class Solution(object):
    
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        
        for cur_idx, char in enumerate(s):
            if char == '(':
                stack.append( cur_idx )              
            else:
                stack.pop()
                if not stack:
                    stack.append( cur_idx )
                else:
                    max_length = max(max_length, cur_idx - stack[-1])
        return max_length


assert Solution().longestValidParentheses(")()())") == 4
assert Solution().longestValidParentheses("(()") == 2
