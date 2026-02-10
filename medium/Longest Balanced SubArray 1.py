class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for start in range(n):
            odd=set()
            even=set()
            for end in range(start, n):
                if nums[end]%2==0:
                    even.add(nums[end])
                else:
                    odd.add(nums[end])
                if len(odd)==len(even):
                    ans=max(ans, end-start+1)
        return ans