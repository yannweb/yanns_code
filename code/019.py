class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        cur, prev_of_removal = dummy_head, dummy_head
        
        while cur.next != None:
            if n <= 0:
                prev_of_removal = prev_of_removal.next
            cur = cur.next
            n -=1
        
        n_th_node = prev_of_removal.next
        prev_of_removal.next = n_th_node.next
        
        del n_th_node
        
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
    head_of_test_1 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_1 = Solution().removeNthFromEnd( head_of_test_1, 1 )
    linked_list_print( head_of_test_1 )

    head_of_test_2 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_2 = Solution().removeNthFromEnd( head_of_test_2, 2 )
    linked_list_print( head_of_test_2 )

    head_of_test_3 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_3 = Solution().removeNthFromEnd( head_of_test_3, 3 )
    linked_list_print( head_of_test_3 )

    head_of_test_4 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_4 = Solution().removeNthFromEnd( head_of_test_4, 4 )
    linked_list_print( head_of_test_4 )

    head_of_test_5 = linked_list_factory( [1,2,3,4,5] )
    head_of_test_5 = Solution().removeNthFromEnd( head_of_test_5, 5 )
    linked_list_print( head_of_test_5 )


if __name__ == '__main__':
    test_bench()
