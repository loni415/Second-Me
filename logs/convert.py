def convert_to_utf8(input_file_path, output_file_path):
    """
    Converts a text file to UTF-8 encoding.

    Args:
        input_file_path (str): Path to the input text file.
        output_file_path (str): Path to the output UTF-8 encoded text file.
    """
    try:
        # Open the input file with universal newline support
        with open(input_file_path, 'r', encoding='utf-8', errors='ignore') as input_file:
            content = input_file.read()

        # Write the content to the output file in UTF-8 encoding
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(content)

        print(f"File successfully converted to UTF-8: {output_file_path}")
    except Exception as e:
        print(f"Error during conversion: {e}")

# Example usage
if __name__ == "__main__":
    input_path = "/Users/lukasfiller/Downloads/secondme_knowledge/dis_ch8_1.txt"
    output_path = "/Users/lukasfiller/Downloads/secondme_knowledge/dis_ch8_1_sm.txt"
    convert_to_utf8(input_path, output_path)