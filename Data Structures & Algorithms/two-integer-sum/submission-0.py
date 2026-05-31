class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i in range(0,len(nums)):
            diff = target - nums[i]

            if diff in res:
                return [res[diff],i]
            else:
                res[nums[i]] = i
              