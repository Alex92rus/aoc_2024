import re

# BFS maze - left, right. up, down, diagonals on
def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def traverse(array_maze, i, j, stack):
    pass


def count_number_xmas(location_list: list):
    count_xmas = 0
    array_maze = []
    for line in location_list:
        array_maze.append([x for x in line])
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            if array_maze[i][j] == 'X':
                candidate = array_maze[i][j] + array_maze[i][j - 1] + array_maze[i][j - 2] + array_maze[i][j - 3] # left
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i][j + 1] + array_maze[i][j + 2] + array_maze[i][j + 3] # right
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i - 1][j] + array_maze[i - 2][j] + array_maze[i - 3][j] # up
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i + 1][j] + array_maze[i + 2][j] + array_maze[i + 3][j] # down
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i - 1][j - 1] + array_maze[i - 2][j - 2] + array_maze[i - 3][j - 3] # north west
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i - 1][j + 1] + array_maze[i - 2][j + 2] + array_maze[i - 3][j + 3] # north east
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i + 1][j + 1] + array_maze[i + 2][j + 2] + array_maze[i + 3][j + 3] # south east
                if candidate == 'XMAS':
                    count_xmas += 1
                candidate = array_maze[i][j] + array_maze[i + 1][j - 1] + array_maze[i + 2][j - 2] + array_maze[i + 3][j - 3] # south west
                if candidate == 'XMAS':
                    count_xmas += 1
    return count_xmas


def count_cross_mas(location_list: list):
    count_xmas = 0
    array_maze = []
    for line in location_list:
        array_maze.append([x for x in line])
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            if array_maze[i][j] == 'A':
                front_diagonal = array_maze[i + 1][j - 1] + array_maze[i][j] + array_maze[i - 1][j + 1]  # left
                back_diagonal = array_maze[i - 1][j - 1] + array_maze[i][j] + array_maze[i + 1][j + 1]  # left
                if (front_diagonal == 'MAS' or front_diagonal == 'SAM') and (back_diagonal == 'MAS' or back_diagonal == 'SAM'):
                    count_xmas += 1
    return count_xmas


if __name__ == '__main__':
    location_list = read_file('input.txt')
    xmas_count = count_number_xmas(location_list)
    print(f"required number of XMAS: {xmas_count}")
    test_location_list = read_file('test_input.txt')
    xmas_count = count_number_xmas(test_location_list)
    print(f"required number of XMAS on test: {xmas_count}")
    cross_mas_count = count_cross_mas(location_list)
    print(f"required number of cross MAS: {cross_mas_count}")
    test_location_list_pt2 = read_file('test_input_part2.txt')
    cross_mas_count = count_cross_mas(test_location_list_pt2)
    print(f"test required number of cross MAS: {cross_mas_count}")
