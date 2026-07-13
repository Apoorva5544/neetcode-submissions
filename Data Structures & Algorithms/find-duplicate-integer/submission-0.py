class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeat = set()
        for n in nums:
            if n in repeat:
                return n
            repeat.add(n)
        return -1