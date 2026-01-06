'''

Task 2: Write and Append Data to a File

Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.

Expected Output:
For example, if the user enters 25, the output should be:

Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
'''

data = input('Enter text to write to the file: ')
with open('output.txt', 'w') as f:
    f.write(data + "\n")
    print('Data successfully written to output.txt')

data = input('Enter additional text to append: ')
with open('output.txt', 'a') as f:
    f.write(data + "\n")
    print('Data successfully appended to output.txt')

try:
    with open('output.txt', 'r') as f:
            print('Final content of output.txt::')
            for line in f:
                print(line.rstrip('\n'))
except FileNotFoundError:
    print("Error: The file 'output.txt' was not found.")