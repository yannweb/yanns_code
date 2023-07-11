[TOC]



#### array_list

1. 列表写入字典

  

array/

[array_in_dict](part/array/array_in_dict)



#### dict

1. 获取字典的值
2. 反写字典



比起直接取值，还可以处理空值的情况

~~python
            index_of_dual = num_idx_dict.get(dual,None)
            if index_of_dual is not None and index_of_dual != i:
                solution = [i,index_of_dual]
             # 对比 x=   num_idx_dict[dual]
~~



~~python
        for i,v in enumerate(nums):
            #dual = target - v
            #index_of_dual = num_idx_dict.get(dual,None)
            if index_of_dual is not None and index_of_dual != i:
            #   solution = [i,index_of_dual]
            #    break
            #else:
                num_idx_dict[v] = i   # 需要返回index的时候用
~~





#### ListNode





#### math

1. 返回除余
2. 负数处理



~~python
divmod(3+4, 2)
(3, 1)
~~



数字转字符处理时，负数的处理方法，加标记，加处理逻辑

~~python
        str_int = str(x)
        is_negative = False
        if str_int[0] == '-':
            str_int=str_int[::-1]
            is_negative=True
        str_int_reversed = str_int[::-1]
        int_reversed = int(str_int_reversed)
        if is_negative:
            int_reversed = -1* int_reversed
~~





#### str



