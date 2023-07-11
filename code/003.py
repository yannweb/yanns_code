class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None

class Solution:
    def lengthOfLongestSubstring(self,s):
        l_p = 0
        r_p = 0
        res = 0
        has = set()
        while r_p < len(s):
            if s[r_p] not in has:
                has.add(s[r_p])
                r_p +=1
                if res <= len(has): # no s
                    res = len(has)
            else:
                has.remove(s[l_p])
                l_p += 1
        return res

                



def number_of_linked_list( node: ListNode):

    number_string = ''
    cur = node
    while cur:
        number_string += str(cur.val)
        cur = cur.next

    return number_string[::-1]   # 把链表解析出来，原本是对象

# from collections import namedtuple
# TestEntry = namedtuple('TestEntry','array target')

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io

    test_string= ["aab", "pwwkew", "", "au"]
    # expected answer:
    '''
    2, 3, 0, 2
    '''

    def readlines():
        #for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
        for line in test_string:
            #yield line.strip('\n')
            yield line

    lines = readlines()
    while True:
        try:
            line = next(lines)
            #s = stringToString(line);
            s = line
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break
assert Solution().lengthOfLongestSubstring("pwwkew") == 3

if __name__ == '__main__':
    main()


