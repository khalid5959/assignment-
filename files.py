def insert_line(filename, line_number, new_line):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Insert the new line at the specified position
        lines.insert(line_number - 1, new_line + '\n')

        with open(filename, 'w') as file:
            file.writelines(lines)
            print(f"Line inserted successfully at position {line_number}.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Usage example
file_to_modify = 'india.txt'
line_to_insert = "This is the new line to insert"
position_to_insert = 3  # Insert at line 3 (1-based index)

insert_line(file_to_modify, position_to_insert, line_to_insert)