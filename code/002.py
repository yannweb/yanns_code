class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy_head = ListNode('@') # ？
        iterator = dummy_head

        carry_in = 0

        while l1 or l2:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            carry_in, digit_sum = divmod(val_1+val_2 + carry_in,10)

            iterator.next = ListNode(digit_sum)
            iterator = iterator.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry_in:
            iterator.next = ListNode(carry_in)
        return dummy_head.next

def number_of_linked_list( node: ListNode):

    number_string = ''
    cur = node
    while cur:
        number_string += str(cur.val)
        cur = cur.next

    return number_string[::-1]   # 把链表解析出来，原本是对象

# from collections import namedtuple
# TestEntry = namedtuple('TestEntry','array target')

def test_bench():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    head_of_sum = Solution().addTwoNumbers(l1=l1,l2=l2)
    print( number_of_linked_list(head_of_sum))


if __name__ == "__main__":
    test_bench()

