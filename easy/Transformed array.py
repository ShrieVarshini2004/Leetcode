class Solution(object):
    def constructTransformedArray(self, nums):
        n=len(nums)
        result=[0]*n
        for i in range(n):
            if nums[i]==0:
                result[i]=0
            else:
                new_idx=(i+nums[i])%n
                result[i]=nums[new_idx]
        return result