fruit = input("Enter the fruit : ")
flag = False
fruits = ['apples', 'bananas', 'blueberries', 'cherries', 'cantaloupes','dates', 'figs', 'grapes','kiwis', 'mangos']
for f in fruits:
	if f == fruit:
		print("The fruit "+fruit+" is present in the list")
		flag = True
		break
if flag == False:
	print("The fruit is not present in the list")
