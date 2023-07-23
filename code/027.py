# class Listnode(object):
    
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
from _listnode import Listnode
from _listnode import linked_list_factory
from _listnode import linked_list_point

class Solution(object):
    
    def removeElement(self,nums, val):
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res +=1
        return res

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
    head_1=linked_list_factory([0,0,1,1,1,2,2,3,3,4])
    head_2=linked_list_factory([1,3,4])
    head_3=linked_list_factory([5,6])

    # head_of_solution = Solution().removeDuplicates(head_1)
    # linked_list_point(head_of_solution)
assert Solution().removeElement([3,2,2,3],3) == 2
assert (Solution().removeElement([0,1,2,2,3,0,4,2],2)) ==5

