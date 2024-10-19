import numpy as np

data = [
    ["Alabama", 4779736, 5.7],
    ["Alaska", 710231, 5.6],
    ["Arizona", 6392017, 4.7],
    ["Arkansas", 2915918, 5.6],
    ["California", 37253956, 4.4],
    ["Colorado", 5029196, 2.8],
    ["Connecticut", 3574097, 2.4],
    ["Delaware", 897934, 5.8]
]
murder_rates = [row[2] for row in data]
mean_murder_rate = sum(murder_rates) / len(murder_rates)
murder_rates_sorted = sorted(murder_rates)
n = len(murder_rates)
if n % 2 == 0:
    median_murder_rate = (murder_rates_sorted[n // 2 - 1] + murder_rates_sorted[n // 2]) / 2
else:
    median_murder_rate = murder_rates_sorted[n // 2]
variance_murder_rate = sum((x - mean_murder_rate) ** 2 for x in murder_rates) / n
print("Mean Murder Rate: "+str(mean_murder_rate)+" per 100,000 people")
print("Median Murder Rate: "+str(median_murder_rate)+" per 100,000 people")
print("Variance of Murder Rates: "+str(variance_murder_rate))

