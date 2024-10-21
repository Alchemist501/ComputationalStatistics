#Experiment4.3:= Calculate the n-th order discrete diﬀerence along the given axis
import numpy as np
print("nth-order discrete difference along axis 0 : ",np.diff(np.array([1,2,4,7,0]),int(input("Enter value for n :"))))
