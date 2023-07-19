from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        solution = list()
        size_of_input = len( nums )
 
        for i in range( size_of_input - 3 ):
            if i > 0 and nums[i-1] == nums[i]:
                pass
                continue

            for j in range( i+1, size_of_input - 2):
                if j > i+1 and nums[j-1] == nums[j]:
                    pass
                    continue
                
                k, m = (j+1), (size_of_input-1)

                while k < m:
                    quadruple = [ nums[i], nums[j], nums[k],nums[m] ]
                    four_sum = sum( quadruple )

                    if four_sum == target :

                        solution.append( quadruple )
                        k += 1

                        while k < m and nums[k-1] == nums[k]:
                            k += 1

                        m -= 1

                        while k < m and nums[m+1] == nums[m]:
                            m -= 1
                    
                    elif four_sum > target:
                        m -= 1

                        while k < m and nums[m+1] == nums[m]:
                            m -= 1

                    else:
                        k += 1

                        while k < m and nums[k-1] == nums[k]:
                            k += 1

        return solution
    
assert ( Solution().fourSum( [1, 0, -1, 0, -2, 2], 1))  == [[-2, 0, 1, 2], [-1, 0, 0, 2]]  
