def intToBin(number):
    number = int(number)
    bin_number = ""

    if number == 0:
        return "0"

    while number > 0:
        remainder = number % 2
        bin_number = str(remainder) + bin_number
        number = number // 2

    return bin_number

def binToInt(number):
    number = str(number)
    decNumber = 0

    num_len = len(number)

    for index in range(num_len):
        power = num_len - index - 1
        decNumber += int(number[index]) * (2 ** power)

    return decNumber


def floatToBin(number):
    number = str(number)
    number = number.split(".")
    number = int(number)
    return number


def floatToBin(number):
    # Convert the number to float if it's not already
    number = float(number)
    bin_number = ""  # Initialize an empty string to store the binary representation

    # Edge case: if the input number is 0, return "0" as its binary representation
    if number == 0.0:
        return "0"

    # Handle negative numbers
    sign = ""  # Empty string to store sign bit
    if number < 0:
        sign = "1"  # Set sign bit to 1 for negative numbers
        number = -number  # Take the absolute value

    # Convert the integer part to binary
    int_part = int(number)
    bin_int_part = intToBin(int_part)

    # Convert the fractional part to binary
    frac_part = number - int_part
    bin_frac_part = ""
    precision = 20  # Set precision for fractional part

    while frac_part > 0 and len(bin_frac_part) < precision:
        # Multiply fractional part by 2 and append the integer part to the binary representation
        frac_part *= 2
        bin_frac_part += str(int(frac_part))
        # Update fractional part by taking the decimal part after multiplication
        frac_part -= int(frac_part)

    # Combine the integer and fractional parts with a binary point
    bin_number = bin_int_part + "." + bin_frac_part

    # Add sign bit if it's a negative number
    if sign:
        bin_number = sign + bin_number

    return bin_number


