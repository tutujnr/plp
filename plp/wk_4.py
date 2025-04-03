def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File '{input_filename}' was successfully read and modified.")
        print(f"Modified content has been written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing the files.")


def open_file_with_error_handling():
    filename = input("Enter the filename to open: ")

    try:
        # Try to open the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except IOError:
        print(f"Error: There was an issue opening the file '{filename}'.")


# Main program to call both functions
def main():
    # Step 1: Ask for the file to read and modify
    input_file = input("Enter the filename to read: ")
    output_file = input("Enter the filename to save modified content: ")
    
    # Perform the file read and write operation
    read_and_write_file(input_file, output_file)

    # Step 2: Open and display the content of a file with error handling
    open_file_with_error_handling()


if __name__ == "__main__":
    main()
