class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}

        # Step 1: Count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        total = 0

        # Step 2 & 3: Find max frequency and sum totals
        for count in freq.values():
            if count > max_freq:
                max_freq = count
                total = count
            elif count == max_freq:
                total += count

        return total