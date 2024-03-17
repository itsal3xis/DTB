def binToDec(binary_num):
    binary_str = str(binary_num)  # Ensure input is a string
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
        decimal_num = 0
        power = len(integer_part) - 1
        for digit in integer_part:
            decimal_num += int(digit) * (2 ** power)
            power -= 1

        power = -1
        for digit in fractional_part:
            decimal_num += int(digit) * (2 ** power)
            power -= 1
    else:
        decimal_num = 0
        power = len(binary_str) - 1
        for digit in binary_str:
            decimal_num += int(digit) * (2 ** power)
            power -= 1
    return decimal_num


def decToBin(decimal_num):
    if isinstance(decimal_num, int):
        return bin(decimal_num)[2:]
    elif isinstance(decimal_num, float):
        integer_part = int(decimal_num)
        fractional_part = decimal_num - integer_part
        int_binary = bin(integer_part)[2:]
        fractional_binary = ""
        while fractional_part > 0:
            fractional_part *= 2
            bit = int(fractional_part)
            fractional_binary += str(bit)
            fractional_part -= bit
        return int_binary + "." + fractional_binary


