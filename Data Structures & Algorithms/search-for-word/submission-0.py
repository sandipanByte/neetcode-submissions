class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            # Word completely matched
            if i == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Wrong character
            if board[r][c] != word[i]:
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Search up, down, left, right
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Undo the change (backtracking)
            board[r][c] = temp

            return found

        # Try every cell as the starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
