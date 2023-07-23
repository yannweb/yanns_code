# class Listnode(object):
    
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
import sys
sys.path.append("..")
from _listnode import Listnode
from _listnode import linked_list_factory
from _listnode import linked_list_point

class Solution(object):
    
    def SwapPairs(self,head:Listnode) -> Listnode:
        if head is None or head.next is None:
            return head
        
        dummy_head = Listnode(0)
        previous = dummy_head

        while head and head.next:
            original_second = head.next
            head.next = original_second.next
            original_second.next = head
            previous.next=original_second
            previous = head
            head = head.next
        return dummy_head.next  

# def linked_list_factory(elements):
#     last_node = None
#     for element in reversed(elements):
#         cur_node = Listnode(element)
#         cur_node.next = last_node
#         last_node = cur_node
#     return last_node

# def linked_list_point(head:Listnode):
#     cur = head
#     while cur:
#         print(cur.val, end='->')
#         cur = cur.next
#     print('None\n')

def test_bench():
    head_1=linked_list_factory([1,2,3,4])
    head_2=linked_list_factory([1,3,4])
    head_3=linked_list_factory([5,6])

    head_of_solution = Solution().SwapPairs(head_1)
    linked_list_point(head_of_solution)

if __name__ == "__main__":
    test_bench()
