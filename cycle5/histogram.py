#Experiment 5.2 := Measure your classmate’s height and draw the histogram 
import matplotlib.pyplot as plt
heights = [170, 165, 172, 160, 168, 177, 182, 160, 175, 169, 155, 167]
bin_intervals = range(150, 190, 5)  
plt.hist(heights, bins=bin_intervals, edgecolor='black')
plt.title('Height Distribution of Classmates')
plt.xlabel('Height (cm)')
plt.ylabel('Number of Classmates')
plt.show()
