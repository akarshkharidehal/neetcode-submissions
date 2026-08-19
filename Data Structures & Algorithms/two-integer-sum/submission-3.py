class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = sorted([(v, i) for i, v in enumerate(nums)])
        l = 0
        r = len(nums)-1  
        while (l<r):   
            l_value, l_index = index_nums[l]
            r_value, r_index = index_nums[r]

            current_sum = l_value + r_value 
            if current_sum == target:
                return sorted([l_index, r_index])
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return []