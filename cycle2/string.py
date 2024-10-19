s = input("Enter the string : ")
def Valid(s):
	ls = ['{','(','[',']',')','}']
	for i in range(len(s)):
		for j in range(len(ls)):
			if s[i] == ls[j] and s[len(s)-i-1] != ls[len(ls)-j-1]:
				return False
	return True
if Valid(s) :
	print("The string is valid")
else:
	print("The string is not valid")
