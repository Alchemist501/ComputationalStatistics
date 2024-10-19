import math

def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x


def isFibonacci(n):
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

n=int(input("Enter the number: "))

if (isFibonacci(n) == True):
	print(str(n)+ " is a Fibonacci Number")
else:
	print(str(n) + " is not a Fibonacci Number ")

