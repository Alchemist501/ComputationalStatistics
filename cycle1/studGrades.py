N = int(input("Enter the number of subjects : "))
sub = []
for i in range(N):
	sub.append(input("Enter the subject : "))
mark = []
for s in sub:
	mark.append(int(input("Enter the marks for subject "+s+" = ")))
avg = sum(mark)/len(mark)
dic = dict(zip(sub,mark))
print("The dictionary of student is ")
print(dic)
print("Average of marks is "+str(avg))
