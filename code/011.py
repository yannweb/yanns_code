from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)
        left,right = 0,size -1
        maxwidth =size -1
        area = 0
        for width in range(maxwidth,0,-1):
            if height[left] < height[right]:
                area = max(area,width*height[left])
                left +=1
            else:
                area = max(area,width*height[right])
                right -=1
        return area
    
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([4,3,2,1,4]) == 16
