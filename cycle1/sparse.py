r=int(input("enter no of rows:"))
c=int(input("enter no of cols"))
matrix=[]
print("enter the entries rowwise:")
for i in range(r):
	a=[]
	for j in range(c):
		a.append(int(input("Enter matrix["+str(i)+"]["+str(j)+"] = ")))
	matrix.append(a)
print()
for i in range(r):
	for j in range(c):
		print(matrix[i][j])
	print()
dic = {}
for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		if matrix[i][j]!=0:
			dic[i,j] = matrix[i][j]
print("position of non zero elements in the matrix is :")
print(dic)
