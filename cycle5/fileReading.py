# Write a program to count the number of words, sentences, upper case letters, lowercase letters and special symbols in a text stored in file.
import string
file = input("Enter the name of the file :")
try:
    with open(file, "r") as file:
        text = file.read()
    print(
        "There are "+ str(len(text.split()))+ " words , "
        + str(len(text.split("." or "!" or "?")))+ " sentences , "
        + str(sum(1 for char in text if char.isupper()))+ " uppercase letters , "
        + str(sum(1 for char in text if char.islower()))+ " lowercase letters and "
        + str(sum(1 for char in text if char in string.punctuation))+ " special symbols present in the file."
    )
except FileNotFoundError:
    print(file + " not found!!!!")
