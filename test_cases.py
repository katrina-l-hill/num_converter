import num_Converter
from num_Converter import convert_base


# Separate tests for each base conversion
def test_to_other_bases():
    bin_inputs = ["0", "10", "1010", "1111"]
    oct_inputs = ["0o0", "0o2","0o12","0o17"]
    dec_inputs = ["0", "2", "10", "15"]
    hex_inputs = ["0x0", "0x2", "0xa", "0xf"]
    bin_outputs = ["0b0", "0b10","0b1010","0b1111"]
    oct_outputs = ["0o0", "0o2", "0o12", "0o17"]
    dec_outputs = ["0","2","10","15"]
    hex_outputs = ["0x0", "0x2", "0xa", "0xf"]

    #bin conv tests
    for i in range(len(bin_inputs)):
        assert convert_base(bin_inputs[i], 2, 2) == bin_outputs[i], f"Binary test failed: expected {bin_outputs[i]}, got {convert_base(bin_inputs[i], 2, 2)}"
        assert convert_base(bin_inputs[i], 2, 8) == oct_outputs[i], f"Octal test failed: expected {oct_outputs[i]}, got {convert_base(bin_inputs[i], 2, 8)}"
        assert convert_base(bin_inputs[i], 2, 10) == dec_outputs[i],f"Decimal test failed: expected {dec_outputs[i]}, got {convert_base(bin_inputs[i], 2, 10)}"
        assert convert_base(bin_inputs[i], 2, 16) == hex_outputs[i], f"Hexadecimal test failed: expected {hex_outputs[i]}, got {convert_base(bin_inputs[i], 2, 16)}"

    #oct conv tests
    for i in range(len(oct_inputs)):
        assert convert_base(oct_inputs[i], 8, 2) == bin_outputs[i], f"Binary test failed: expected {bin_outputs[i]}, got {convert_base(oct_inputs[i], 8, 2)}"
        assert convert_base(oct_inputs[i], 8, 8) == oct_outputs[i], f"Octal test failed: expected {oct_outputs[i]}, got {convert_base(oct_inputs[i], 8, 8)}"
        assert convert_base(oct_inputs[i], 8, 10) == dec_outputs[i], f"Decimal test failed: expected {dec_outputs[i]}, got {convert_base(oct_inputs[i], 8, 10)}"
        assert convert_base(oct_inputs[i], 8, 16) == hex_outputs[i], f"Hexadecimal test failed: expected {hex_outputs[i]}, got {convert_base(oct_inputs[i], 8, 16)}"

    #dec conv tests
    for i in range(len(dec_inputs)):
        assert convert_base(dec_inputs[i], 10, 2) == bin_outputs[i], f"Binary test failed: expected {bin_outputs[i]}, got {convert_base(dec_inputs[i], 10, 2)}"
        assert convert_base(dec_inputs[i], 10, 8) == oct_outputs[i], f"Octal test failed: expected {oct_outputs[i]}, got {convert_base(dec_inputs[i], 10, 8)}"
        assert convert_base(dec_inputs[i], 10, 10) == dec_outputs[i], f"Decimal test failed: expected {dec_outputs[i]}, got {convert_base(dec_inputs[i], 10, 10)}"
        assert convert_base(dec_inputs[i], 10, 16) == hex_outputs[i], f"Hexadecimal test failed: expected {hex_outputs[i]}, got {convert_base(dec_inputs[i], 10, 16)}"
        
    #hex conv tests
    for i in range(len(hex_inputs)):
        assert convert_base(hex_inputs[i], 16, 2) == bin_outputs[i], f"Binary test failed: expected {bin_outputs[i]}, got {convert_base(hex_inputs[i], 16, 2)}"
        assert convert_base(hex_inputs[i], 16, 8) == oct_outputs[i], f"Octal test failed: expected {oct_outputs[i]}, got {convert_base(hex_inputs[i], 16, 8)}"
        assert convert_base(hex_inputs[i], 16, 10) == dec_outputs[i], f"Decimal test failed: expected {dec_outputs[i]}, got {convert_base(hex_inputs[i], 16, 10)}"
        assert convert_base(hex_inputs[i], 16, 16) == hex_outputs[i], f"Hexadecimal test failed: expected {hex_outputs[i]}, got {convert_base(hex_inputs[i], 16, 16)}"

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