class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        k = len(nums)-1
        result = [0]*len(nums)
        while(i<=j):
            if(abs(nums[i]) > abs(nums[j])):
                result[k] = nums[i]*nums[i]
                i = i+1
            else:
                result[k] = nums[j]*nums[j]
                j = j-1
            k = k-1
        return result 
