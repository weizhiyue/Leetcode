### Sol 1: DFS and BFS
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # BFS
        # DFS
        # Union-Find
        # Vertex: position where there is a value of 1.
        # Edge: adjacent position.
        count = 0
        max_area = 0
        self.direction = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                self.tmp_area = 0
                # self.dfs(grid, i, j)
                self.bfs(grid, i, j)
                # print("The area of curr island: ", self.tmp_area)
                max_area = max(max_area, self.tmp_area)
                count += 1
        # print("# of island: ", count)
        return max_area
                
        
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        self.tmp_area += 1
        for dirc in self.direction:
            row = i + dirc[0]
            col = j + dirc[1]
            if self.check_within_bound(grid, row, col) and grid[row][col] == 1:
                self.dfs(grid, row, col)
    
    
    def bfs(self, grid, i, j):
        queue = []
        queue.append((i, j))
        grid[i][j] = 0
        self.tmp_area += 1
        while len(queue) != 0:
            top = queue.pop(0)
            for dirc in self.direction:
                row = top[0] + dirc[0]
                col = top[1] + dirc[1]
                if self.check_within_bound(grid, row, col) and grid[row][col] == 1:
                    grid[row][col] = 0
                    self.tmp_area += 1
                    queue.append((row, col))
                    

                    
    def check_within_bound(self, grid, row, col):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])




### Sol 2: Union Find
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Union-Find
        # initialization: parent and sizes
        parents = collections.defaultdict()
        sizes = collections.defaultdict()
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        
        # Each vertex is the parent of itself (set containing itself)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    parents[(i, j)] = (i, j)
                    sizes[(i, j)] = 1
        
        def check_boundary(i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])
        
        def find(x):
            if x != parents[x]:
                # path compression
                parents[x] = find(parents[x])
            return parents[x]
        
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            # Not in the same set or not counted
            if root_x != root_y:
                if sizes[root_x] >= sizes[root_y]:
                    parents[root_y] = root_x
                    sizes[root_x] += sizes[root_y]
                    return sizes[root_x]
                else:
                    parents[root_x] = root_y
                    sizes[root_y] += sizes[root_x]
                    return sizes[root_y]
            # If belongs to the same set, return 0
            return 0
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Found one area
                if grid[i][j] == 1:
                    if area == 0:
                        area = 1
                    for dirct in directions:
                        row = i + dirct[0]
                        col = j + dirct[1]
                        if check_boundary(row, col) and grid[row][col] == 1:
                            union_res = union((row, col), (i, j))
                            area = max(area, union_res)

        return area
        
      
