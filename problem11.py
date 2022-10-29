def get_input(filename):
    input_data = []
    with open(filename, "r") as file:
        for data in file:
            data = list(map(int, data.strip().split()))
            input_data.append(data)
    return input_data


def greatest_adjacent(grid):
    grid_size = len(grid)
    max_multi = 0
    for starter_row in range(grid_size):
        for column in range(grid_size):
            down_multi = 1
            diagonal_right_multi = 1
            diagonal_left_multi = 1
            right_multi = 1
            for depth in range(4):
                if starter_row <= grid_size - 4:
                    down_multi *= grid[starter_row + depth][column]
                if column <= grid_size - 4:
                    right_multi *= grid[starter_row][column + depth]
                if column <= grid_size - 4 and starter_row <= grid_size - 4:
                    diagonal_right_multi *= grid[starter_row + depth][column + depth]
                if starter_row <= grid_size - 4 and column >= 3:
                    diagonal_left_multi *= grid[starter_row + depth][column - depth]
            max_multi = max(max_multi, down_multi, diagonal_right_multi, diagonal_left_multi, right_multi)
    return max_multi


data_grid = get_input("inputs/problem11.txt")
print(greatest_adjacent(data_grid))
