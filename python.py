import random
import time

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

def main():
    target_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    current_grid = [row[:] for row in target_grid]
    shuffle_grid(current_grid)

    empty_cell = find_empty_cell(current_grid)
    moves = {
        'w': move_up,
        's': move_down,
        'a': move_left,
        'd': move_right
    }

    start_time = time.time()
    max_time = 120  # 2 minutes

    while not is_solved(current_grid) and (time.time() - start_time) < max_time:
        print_grid(current_grid)
        print(f"Enter w/a/s/d to move the empty cell, q to quit. Time left: {max_time - int(time.time() - start_time)} seconds:")
        action = input().strip().lower()

        if action == 'q':
            break

        if action in moves:
            empty_cell = moves[action](current_grid, empty_cell)

    elapsed_time = time.time() - start_time
    if action != 'q' and elapsed_time < max_time:
        print_grid(current_grid)
        print("Congratulations! You solved the puzzle!")
    elif action == 'q':
        print_grid(current_grid)
        print("Game aborted by player.")
    else:
        print_grid(current_grid)
        print(f"Time's up! Game over. Puzzle not solved in {max_time} seconds.")

if __name__ == "__main__":
    main()