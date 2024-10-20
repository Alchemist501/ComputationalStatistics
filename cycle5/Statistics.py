#Experiment5.3:= Table contains population and murder rates (in units of murders per 100,000 people per year) for different states. Compute the mean, median and variance for the population.
import statistics as stat
data =  [
    ["Alabama", 4779736, 5.7],
    ["Alaska", 710231, 5.6],
    ["Arizona", 6392017, 4.7],
    ["Arkansas", 2915918, 5.6],
    ["California", 37253956, 4.4],
    ["Colorado", 5029196, 2.8],
    ["Connecticut", 3574097, 2.4],
    ["Delaware", 897934, 5.8]
]
ls = []
for row in data:
	ls.append(row[1])
print(str(stat.mean(ls))+" is the mean of the population , "
	+str(stat.median(ls))+" is the median and "
	+str(stat.variance(ls))+" is the variance"
)
