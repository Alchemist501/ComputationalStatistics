import matplotlib.pyplot as plt
import pandas as pd

# Data
area = {'Africa': 11.7, 'Asia': 10.4, 'Europe': 1.9, 'North America': 9.4, 'Oceania': 3.3, 'South America': 6.9, 'Soviet Union': 7.9}

# Convert to DataFrame
df = pd.DataFrame(list(area.items()), columns=['Continent', 'Area'])

# Plotting
fig = plt.figure(figsize=(10, 5))
plt.bar(df['Continent'], df['Area'], color='red', width=0.5)
plt.xlabel("Continents")
plt.ylabel("Area")
plt.title("Bar Chart")
plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.tight_layout()  # Adjust layout to fit labels
plt.show()

