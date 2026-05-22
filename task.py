def conv_num(num_str):
    """convert numeric string to int or float"""
    # string must not be empty
    if not isinstance(num_str, str) or len(num_str) == 0:
        return None
    # Handle negative sign
    negative = False
    s = num_str
    if s[0] == '-':
        negative = True
        s = s[1:]
        if len(s) == 0:
            return None
    # Handle hexadecimal
    if len(s) >= 2 and s[0] == '0' and s[1] in 'xX':
        hex_digits = s[2:]
        if len(hex_digits) == 0:
            return None
        result = _parse_hex(hex_digits)
        if result is None:
            return None
        return -result if negative else result
    # Handle decimal int/float
    return _parse_decimal(s, negative)


def my_datetime(num_sec):
    pass


def conv_endian(num, endian='big'):
    """
    Takes in an integer, num, and converts it to its hexadecimal
    value depending on it's endianess. The hex value is returned as
    a string. Function will return None if the endian is invalid.
    """

    hex_dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                      5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                      10: 'A', 11: 'B', 12: 'C', 13: 'D',
                      14: 'E', 15: 'F'}

    # invalid endian
    if endian not in ('big', 'little'):
        return None

    # keep track of negative num
    negative = num < 0
    num = abs(num)

    # check for 0
    if num == 0:
        return '00'

    # convert decimal to hex --> gather remainders in list
    hex_list = []
    while num != 0:
        remainder = num % 16
        hex_list.insert(0, hex_dictionary[remainder])
        num = num // 16

    # join list as a string, separated by no spaces
    hex_string = ''.join(hex_list)

    # prepend a 0 when there is an uneven number of bytes
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    # split into bytes
    byte_list = []
    for i in range(0, len(hex_string), 2):
        byte_list.append(hex_string[i:i + 2])

    # reverse if little endian
    if endian == 'little':
        byte_list.reverse()

    # separate bytes by a space
    hex_final = ' '.join(byte_list)

    # add negative sign if original num was neg
    if negative:
        hex_final = '-' + hex_final

    return hex_final


# Helper functions for conv_num()
def _parse_hex(hex_str):
    """Helper fucntion to parse a hex string (no prefix)
    and then return an int, or None if it is invalid"""
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    result = 0
    for char in hex_str:
        if char not in hex_map:
            return None
        result = result * 16 + hex_map[char]
    return result


def _parse_decimal(s, negative):
    """Parse a decimal integer or float string, return num or None"""
    dig_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    }
    dot_index = None
    for i, char in enumerate(s):
        if char == '.':
            if dot_index is not None:
                return None  # multiple decimal points
            dot_index = i
        elif char not in dig_map:
            return None  # INvalid
    if len(s) == 0 or s == '.':
        return None  # empty
    if dot_index is None:
        result = 0
        for char in s:
            result = result * 10 + dig_map[char]
        return -result if negative else result
    else:
        # Number is a flaot
        int_part = s[:dot_index]
        frac_part = s[dot_index + 1:]

        int_val = 0
        for char in int_part:
            int_val = int_val * 10 + dig_map[char]
        frac_val = 0
        frac_len = len(frac_part)
        for char in frac_part:
            frac_val = frac_val * 10 + dig_map[char]
        divisor = 10 ** frac_len if frac_len > 0 else 1
        result = int_val + frac_val / divisor
        return -result if negative else result
