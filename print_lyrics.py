def print_file_as_array(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print("{")
            for line in lines[:-1]:
                print(f'"{line.strip()}",')
            if lines:  # Check if the file is not empty
                print(f'"{lines[-1].strip()}"')  # Print the last line without a comma
            print("}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage:
file_name = "example.txt"  # Change this to your file's name
print_file_as_array(file_name)
