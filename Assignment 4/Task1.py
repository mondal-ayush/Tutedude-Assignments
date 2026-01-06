'''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.

Expected Output:

If the file exists:

Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

If the file does not exist:

Error: The file 'sample.txt' was not found.
'''

try:
    with open('sample.txt', 'r') as f:
        print('Reading file content:')
        for line in f.readlines():
            print(line.rstrip('\n'))
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
