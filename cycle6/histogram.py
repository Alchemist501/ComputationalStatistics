import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('lois_continuous.csv', low_memory=False)
print(data.columns)
swale_data = data[data['SITE_NAME'] == 'Swale at Catterick Bridge']
temperature = swale_data['Temperature water continuous0476 (Cel)']
dissolved_oxygen = swale_data['Oxygen dissolved continuous0474 (% satn)']
mean_temperature = temperature.mean()
median_dissolved_oxygen = dissolved_oxygen.median()
print("Mean Temperature at Swale at Catterick Bridge: "+str(mean_temperature)+"°C")
print("Median Dissolved Oxygen at Swale at Catterick Bridge: "+str(median_dissolved_oxygen)+"mg/L")
plt.hist(temperature, bins=10, edgecolor='black')
plt.title('Temperature Distribution at Swale at Catterick Bridge')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

