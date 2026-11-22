class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_map = {}

        for n in nums:
            if n not in counter_map:
                counter_map[n] = 1
            else:
                counter_map[n] += 1
        

        sorted_nums = dict(sorted(counter_map.items(), key=lambda item: item[1], reverse=True))

        result = []
        for key, value in list(sorted_nums.items())[:k]:
            result.append(key)

        return result

