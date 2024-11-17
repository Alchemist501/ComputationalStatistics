# Experiment 2.1 := Given a string s containing just the characters '(',')','{','}','[',']', determine if the input string is valid.
# An input string is valid if
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the same order.
# Every close bracket has a corresponding open bracket of the same type.


def Valid(str):
    stack = []
    check = {"(": ")", "{": "}", "[": "]"}
    for ch in str:
        if ch in check:
            stack.append(ch)
        elif ch in check.values():
            if not stack or check[stack.pop()] != ch:
                return False
    return not stack


print("Valid string" if (Valid(input("Enter a string : "))) else "Invalid string")
