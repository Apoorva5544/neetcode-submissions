class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def backtracking(i):
            if i == len(nums):
                result.append(subset[:])
                return
            
            subset.append(nums[i])
            backtracking(i+1)

            subset.pop()
            backtracking(i+1)

        backtracking(0)
        return result 