# Experiment5.3:= Table contains population and murder rates (in units of murders per 100,000 people per year) for different states. Compute the mean, median and variance for the population.
import statistics as st

data = [4779736, 710231, 6392017, 2915918, 37253956, 5029196, 3574097, 897934]
print("Mean is : ", st.mean(data))
print("Median is : ", st.median(data))
print("Variance is : ", st.variance(data))
