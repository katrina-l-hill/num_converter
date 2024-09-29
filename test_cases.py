import num_Converter
from num_Converter import convert_base

# Normal cases
def test_function_case_one():
    assert convert_base("1010", 2, 10) == "10"  # Binary 1010 should convert to decimal 10

def test_function_case_two():
    assert convert_base("17", 8, 16) == "0xf"  # Octal 17 should convert to hexadecimal f

def test_function_case_three():
    assert convert_base("a", 16, 2) == "0b1010"  # Hexadecimal a should convert to binary 1010

# Edge cases
def test_non_int_char():
    assert convert_base("G2", 16, 10) == "Error: 'G2' is not valid in base 16." # Test converting a string with non-integer characters (like 'G') in base 16

def test_base_out_of_range():
    assert convert_base("10", 10, 20) == None # Test converting from base 10 to an out-of-range base (20)

def test_input_zero():
    assert convert_base("0", 10, 2) == "0b0" # Test converting zero from base 10 to base 2