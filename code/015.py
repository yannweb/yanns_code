class Solution:
    def threeSum( self, nums ) :
        length = len(nums)
        nums.sort()
        triplet_answer = list()

        for i in range(0, length - 2 ):
            if i > 0 and ( nums[i-1] == nums[i] ):
                pass
                continue
            
            j , k = i + 1, length -1

            while j < k :
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    triplet_answer.append( [ nums[i], nums[j], nums[k] ] )

                    j += 1
                    k -= 1

                    while j < k and ( nums[j] == nums[j-1] ):
                        j += 1

                    while j < k and ( nums[k] == nums[k+1] ):
                        k -= 1

                elif three_sum < 0:
                    j += 1

                else:
                    k -= 1

        return triplet_answer

# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))    
assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]    
