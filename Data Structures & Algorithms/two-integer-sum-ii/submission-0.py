class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_diff = {}
        index = 1

        while index <= len(numbers):
            diff = target - numbers[index - 1]

            if numbers[index - 1] in hash_diff and numbers[index - 1] != hash_diff:
                return [hash_diff[numbers[index - 1]], index]

            else:
                hash_diff[diff] = index

            index += 1
        
        