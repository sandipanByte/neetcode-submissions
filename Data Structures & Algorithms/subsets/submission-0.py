class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            # Add a copy of the current subset
            result.append(current.copy())

            for i in range(index, len(nums)):
                # Choose
                current.append(nums[i])

                # Explore
                backtrack(i + 1, current)

                # Undo choice
                current.pop()

        backtrack(0, [])

        return result
        