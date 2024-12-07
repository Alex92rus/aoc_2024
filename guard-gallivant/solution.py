from collections import defaultdict
import platform
import os
from time import sleep


def clear_screen():
    # sleep(4)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


direction_guide = {
    '>': lambda i, j: (i, j + 1),
    '<': lambda i, j: (i, j - 1),
    '^': lambda i, j: (i - 1, j),
    'V': lambda i, j: (i + 1, j)
}

turn_right = {
    '>': 'V',
    '<': '^',
    '^': '>',
    'V': '<'
}


def locate_guard(array_maze: list) -> tuple:
    for i, level in enumerate(array_maze):
        for j in range(len(level)):
            if level[j] in ['>', '<', '^', 'V']:
                return i, j
    return -1, -1


def print_maze(array_maze):
    clear_screen()
    colors = [31, 32, 33, 34, 35, 36]  # Red, Green, Yellow, Blue, Magenta, Cyan
    for i, line_row in enumerate(array_maze):
        for j, charact in enumerate(line_row):
            if charact in direction_guide.keys():
                print(f"\033[{colors[1]}m{charact}\033[0m", end='')
            else:
                print(charact, end='')
        print()


def dungeon_obstacle_setter_mapper(dungeon_map: list):
    obstacle_locations_count = 0
    array_maze = []
    beginning_position = []
    for line in dungeon_map:
        array_maze.append([x for x in line if x != '\n'])
        beginning_position.append([x for x in line if x != '\n'])
    for obstacle_row in range(len(array_maze)):
        for obstacle_column in range(len(array_maze[obstacle_row])):
            if array_maze[obstacle_row][obstacle_column] == '.':
                current_row, current_column = locate_guard(array_maze)
                guard_positions = defaultdict(set)
                array_maze[obstacle_row][obstacle_column] = '#'
                while -1 < current_row < len(array_maze) and - 1 < current_column < len(array_maze[0]):
                    if array_maze[current_row][current_column] in guard_positions[(current_row, current_column)]:
                        obstacle_locations_count += 1
                        break
                    else:
                        guard_positions[(current_row, current_column)].add(array_maze[current_row][current_column])
                    (new_row, new_column) = direction_guide[array_maze[current_row][current_column]](current_row, current_column)
                    if -1 < new_row < len(array_maze) and - 1 < new_column < len(array_maze[0]):
                        if array_maze[new_row][new_column] == '#':
                            array_maze[current_row][current_column] = turn_right[array_maze[current_row][current_column]]
                        else:
                            array_maze[new_row][new_column] = array_maze[current_row][current_column]
                            array_maze[current_row][current_column] = 'X'
                            current_row, current_column = new_row, new_column
                    else:
                        array_maze[current_row][current_column] = 'X'
                        current_row, current_column = new_row, new_column
                reset_puzzle(array_maze, beginning_position)
    return obstacle_locations_count


def reset_puzzle(array_maze, beginning_position):
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            array_maze[i][j] = beginning_position[i][j]


def dungeon_mapper(map: list):
    visited_locations_count = 0
    array_maze = []
    for line in map:
        array_maze.append([x for x in line if x != '\n'])
    current_row, current_column = locate_guard(array_maze)
    while -1 < current_row < len(array_maze) and - 1 < current_column < len(array_maze[0]):
        (new_row, new_column) = direction_guide[array_maze[current_row][current_column]](current_row, current_column)
        if -1 < new_row < len(array_maze) and - 1 < new_column < len(array_maze[0]):
            if array_maze[new_row][new_column] == '#':
                array_maze[current_row][current_column] = turn_right[array_maze[current_row][current_column]]
            else:
                if array_maze[new_row][new_column] != 'X':
                    visited_locations_count += 1
                array_maze[new_row][new_column] = array_maze[current_row][current_column]
                array_maze[current_row][current_column] = 'X'
                current_row, current_column = new_row, new_column
        else:
            if array_maze[current_row][current_row] != 'X':
                visited_locations_count += 1
            array_maze[current_row][current_column] = 'X'
            current_row, current_column = new_row, new_column
    # print_maze(array_maze)
    return visited_locations_count


if __name__ == '__main__':
    test_location_list = read_file('test_input.txt')
    location_list = read_file('input.txt')
    locations_visited = dungeon_mapper(test_location_list)
    print(f"test input: locations the guard will ever visit: {locations_visited}")
    locations_visited = dungeon_mapper(location_list)
    print(f"assessment input: locations the guard will ever visit: {locations_visited}")
    obstacles_looping_guard = dungeon_obstacle_setter_mapper(test_location_list)
    print(f"test input: number of locations for obstacles such that guard will be in a loop: {obstacles_looping_guard}")
    obstacles_looping_guard = dungeon_obstacle_setter_mapper(location_list)
    print(f"assessment input: number of locations for obstacles such that guard will be in a loop: {obstacles_looping_guard}")
