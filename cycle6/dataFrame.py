import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('BankChurners.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Step 2: Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in the dataset:")
print(missing_values[missing_values > 0])

# Step 3: Address Missing Values
# Fill missing numerical values with the mean and categorical with mode
df.fillna(df.mean(), inplace=True)  # For numerical columns
for column in df.select_dtypes(include=['object']).columns:
    df[column].fillna(df[column].mode()[0], inplace=True)  # For categorical columns

# Step 4: Present ratio of Attrition flags through a bar chart
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Attrition_Flag')
plt.title('Count of Attrition Flags')
plt.xlabel('Attrition Flag')
plt.ylabel('Count')
plt.show()

# Step 5: Bar Charts and Box Plots for Categorical Variables
# Example for 'Gender'
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Gender')
plt.title('Count of Customers by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
print(df.columns)

# Box Plot for 'Age' versus 'Attrition_Flag'
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Attrition_Flag', y='Customer_Age')
plt.title('Age Distribution by Attrition Flag')
plt.xlabel('Attrition Flag')
plt.ylabel('Age')
plt.show()

# Step 6: Compute Descriptive Statistics for the DataFrame
descriptive_stats = df.describe(include='all')
print("\nDescriptive statistics:")
print(descriptive_stats)

# Step 7: Correlation Coefficient Heatmap
correlation_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Step 8: Eliminate Unnecessary Columns
# Drop unnecessary columns (example: 'CLIENTNUM')
columns_to_drop = ['CLIENTNUM']  # Adjust this list based on your dataset
df.drop(columns=columns_to_drop, axis=1, inplace=True)
print("\nDataframe after dropping unnecessary columns:")
print(df.head())
