[TOC]

#### 定义结构

```python
class ListNode:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None

#if __name__ == '__main__':
#    assert Solution().mergeTwoLists(ListNode(1), ListNode(2)).val == 1

```



#### 使用

```python
class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy_head = ListNode('@') # ？
        iterator = dummy_head
```



#### 解析对象

```python
def number_of_linked_list( node: ListNode):

    number_string = ''
    cur = node
    while cur:
        number_string += str(cur.val)
        cur = cur.next

    return number_string[::-1]   # 把链表解析出来，原本是对象
```



#### 构造用例

```python
def test_bench():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    head_of_sum = Solution().addTwoNumbers(l1=l1,l2=l2)
    print( number_of_linked_list(head_of_sum))
```
