import re
from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        line = f.readline()
        f.close()
    return line


def assort_stones(stones_list: list, blinks_number=0):
    stone_numbers_dict = defaultdict(int)
    for stone in stones_list:
        stone_numbers_dict[stone] += 1
    for blink in range(blinks_number):
        new_list = defaultdict(int)
        print(f'Blink number: {blink}')
        for stone in stone_numbers_dict:
            if stone == 0:
                new_list[1] += stone_numbers_dict[0]
            elif len(str(stone)) % 2 == 0:
                pow_ten = 10 ** (len(str(stone)) // 2)
                major = stone // pow_ten
                reminder = stone % pow_ten
                new_list[major] += stone_numbers_dict[stone]
                new_list[reminder] += stone_numbers_dict[stone]
            else:
                new_stone = stone * 2024
                new_list[new_stone] += stone_numbers_dict[stone]
        stone_numbers_dict = new_list
    return sum(stone_numbers_dict.values())


if __name__ == '__main__':
    stone_sequence = read_file('input.txt')
    stone_sequence = [int(x) for x in stone_sequence.split()]
    number_of_final_stones = assort_stones(stone_sequence, blinks_number=25)
    print(f"the final number of stones after 25 blinks are {number_of_final_stones}.")
    test_stone_sequence = read_file('test_input.txt')
    test_stone_sequence = [int(x) for x in test_stone_sequence.split()]
    number_of_final_stones = assort_stones(test_stone_sequence, blinks_number=25)
    print(f"test: the final number of stones after 25 blinks are {number_of_final_stones}.")
    stone_sequence = assort_stones(stone_sequence, blinks_number=75)
    print(f"the final number of stones after 75 blinks are {stone_sequence}.")
    number_of_final_stones = assort_stones(test_stone_sequence, blinks_number=75)
    print(f"test: the final number of stones after 75 blinks are {number_of_final_stones}.")
