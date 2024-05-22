#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding:
    Prototype: def validUTF8(data)
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data
    To handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    num_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if num_bytes == 0:
            while mask_byte & i:
                num_bytes += 1
                mask_byte = mask_byte >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        num_bytes -= 1
    if num_bytes == 0:
        return True
    return False
