def conv_num(num_str):
    pass


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
