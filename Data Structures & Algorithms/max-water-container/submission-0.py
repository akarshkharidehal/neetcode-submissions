class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # vertical = min(heights[l],heights[r])
        # horizontal=r-l
        # to get max amount of water we should get max area from vertical and horizontal
        # area = vertical * horizontal
        # Compare the heights and decrement/increment l,r
          l = 0
          r = len(heights)-1
          max_water=0
          while l<r:
            vertical = min(heights[l],heights[r])
            horizontal=r-l
            area = vertical * horizontal
            max_water=max(max_water,area)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
          return max_water 
          
          
        
                 

        