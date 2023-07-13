```python
        temp = ListNode(-1)      # 哨兵
        head = temp							 # 复制头
        while l1 and l2 :         # 都存在
            if l1.val > l2.val:
                temp.next = l2		# 定义第三方指向
                l2 = l2.next			# 移动处理值
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next		# 第三方移动
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return head.next				# 哨兵带出真头

```
