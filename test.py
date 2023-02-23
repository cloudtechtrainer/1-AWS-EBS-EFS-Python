# Open the input file for reading
with open('my_input_files/input_file.txt', 'r') as input_file:

    # Read the contents of the input file
    input_text = input_file.read()

    # Modify the text (in this case, convert it to uppercase)
    modified_text = input_text.upper()

# Open the output file for writing
with open('my_output_files/output_file.txt', 'w') as output_file:

    # Write the modified text to the output file
    output_file.write(modified_text)
