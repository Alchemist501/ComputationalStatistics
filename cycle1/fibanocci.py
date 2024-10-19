num = int(input("Enter the number : "))
def fibanocci(num):
	if num == 0:
		return 0
	if num == 1 or num == 2:
		return 1
	if(num > 1):
		return fibanocci(num - 1) + fibanocci(num - 2)
print(fibanocci(num))
