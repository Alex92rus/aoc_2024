from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines

def determine_collinearity(city_map: list):
    array_maze = []
    anti_node_maze = []
    anti_node_count = 0
    for line in city_map:
        array_maze.append([x for x in line if x != '\n'])
        anti_node_maze.append(['.' for x in line if x != '\n'])
    antenna_locations = defaultdict(set)
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            if array_maze[i][j] != '.':
                for antenna_with_same_freq in antenna_locations[array_maze[i][j]]:  # array_maze[i][j] will have the greatest i from the group so far
                    diff_row = i - antenna_with_same_freq[0]  # >= 0
                    diff_col = antenna_with_same_freq[1] - j
                    node_up_i = antenna_with_same_freq[0] - diff_row
                    node_up_j = antenna_with_same_freq[1] + diff_col
                    node_down_i = i + diff_row
                    node_down_j = j - diff_col
                    if 0 <= node_up_j < len(array_maze[i]) and 0 <= node_up_i < len(array_maze):
                        if anti_node_maze[node_up_i][node_up_j] != '#':
                            anti_node_maze[node_up_i][node_up_j] = '#'
                            anti_node_count += 1
                    if 0 <= node_down_j < len(array_maze[i]) and 0 <= node_down_i < len(array_maze):
                        if anti_node_maze[node_down_i][node_down_j] != '#':
                            anti_node_maze[node_down_i][node_down_j] = '#'
                            anti_node_count += 1
                antenna_locations[array_maze[i][j]].add((i, j))
    for i, line_row in enumerate(anti_node_maze):
        for j, charact in enumerate(line_row):
            print(charact, end='')
        print()
    return anti_node_count


def determine_collinearity_all_points(city_map: list):
    array_maze = []
    anti_node_maze = []
    anti_node_count = 0
    for line in city_map:
        array_maze.append([x for x in line if x != '\n'])
        anti_node_maze.append(['.' for x in line if x != '\n'])
    antenna_locations = defaultdict(set)
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            if array_maze[i][j] != '.':
                for antenna_with_same_freq in antenna_locations[array_maze[i][j]]:  # array_maze[i][j] will have the greatest i from the group so far
                    diff_row = i - antenna_with_same_freq[0]  # >= 0
                    diff_col = antenna_with_same_freq[1] - j
                    node_up_i = antenna_with_same_freq[0] - diff_row
                    node_up_j = antenna_with_same_freq[1] + diff_col
                    node_down_i = antenna_with_same_freq[0] + diff_row
                    node_down_j = antenna_with_same_freq[1] - diff_col
                    if anti_node_maze[antenna_with_same_freq[0]][antenna_with_same_freq[1]] != '#':
                        anti_node_maze[antenna_with_same_freq[0]][antenna_with_same_freq[1]] = '#'
                        anti_node_count += 1
                    while 0 <= node_up_j < len(array_maze[i]) and 0 <= node_up_i < len(array_maze):
                        if anti_node_maze[node_up_i][node_up_j] != '#':
                            anti_node_maze[node_up_i][node_up_j] = '#'
                            anti_node_count += 1
                        node_up_i -= diff_row
                        node_up_j += diff_col
                    while 0 <= node_down_j < len(array_maze[i]) and 0 <= node_down_i < len(array_maze):
                        if anti_node_maze[node_down_i][node_down_j] != '#':
                            anti_node_maze[node_down_i][node_down_j] = '#'
                            anti_node_count += 1
                        node_down_i += diff_row
                        node_down_j -= diff_col
                antenna_locations[array_maze[i][j]].add((i, j))
    for i, line_row in enumerate(anti_node_maze):
        for j, charact in enumerate(line_row):
            print(charact, end='')
        print()
    return anti_node_count


if __name__ == '__main__':
    test_city_map = read_file('test_input.txt')
    city_map = read_file('input.txt')
    engineered_value = determine_collinearity(test_city_map)
    print(f"test input: the number of anti-nodes is: {engineered_value}")
    engineered_value = determine_collinearity(city_map)
    print(f"assessment input: Sum of target values of equations: {engineered_value}")
    number_of_antinodes = determine_collinearity_all_points(test_city_map)
    print(f"test input: the number of anti-nodes is: {number_of_antinodes}")
    number_of_antinodes = determine_collinearity_all_points(city_map)
    print(f"assessment input: Sum of target values of equations: {number_of_antinodes}")
