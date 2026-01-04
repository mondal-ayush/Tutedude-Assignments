"""

Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:

Enter your first name: John
Enter your second name: Doe

Hello, John Doe! Welcome to the Python program.
"""

def main():
    firstname = input("Enter your first name: ")
    secondname = input("Enter your second name: ")
    print(f"\nHello, {firstname} {secondname}! Welcome to the Python program.")

if __name__ == '__main__':
    main()