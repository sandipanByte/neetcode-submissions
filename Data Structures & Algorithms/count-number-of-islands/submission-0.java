class Solution {

    public void dfs(char[][] grid, int r, int c) {

        int rows = grid.length;
        int cols = grid[0].length;

        // Out of bounds or water
        if (r < 0 || r >= rows || c < 0 || c >= cols) {
            return;
        }

        if (grid[r][c] == '0') {
            return;
        }

        // Mark as visited
        grid[r][c] = '0';

        // Visit 4 directions
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }

    public int numIslands(char[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        int count = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {

                if (grid[r][c] == '1') {
                    count++;

                    dfs(grid, r, c);
                }
            }
        }

        return count;
    }
}
