# class Listnode(object):
    
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
from _listnode import Listnode
from _listnode import linked_list_factory
from _listnode import linked_list_point

class Solution(object):
    
    def mergeKList(self,lists):
        node = []
        for k in lists:
            while k:
                # print(k.val)
                node.append(k.val)
                k = k.next
        point = result = Listnode(0)        
        for node in sorted(node):
            point.next = Listnode(node)
            point = point.next
        return result.next

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

    head_of_solution = Solution().mergeKList([head_1,head_2,head_3])
    linked_list_point(head_of_solution)

if __name__ == "__main__":
    test_bench()
