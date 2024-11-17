# Experiment 1.1 := Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
n = int(input("Enter the number : "))
print(n, "is an odd number" if (n % 2 == 1) else "is an even number")
