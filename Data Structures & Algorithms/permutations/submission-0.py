class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False]*len(nums)

        def backtrack(curr):
            if(len(curr)==len(nums)):
                ans.append(curr[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue 
                
                visited[i]=True
                curr.append(nums[i])

                backtrack(curr)
                curr.pop()
                visited[i] = False
                
        backtrack([])
        return ans