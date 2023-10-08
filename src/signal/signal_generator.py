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