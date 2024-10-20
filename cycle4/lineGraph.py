#Experiment4.7:= Plot line graph from NumPy array 
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.array([10,20,30,40,50,60,70,80,90,100]),range(1,11,1),marker="o",color="green")
plt.xlabel("Elements of array")
plt.ylabel("Index range")
plt.title("Numpy array")
plt.grid()
plt.show()
