class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1
        
        sorted_dict = sorted(freq.items(), key = lambda x:x[1], reverse=True)

        result = []
        for num,count in sorted_dict[:k]:
            result.append(num)

        return result