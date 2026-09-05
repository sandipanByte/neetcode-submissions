class Solution:
    def topKFrequent(self, nums, k):
        freq = {}

        # Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Sort by frequency
        sorted_nums = sorted(freq, key=freq.get, reverse=True)

        # Return first k elements
        return sorted_nums[:k]

        