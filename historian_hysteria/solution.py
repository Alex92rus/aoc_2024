from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines

def calculate_distance(location_list: list):
    list_left = []
    list_right = []
    for line in location_list:
        numbers = line.split()
        list_left.append(int(numbers[0]))
        list_right.append(int(numbers[1]))
    list_left.sort()
    list_right.sort()
    diff = 0
    for i, e in enumerate(zip(list_left, list_right)):
        diff += abs(e[0] - e[1])
    return diff

def calculate_similarity(location_list: list):
    list_left = []
    dict_right = defaultdict(int)
    for line in location_list:
        numbers = line.split()
        list_left.append(int(numbers[0]))
        dict_right[int(numbers[1])] += 1
    sim = 0
    for i, e in enumerate(list_left):
        sim += e * dict_right[e]
    return sim

if __name__ == '__main__':
    location_list = read_file('input.txt')
    distance = calculate_distance(location_list)
    print(f"required distance: {distance}")
    test_location_list = read_file('test_input.txt')
    distance = calculate_distance(test_location_list)
    print(f"test distance: {distance}")
    similarity = calculate_similarity(location_list)
    print(f"required similarity: {similarity}")
    similarity = calculate_similarity(test_location_list)
    print(f"test similarity: {similarity}")