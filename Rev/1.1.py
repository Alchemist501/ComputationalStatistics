# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
num = int(input("Enter a number :"))
print(
    str(num) + " is an even number"
    if (num % 2 == 0)
    else str(num) + " is an odd number"
)
