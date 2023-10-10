import time
import os

input_file_name = input("Enter the name of the input file: ") + ".txt"

try:
    file_size = os.path.getsize(input_file_name)
    max_allowed_size = 200 * 1024 * 1024 
    
    if file_size > max_allowed_size:
        print(f"Error: File '{input_file_name}' is too large. Please choose a smaller file.")
    else:
        with open(input_file_name, 'r') as infile:
            lines = infile.readlines()

    with open('output.txt', 'w') as outfile:
        for i, line in enumerate(lines):
            print(line)
            if i == len(lines) - 1:
                modified_line = f'text ("{line.strip()}",1)\n'
            else:
                modified_line = f'text ("{line.strip()}",1),\n'
                outfile.write(modified_line)
                print("Converted!")
    print("Conversion complete. Check 'output.txt' for the results.")
            
except FileNotFoundError:
    print(f"Error: File '{input_file_name}' not found.")