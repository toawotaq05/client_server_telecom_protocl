"""
Converts the received binary sequence back
into the original message
(like converting binary back into a string).
"""

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