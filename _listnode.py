class Listnode(object):
    
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next



def linked_list_factory(elements):
    last_node = None
    for element in reversed(elements):
        cur_node = Listnode(element)
        cur_node.next = last_node
        last_node = cur_node
    return last_node

def linked_list_point(head:Listnode):
    cur = head
    while cur:
        print(cur.val, end='->')
        cur = cur.next
    print('None\n')
