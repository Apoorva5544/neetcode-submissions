class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1
        sorted_count = sorted(count, key = count.get, reverse = True)

        return sorted_count[:k]