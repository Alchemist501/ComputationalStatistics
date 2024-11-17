import string as str

try:
    with open(input("Enter file name : "), "r") as file:
        text = file.read()
except FileNotFoundError:
    print(file, " is not found!!!")

print()
print("Number of sentences are : ", len(text.split("." or "!" or "?")))
print("Number of uppercase letters are : ", sum(1 for ch in text if ch.isupper()))
print("Number of lowercase letters are : ", sum(1 for ch in text if ch.islower()))
print(
    "\nNumber of words are : ",
    len(text.split()),
    "\nNumber of special symbols are : ",
    sum(1 for ch in text if ch in str.punctuation),
)
