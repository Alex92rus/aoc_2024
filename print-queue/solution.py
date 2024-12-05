import re
from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def check_page_order(location_list: list):
    lines_to_consider = 0
    page_order_dict = defaultdict(set)
    for line in location_list:
        all_matches: list[tuple] = re.findall("([0-9]+)\|([0-9]+)", line)
        for a_match in all_matches:
            page_order_dict[int(a_match[0])].add(int(a_match[1]))
        if len(all_matches) == 0:
            pages_ahead = True
            sequence = [int(x) for x in line.split(",")]
            for i in range(len(sequence) - 1):
                pages_ahead = pages_ahead and all([x in page_order_dict[sequence[i]] for x in sequence[i + 1:len(sequence)]])
            if pages_ahead:
                middle_index = (len(sequence) - 1) // 2
                lines_to_consider += sequence[middle_index]

    return lines_to_consider


def repair_lines(location_list: list):
    lines_to_consider = 0
    page_order_dict = defaultdict(set)
    for line in location_list:
        all_matches: list[tuple] = re.findall("([0-9]+)\|([0-9]+)", line)
        for a_match in all_matches:
            page_order_dict[int(a_match[0])].add(int(a_match[1]))
        if len(all_matches) == 0:
            pages_ahead = True
            sequence = [int(x) for x in line.split(",")]
            right_sequence = [0 for x in sequence]
            for i in range(len(sequence)):
                page_index = len([x for x in sequence if (x != sequence[i]) and (x not in page_order_dict[sequence[i]])])
                right_sequence[page_index] = sequence[i]
                if page_index != i:
                    pages_ahead = False
            if not pages_ahead:
                print(right_sequence)
                middle_index = (len(right_sequence) - 1) // 2
                lines_to_consider += right_sequence[middle_index]
    return lines_to_consider


if __name__ == '__main__':
    location_list = read_file('input.txt')
    correctly_ordered_lines = check_page_order(location_list)
    print(f"page order is correct on {correctly_ordered_lines} lines")
    test_location_list = read_file('test_input.txt')
    correctly_ordered_lines = check_page_order(test_location_list)
    print(f"page order is correct on {correctly_ordered_lines} lines")
    repaired_lines_sum = repair_lines(location_list)
    print(f"page order is incorrect on lines with middle element sum of: {repaired_lines_sum}")
    repaired_lines_sum = repair_lines(test_location_list)
    print(f"Page order is incorrect on lines with middle element sum of: {repaired_lines_sum}")
