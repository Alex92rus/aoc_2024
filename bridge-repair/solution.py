def read_file(name: str):
    with open(name, 'rt') as f:
        lines = f.readlines()
        f.close()
    return lines


def increment_single_binary(binary_str):
    """
    Increment a single binary string.
    Handles carrying over 1s and extending the string if needed.
    """
    # Convert binary string to list of characters for manipulation
    binary_chars = list(binary_str)

    # Start from the rightmost bit
    carry = 1
    for i in range(len(binary_chars) - 1, -1, -1):
        # Convert current bit to integer and add carry
        current_bit = int(binary_chars[i])
        total = current_bit + carry

        # Update bit and carry
        binary_chars[i] = str(total % 2)
        carry = total // 2

    # If there's still a carry, prepend 1
    if carry:
        binary_chars.insert(0, '1')

    return ''.join(binary_chars)


def increment_single_trinary(trinary_str):
    """
    Increment a single trinary string.
    Handles carrying over 1s and extending the string if needed.
    """
    # Convert trinary string to list of characters for manipulation
    trinary_chars = list(trinary_str)

    # Start from the rightmost bit
    carry = 1
    for i in range(len(trinary_chars) - 1, -1, -1):
        # Convert current bit to integer and add carry
        current_bit = int(trinary_chars[i])
        total = current_bit + carry

        # Update bit and carry
        trinary_chars[i] = str(total % 3)
        carry = total // 3

    # If there's still a carry, prepend 1
    if carry:
        trinary_chars.insert(0, '1')

    return ''.join(trinary_chars)

def equation_decide(line: str):
    target_value = int(line.split(':')[0])
    integer_operands = [int(x) for x in line.split(':')[1].split()]
    operator_mask = ''.join(['0' for x in range(len(integer_operands) - 1)])
    operator_number = len(operator_mask)
    for i in range(2 ** operator_number):
        equation_result = integer_operands[0]
        for j in range(1, len(integer_operands)):
            if operator_mask[j - 1] == '1':
                equation_result += integer_operands[j]
            else:
                equation_result *= integer_operands[j]
            if equation_result > target_value:
                break
        if equation_result == target_value:
            return target_value
        operator_mask = increment_single_binary(operator_mask)
    return 0


def equation_decide_three_operators(line: str):
    target_value = int(line.split(':')[0])
    integer_operands = [int(x) for x in line.split(':')[1].split()]
    operator_mask = ''.join(['0' for x in range(len(integer_operands) - 1)])
    operator_number = len(operator_mask)
    for i in range(3 ** operator_number):
        equation_result = integer_operands[0]
        for j in range(1, len(integer_operands)):
            if operator_mask[j - 1] == '2':
                equation_result = int(str(equation_result) + str(integer_operands[j]))
            elif operator_mask[j - 1] == '1':
                equation_result += integer_operands[j]
            else:
                equation_result *= integer_operands[j]
            if equation_result > target_value:
                break
        if equation_result == target_value:
            return target_value
        operator_mask = increment_single_trinary(operator_mask)
    return 0


def equation_sum(equation_list):
    return sum([equation_decide(equation) for equation in equation_list])


def equation_sum_with_concatenation(equation_list):
    return sum([equation_decide_three_operators(equation) for equation in equation_list])

if __name__ == '__main__':
    test_location_list = read_file('test_input.txt')
    equations = read_file('input.txt')
    engineered_value = equation_sum(test_location_list)
    print(f"test input: Sum of target values of equations: {engineered_value}")
    engineered_value = equation_sum(equations)
    print(f"assessment input: Sum of target values of equations: {engineered_value}")
    engineered_value = equation_sum_with_concatenation(test_location_list)
    print(f"test input: Sum of target values of equations: {engineered_value}")
    engineered_value = equation_sum_with_concatenation(equations)
    print(f"assessment input: Sum of target values of equations: {engineered_value}")
