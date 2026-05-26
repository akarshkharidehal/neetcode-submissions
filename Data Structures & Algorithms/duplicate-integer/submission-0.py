class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in range(0,len(nums)):
          if not nums[i] in s:
             s.add(nums[i])
          else:
              return True

        return False       



