def read_grid(filename):
    """
    Reads word search grid from file
    
    Args:
        filename (str): Path to the text file containing grid of characters
        
    Returns:
        list(str): Gird containing characters
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")

def find_xmas_part1(grid):
    """Find all occurrences of 'XMAS' in any direction."""
    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(0,1), (1,0), (1,1), (-1,1), # right, down, diag down-right, diag up-right
                 (0,-1), (-1,0), (-1,-1), (1,-1)] # left, up, diag up-left, diag down-left
    
    def check_pattern(x, y, dx, dy):
        """Check if pattern 'XMAS' exists starting at (x,y) in direction (dx,dy)."""
        pattern = 'XMAS'
        for i, char in enumerate(pattern):
            new_x, new_y = x + i * dx, y + i * dy
            if not (0 <= new_x < rows and 0 <= new_y < cols):
                return False
            if grid[new_x][new_y] != char:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_pattern(i, j, dx, dy):
                    count += 1
                    
    return count

def find_xmas_part2(grid):
    """Find X patterns formed by two 'MAS' strings."""
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0
    
    def check_x_pattern(x, y):
        """Check if X pattern exists centered at (x,y)."""
        # Check all possible combinations of MAS (forward/backward) in X pattern
        patterns = [('MAS', 'MAS'), ('MAS', 'SAM'), ('SAM', 'MAS'), ('SAM', 'SAM')]
        
        for p1, p2 in patterns:
            # Assume pattern is valid until proven otherwise
            valid = True
            
            # Check top-left to bottom-right diagonal
            for i, char in enumerate(p1):
                if not (0 <= x-1+i < rows and 0 <= y-1+i < cols):
                    valid = False
                    break
                if grid[x-1+i][y-1+i] != char:
                    valid = False
                    break
                    
            if not valid:
                continue
                
            # Check top-right to bottom-left diagonal
            for i, char in enumerate(p2):
                if not (0 <= x-1+i < rows and 0 <= y+1-i < cols):
                    valid = False
                    break
                if grid[x-1+i][y+1-i] != char:
                    valid = False
                    break
                    
            if valid:
                return True
                
        return False
    
    # Check each possible center point for an X pattern
    for i in range(1, rows-1):  # Start at 1 to ensure space for top of X
        for j in range(1, cols-1):  # Start at 1 to ensure space for left of X
            if check_x_pattern(i, j):
                total_count += 1
                
    return total_count

if __name__ == "__main__":
    try:
        grid = read_grid('input.txt')
        
        # Part 1: Find all XMAS occurrences
        xmas_count = find_xmas_part1(grid)
        print(f"Part 1 - XMAS occurrences: {xmas_count}")
        
        # Part 2: Find X patterns made of MAS
        x_pattern_count = find_xmas_part2(grid)
        print(f"Part 2 - X-MAS patterns: {x_pattern_count}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")

