class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sett = {}

        for i,num in enumerate(nums):
            rest = target-num
            if rest in sett:
                return [sett[rest],i]

            sett[num] = i