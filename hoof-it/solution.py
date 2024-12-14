# Python program to copy a nested list
import copy


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def traverse_to_top(i, j, maze, count_trails=False):
    if 0 <= i < len(maze) and 0 <= j < len(maze[0]):
        if maze[i][j] == 9:
            if not count_trails:
                maze[i][j] = -1
            return 1
        node_sum = 0
        if i + 1 < len(maze) and maze[i + 1][j] == maze[i][j] + 1:
            node_sum += traverse_to_top(i + 1, j, maze, count_trails)
        if i - 1 >= 0 and maze[i - 1][j] == maze[i][j] + 1:
            node_sum += traverse_to_top(i - 1, j, maze, count_trails)
        if j + 1 < len(maze[i]) and maze[i][j + 1] == maze[i][j] + 1:
            node_sum += traverse_to_top(i,  j + 1, maze, count_trails)
        if j - 1 >= 0 and maze[i][j - 1] == maze[i][j] + 1:
            node_sum += traverse_to_top(i, j - 1, maze, count_trails)
        return node_sum
    return 0


def hoof_it(topology_map: list, count_trails=False):
    array_maze = []
    for line in topology_map:
        array_maze.append([int(x) for x in line if x != '\n'])

    trailhead_score = 0
    for i in range(len(array_maze)):
        for j in range(len(array_maze[i])):
            if array_maze[i][j] == 0:
                if not count_trails:
                    unmarked = copy.deepcopy(array_maze)
                else:
                    unmarked = array_maze
                trailhead_score += traverse_to_top(i, j, unmarked, count_trails=count_trails)
    return trailhead_score


if __name__ == '__main__':
    topological_map = read_file('input.txt')
    trail_score = hoof_it(topological_map)
    print(f"required trailhead_score on topo map: {trail_score}")
    test_topological_map = read_file('test_input.txt')
    # trail_score = hoof_it(test_topological_map)
    # print(f"test input: required trailhead_score on topo map: {trail_score}")
    trail_score = hoof_it(topological_map, count_trails=True)
    print(f"The number of different hiking trails is: {trail_score}")
    trail_score = hoof_it(test_topological_map, count_trails=True)
    print(f"test input: The number of different hiking trails is: {trail_score}")


