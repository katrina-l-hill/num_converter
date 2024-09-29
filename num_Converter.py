# Function to convert to new base string
def convert_base(num_in_base_string, base_to_convert_from, base_to_convert_to):
    try:
        if base_to_convert_to == 2:
            return bin(int(num_in_base_string, base_to_convert_from))        
        if base_to_convert_to == 8:
            return oct(int(num_in_base_string, base_to_convert_from))
        if base_to_convert_to == 10:
            return str(int(num_in_base_string, base_to_convert_from))
        if base_to_convert_to == 16:
            return hex(int(num_in_base_string, base_to_convert_from))
    except ValueError:
        return f"Error: '{num_in_base_string}' is not valid in base {base_to_convert_from}."

def main():
    # User input
    # Take user input for an original base number
    num_in = input("Enter the number to convert: ")
    # Take user input for the base of the input number (between 2 and 16)
    base_to_convert_from = int(input("Enter the base of the input number (2, 8, 10 or 16): "))
    # Take user input for the base to which the number should be converted (between 2 and 16)
    base_to_convert_to = int(input("Enter the base to convert to (2, 8, 10 or 16): "))
    num_out_str = convert_base(num_in, base_to_convert_from, base_to_convert_to)
    print(num_out_str)

# Run the main function
if __name__ == "__main__":
    main()
