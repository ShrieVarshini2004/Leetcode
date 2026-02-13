class Solution:
    def kLengthApart(self, nums, k):
        zeroCount = k

        for num in nums:
            if num == 1:
                if zeroCount < k:
                    return False
                zeroCount = 0
            else:
                zeroCount += 1

        return True