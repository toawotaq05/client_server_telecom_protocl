import unittest
import numpy as np
from src.signal.signal_decoder import binary_to_string
from src.signal.signal_generator import string_to_binary


def test_bin_to_string():
    test_str = "SYN-ACK"
    binary_rep = string_to_binary(test_str)
    converted_str = binary_to_string(binary_rep)
    assert converted_str == test_str

def test_edge_cases_bin_to_string():
    test_str = "5trazS.ÖpP2!"
    binary_rep = string_to_binary(test_str)
    converted_str = binary_to_string(binary_rep)
    assert converted_str == test_str
