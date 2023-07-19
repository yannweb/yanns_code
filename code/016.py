class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        three_sum_closet_solution = None
        for i in range( len(nums)-2 ):
            
            if i > 0 and nums[i] == nums[i-1]:
                pass 
                continue
            
            j, k = i+1, len(nums)-1

            while j < k :
                three_sum = nums[i] + nums[j] + nums[k]
                diff = three_sum - target         

                if three_sum_closet_solution == None:
                    three_sum_closet_solution = three_sum
                else:
                    prev_diff = three_sum_closet_solution - target
                    if abs(diff) < abs(prev_diff):
                        three_sum_closet_solution = three_sum

                if( diff == 0 ):
                    three_sum_closet_solution = three_sum
                    return three_sum_closet_solution
                elif diff > 0:
                    k -= 1
                else:
                    j += 1

        return three_sum_closet_solution
    
# print(Solution().threeSumClosest([-1, 2, 1, -4],-1))    
assert (Solution().threeSumClosest([-1, 2, 1, -4],-1)) == -1   
