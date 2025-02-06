import random

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "X" for num in row))
    print()

def find_empty_cell(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_solved(grid):
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(3):
        for j in range(3):
            if grid[i][j] != target[i][j]:
                return False
    return True

def move_up(grid, empty_cell):
    i, j = empty_cell
    if i > 0:
        grid[i][j], grid[i-1][j] = grid[i-1][j], grid[i][j]
        return (i-1, j)
    return empty_cell

def move_down(grid, empty_cell):
    i, j = empty_cell
    if i < 2:
        grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
        return (i+1, j)
    return empty_cell

def move_left(grid, empty_cell):
    i, j = empty_cell
    if j > 0:
        grid[i][j], grid[i][j-1] = grid[i][j-1], grid[i][j]
        return (i, j-1)
    return empty_cell

def move_right(grid, empty_cell):
    i, j = empty_cell
    if j < 2:
        grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
        return (i, j+1)
    return empty_cell

def shuffle_grid(grid):
    moves = [move_up, move_down, move_left, move_right]
    for _ in range(100):  # Number of random moves to shuffle the grid
        empty_cell = find_empty_cell(grid)
        move = random.choice(moves)
        empty_cell = move(grid, empty_cell)

def is_solvable(grid):
    inversions = 0
    numbers = [num for row in grid for num in row if num != 0]
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                inversions += 1
                
    empty_cell_row = find_empty_cell(grid)[0]
    total_rows = 3
    
    # Adjusting for the position of the empty cell
    if empty_cell_row % 2 == 0:
        inversions += 1
    
    return inversions % 2 == 0

def main():
    target_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    current_grid = [row[:] for row in target_grid]
    
    while not is_solvable(current_grid):
        shuffle_grid(current_grid)
    
    empty_cell = find_empty_cell(current_grid)
    moves = {
        'w': move_up,
        's': move_down,
        'a': move_left,
        'd': move_right
    }

    while not is_solved(current_grid):
        print_grid(current_grid)
        print("Enter w/a/s/d to move the empty cell, q to quit:")
        action = input().strip().lower()

        if action == 'q':
            break

        if action in moves:
            empty_cell = moves[action](current_grid, empty_cell)

    if action != 'q':
        print_grid(current_grid)
        print("Congratulations! You solved the puzzle!")

if __name__ == "__main__":
    main()