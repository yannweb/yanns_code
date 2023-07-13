class Solution:
    def reverse(self, x:int)->int:
        str_int = str(x)
        is_negative = False
        if str_int[0] == '-':
            str_int=str_int[::-1]
            is_negative=True
        str_int_reversed = str_int[::-1]
        int_reversed = int(str_int_reversed)
        if is_negative:
            int_reversed = -1* int_reversed
        if int_reversed > 2147483648 -1 or int_reversed < -2147483648:
            return 0
        return int_reversed

    def reverse1(self, x:int)->int:
        res = 0
        while x !=0:
            res = res * 10 + x % 10
            x //=10
        if res > 0xffffffFF//2 or res < -0xffffffFF//2 :
            return 0
        return res
            
                 
assert Solution().reverse1(2147483646) == 0


from collections import namedtuple
TestEntry = namedtuple('TestEntry', 'array target')
def test_bench():
    test_integers = [123, -123, 120, 2**31]

    for x in test_integers:
        ret_value = Solution().reverse(x)
        print(ret_value)

    return
if __name__ == '__main__':
    test_bench()
