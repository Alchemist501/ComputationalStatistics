# Experiment 2.2 := Define a tuple containing the names of different fruits.
# Write a python program that prompts the user to enter a fruit name.
# If the entered fruit name exists in the tuple, display a message confirming its presence
# Otherwise display a message indicating its absence.

fruits = ("Apple", "Orange", "Grapes", "Banana", "Blueberry", "PineApple")
fruit = input("Enter a string : ")
print(fruit, "is" if (fruit in fruits) else "is not", "present in the tuple.")
