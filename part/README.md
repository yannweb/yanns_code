[TOC]



#### array_list

1. 列表写入字典
2. 左右指针

  

array/

[array_in_dict](part/array/array_in_dict)



左右指针

~~python
        l_p = 0
        r_p = 0  # 其实都在0点，也可以视为快慢指针
        # res = 0
        # has = set()
        while r_p < len(s):
            if s[r_p] not in has:
                has.add(s[r_p])
                r_p +=1
                # if res <= len(has): # no s
                #     res = len(has)
            else:
                has.remove(s[l_p])
                l_p += 1
        return res
~~

一般处理无重复问题，右指针吃入，左指针弹出



#### dict

1. 列表写入字典处理
2. 获取字典的值并判断



比起直接取值，还可以处理空值的情况

~~python
        num_idx_dict = dict()
        for i,v in enumerate(nums):
            dual = target - v
            index_of_dual = num_idx_dict.get(dual,None)
            if index_of_dual is not None and index_of_dual != i:  # dict 02
                xx
                break
            else:
                num_idx_dict[v] = i  # 取到则返回，没有则添加 # dict 01
~~





#### ListNode

node_init

node_next



#### math

1. 返回除余
2. 负数处理
3. 构造奇数列或偶数列



~~python
divmod(3+4, 2)
(3, 1)
~~



2 数字转字符处理时，负数的处理方法，加标记，加处理逻辑

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



3 切奇数列，偶数列

~~python
        maxLen = 1
        for i in range(1,n):
            odd = s[i-maxLen-1:i+1]
            even = s[i-maxLen:i+1]
            if i-maxLen-1 >= 0 and odd == odd[::-1]:
                start = i - maxLen -1
                maxLen += 2   # 思路很重要，先符合再尝试扩展
            if i-maxLen >= 0 and even == even[::-1]:
                start = i-maxLen
                maxLen +=1
       return s[start:start+maxLen]         
~~

遍历的同时，**切片**符合的奇/偶数列，只看and签名部分就好

定位的方法，符合的起点+符合的长度



#### str





#### str

1. 整数生成列表
2.  整数边界



~~python
n = 7
print(",".join(list(map(str,range(n)))))
# 0,1,2,3,4,5,6  #可以return 返回
~~



~~python
print(-0xfffffffF//2)  # 8F，负值极限
print(0xffffffFF//2) # 正值极限 2147483647
~~


