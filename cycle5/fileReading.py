# Experiment 5.1 := Write a program to count the number of words, sentences, upper case letters, lowercase letters and special symbols in a text stored in file.
import string as str

try:
    with open(input("Enter file name : "), "r") as file:
        text = file.read()
except FileNotFoundError:
    print(file, "is not found!")
print(
    "\nNumber of words : ",len(text.split()),
    "\nNumber of sentences : ",len(text.split("." or "!" or "?")),
    "\nNumber of uppercase letters : ",sum(1 for ch in text if ch.isupper()),
    "\nNumber of lower case letters : ",sum(1 for ch in text if ch.islower()),
    "\nNumber of special symbols : ",sum(1 for ch in text if ch in str.punctuation),
)
