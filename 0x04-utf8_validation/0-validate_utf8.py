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
    num_bytes_to_follow = 0

    for byte in data:
        if num_bytes_to_follow == 0:
            if (byte >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                num_byte_to_follow = 2
            elif (byte >> 3) = 0b11110:
                num_bytes_to_follow = 3
            elif (byte >> 7) != 0:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1

        return num_bytes_to_follow == 0
