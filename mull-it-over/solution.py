import re

def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def sum_proper_mult_instructions(location_list: list):
    mult_sum = 0
    for line in location_list:
        all_matches: list[tuple] = re.findall("mul\(([0-9]+),([0-9]+)\)", line)
        for a_match in all_matches:
            mult_sum += int(a_match[0]) * int(a_match[1])
    return mult_sum


def check_safe_lines_with_disable(location_list: list):
    mult_sum = 0
    enable_mul = True
    for line in location_list:
        all_matches: list[tuple] = re.findall("(mul\\(([0-9]+),([0-9]+)\\)|do(n't)?)", line)
        for a_match in all_matches:
            if a_match[0] == 'do':
                enable_mul = True
            elif a_match[0] == "don't":
                enable_mul = False
            else:
                if enable_mul:
                    mult_sum += int(a_match[1]) * int(a_match[2])
    return mult_sum


if __name__ == '__main__':
    location_list = read_file('input.txt')
    mult_sum = sum_proper_mult_instructions(location_list)
    print(f"required multiplication sum: {mult_sum}")
    test_location_list = read_file('test_input.txt')
    mult_sum = sum_proper_mult_instructions(test_location_list)
    print(f"required multiplication sum: {mult_sum}")
    similarity = check_safe_lines_with_disable(location_list)
    print(f"required safe lines without single plunger: {similarity}")
    similarity = check_safe_lines_with_disable(test_location_list)
    print(f"test safe lines without single plunger: {similarity}")
