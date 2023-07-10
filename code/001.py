class Solution(object):
    def twoSum(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for i, num in enumerate(nums):
            j = hash_map.get(target - num)
            if j is not None and i != j:
                    return [i,j]

    def twoSum1(self,nums,target):
        num_idx_dict = dict()
        solution = []
        for i,v in enumerate(nums):
            dual = target - v
            #dict 01
            index_of_dual = num_idx_dict.get(dual,None)
            if index_of_dual is not None and index_of_dual != i:
                solution = [i,index_of_dual]
                break
            else:
                num_idx_dict[v] = i  # 取到则返回，没有则添加
        return solution

if __name__ == '__main__':
    print(Solution().twoSum([2, 17, 7, 15], 9));
