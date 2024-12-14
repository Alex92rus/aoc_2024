from collections import defaultdict


def read_file(name: str):
    with open(name, 'rt') as f:
        line = f.readline()
        f.close()
    return line


def compressed_file_checksum(disk_map: str, whole_file_shift=False):
    id_map = []
    disk_id = -1
    disk_id_lenghts = defaultdict(int)
    zero_intervals: list[range] = []
    disk_intervals = {}
    for interval_length in range(len(disk_map)):
        if interval_length % 2 == 0:
            disk_id += 1
            disk_intervals[disk_id] = (range(len(id_map), len(id_map) + int(disk_map[interval_length])))
            for number_of_blocks in range(int(disk_map[interval_length])):
                id_map.append(disk_id)
            disk_id_lenghts[disk_id] = int(disk_map[interval_length])
        else:
            zero_intervals.append(range(len(id_map), len(id_map) + int(disk_map[interval_length])))
            for number_of_blocks in range(int(disk_map[interval_length])):
                id_map.append(0)
    print(id_map)
    front_id = 0
    back_id = len(id_map) - 1
    front_id += int(disk_map[0])
    if whole_file_shift:
        while disk_id > -1:
            for i in range(len(zero_intervals)):
                if (len(zero_intervals[i]) >= disk_id_lenghts[disk_id]
                        and disk_intervals[disk_id].start > zero_intervals[i].start):
                    for zero_index in range(zero_intervals[i].start, zero_intervals[i].start + disk_id_lenghts[disk_id]):
                        id_map[zero_index] = disk_id
                    for file_index in disk_intervals[disk_id]:
                        id_map[file_index] = 0
                    zero_intervals[i] = range(zero_intervals[i].start + disk_id_lenghts[disk_id], zero_intervals[i].stop)
                    break
            disk_id -= 1
    else:
        checksum_without_whole_file_shift(back_id, front_id, id_map)
    print(id_map)
    return sum([x * i for i, x in enumerate(id_map)])


def checksum_without_whole_file_shift(back_id, front_id, id_map):
    while back_id > front_id:
        if id_map[back_id] != 0 and id_map[front_id] == 0:
            id_map[front_id] = id_map[back_id]
            id_map[back_id] = 0
            back_id -= 1
            front_id += 1
        if id_map[front_id] != 0:
            front_id += 1
        if id_map[back_id] == 0:
            back_id -= 1


if __name__ == '__main__':
    location_list = read_file('input.txt')
    disk_checksum = compressed_file_checksum(location_list)
    print(f"required compressed check sum without whole file shifting: {disk_checksum}")
    test_location_list = read_file('test_input.txt')
    disk_checksum = compressed_file_checksum(test_location_list)
    print(f"test input: required compressed check sum without whole file shifting: {disk_checksum}")
    disk_checksum = compressed_file_checksum(location_list, whole_file_shift=True)
    print(f"required compressed check sum: {disk_checksum}")
    test_location_list = read_file('test_input.txt')
    disk_checksum = compressed_file_checksum(test_location_list, whole_file_shift=True)
    print(f"test input: required compressed check sum: {disk_checksum}")


