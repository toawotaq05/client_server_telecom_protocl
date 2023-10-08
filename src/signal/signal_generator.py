"""
This module will generate the digital signals you want
to send, i.e., the sequence of bits.

It should be able to convert a message 
(like a string) into its binary representation.
"""

def string_to_binary(input_string):
    """
    Convert a string to its binary representation.
    
    Args:
    - input_string (str): The input string to be converted.
    
    Returns:
    - str: A binary string representation of the input string.
    """
    binary_output = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_output


def binary_to_string(input_binary):
    """
    Convert a binary string to its ASCII representation.
    
    Args:
    - input_binary (str): The binary string to be converted. 
                          Its length should be a multiple of 8.
    
    Returns:
    - str: The ASCII representation of the binary string.
    """
    if len(input_binary) % 8 != 0:
        raise ValueError("Input binary string length should be a multiple of 8.")
    
    string_output = ''.join(chr(int(input_binary[i:i+8], 2)) for i in range(0, len(input_binary), 8))
    return string_output


# For testing purposes:
if __name__ == '__main__':
    test_str = "SYN"
    binary_rep = string_to_binary(test_str)
    print(f"String: {test_str} -> Binary: {binary_rep}")
    converted_str = binary_to_string(binary_rep)
    print(f"Binary: {binary_rep} -> String: {converted_str}")
