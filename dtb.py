def decToBin(number):
    number = int(number)
    bin_number = ""

    if number == 0:
        return "0"

    while number > 0:
        remainder = number % 2
        bin_number = str(remainder) + bin_number
        number = number // 2

    return bin_number

def binToDec(number):
    number = str(number)
    decNumber = 0

    num_len = len(number)

    for index in range(num_len):
        power = num_len - index - 1
        decNumber += int(number[index]) * (2 ** power)

    return decNumber
