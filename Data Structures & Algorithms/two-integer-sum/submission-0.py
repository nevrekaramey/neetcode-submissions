class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in num_hash:
                return [num_hash[temp], i]
            num_hash[n] = i

        return []