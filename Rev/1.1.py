# Read a number in decimal and convert it into different bases.
num = int(input("Enter a number :"))
print(
    str(num)
    + " in binary form is "
    + str(bin(num))
    + "\n"
    + str(num)
    + " in octal form is "
    + str(oct(num))
    + "\n"
    + str(num)
    + " in hexadecimal form is "
    + str(hex(num))
)
