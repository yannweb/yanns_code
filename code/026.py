# class Listnode(object):
    
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next
from _listnode import Listnode
from _listnode import linked_list_factory
from _listnode import linked_list_point

class Solution(object):
    
    def removeDuplicates(self,nums) -> int:
        if len(nums) == 0:
            return 0
        
        index_of_ordered = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[index_of_ordered]:
                index_of_ordered += 1
                nums[index_of_ordered] = nums[j]
        new_length = index_of_ordered + 1
        return new_length

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
assert Solution().removeDuplicates([1,1,2]) == 2
assert (Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])) ==5

