class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_diff = {}
        index = 0

        while index < len(nums):
            difference = target - nums[index] # diff = 7 - 3

            if difference in map_diff:
                return [map_diff[difference], index]

            else:
                map_diff[nums[index]] = index
                
            index += 1