class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        left = 0
        longest_valid_window = 0

        for right in range(n):
            # Shrink window if condition is violated
            while left < right and nums[left] * k < nums[right]:
                left += 1

            window_size = right - left + 1
            longest_valid_window = max(longest_valid_window, window_size)

        return n - longest_valid_window