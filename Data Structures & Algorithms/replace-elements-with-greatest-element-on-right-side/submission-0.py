class Solution:
    def replaceElements(self, a):
        max_right = -1

        for i in range(len(a) - 1, -1, -1):
            current = a[i]
            a[i] = max_right
            max_right = max(max_right, current)

        return a
