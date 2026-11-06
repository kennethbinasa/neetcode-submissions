class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        num_set = set(nums)
        for num in num_set:
            count = 0
            if (num - 1) not in num_set:
                index = 0

                while index < len(num_set):
                    if num + index in num_set:
                        count += 1

                    else:
                        break

                    index += 1

            if count > ans:
                ans = count

        return ans