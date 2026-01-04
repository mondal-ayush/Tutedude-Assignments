"""

Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
 Expected Output:
The output should include the result of each operation performed, for example:

"""

def main():
    print("::Welcome to the Calculator Program V.0.1::")

    while True:
        print("\n1 -> Addition\n"
              "2 -> Subtraction\n"
              "3 -> Multiplication\n"
              "4 -> Division\n"
              "5 -> Exit\n")

        choice = input("Enter your choice: ").strip()
        if choice == "5":
            break

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == "1":
            print(f"Addition of {num1} and {num2} : ", num1 + num2)
        elif choice == "2":
            print(f"Subtraction of {num1} and {num2} : ", num1 - num2)
        elif choice == "3":
            print(f"Multiplication of {num1} and {num2} : ", num1 * num2)
        elif choice == "4":
            smaller = num1 if num1 < num2 else num2
            greater = num1 if num1 > num2 else num2
            print(f"Division of {greater} and {smaller} : ", greater / smaller)
        else:
            print("Invalid input. Please try again.")

    print("Thank you for using the Calculator Program V.0.1.")

if __name__ == '__main__':
    main()