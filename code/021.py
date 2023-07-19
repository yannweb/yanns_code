class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy_head = ListNode(-1)
        cur = dummy_head
        
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        while l2:
            cur.next = l2
            l2, cur = l2.next, cur.next
        
        while l1:
            cur.next = l1
            l1, cur = l1.next, cur.next
        
        return dummy_head.next


def linked_list_factory( elements ):
    last_node = None
    for element in reversed( elements ):
        cur_node = ListNode( element )
        cur_node.next = last_node
        last_node = cur_node

    return last_node

def linked_list_print( head: ListNode ):
    cur = head
    while cur:
        print( cur.val, end = '->' )
        cur = cur.next

    print('None\n')

def test_bench():

    head_1 = linked_list_factory( [1,2,4] )
    head_2 = linked_list_factory( [1,3,4] )
    head_of_solution = Solution().mergeTwoLists( head_1, head_2 )

    linked_list_print( head_of_solution )

if __name__ == "__main__":

    test_bench()
