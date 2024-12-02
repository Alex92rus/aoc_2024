from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def count_safe_lines(location_list: list):
    line_stright = 0
    for line in location_list:
        numbers = [int(x) for x in line.split()]
        is_sorted_evenly = False
        for i in range(len(numbers)):
            subseq = [num for j, num in enumerate(numbers) if j != i]
            is_sorted_evenly_subseq = True
            if subseq[0] < subseq[1]:
                direction = 'ASC'
            else:
                direction = 'DESC'
            for j in range(len(subseq) - 1):
                if (not (direction == 'ASC' and subseq[j] < subseq[j + 1] < subseq[j] + 4) and
                        not (direction == 'DESC' and subseq[j] > subseq[j + 1] > subseq[j] - 4)):
                    is_sorted_evenly_subseq = False
                    break
            if is_sorted_evenly_subseq:
                is_sorted_evenly = True
        if is_sorted_evenly:
            line_stright += 1
    return line_stright


def check_safe_lines(location_list: list):
    line_stright = 0
    for line in location_list:
        numbers = [int(x) for x in line.split()]
        is_sorted_evenly = True
        if numbers[0] < numbers[1]:
            direction = 'ASC'
        else:
            direction = 'DESC'
        for i in range(len(numbers) - 1):
            if (not (direction == 'ASC' and numbers[i] < numbers[i + 1] < numbers[i] + 4) and
                    not (direction == 'DESC' and numbers[i] > numbers[i + 1] > numbers[i] - 4)):
                is_sorted_evenly = False
                break
        if is_sorted_evenly:
            line_stright += 1
    return line_stright


if __name__ == '__main__':
    location_list = read_file('input.txt')
    distance = count_safe_lines(location_list)
    print(f"required safe lines: {distance}")
    test_location_list = read_file('test_input.txt')
    distance = count_safe_lines(test_location_list)
    print(f"test safe lines: {distance}")
    similarity = check_safe_lines(location_list)
    print(f"required safe lines without single plunger: {similarity}")
    similarity = check_safe_lines(test_location_list)
    print(f"test safe lines without single plunger: {similarity}")
