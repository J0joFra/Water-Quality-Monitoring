import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your CSV file
csv_file = r"C:\Users\JoaquimFrancalanci\Downloads\archive (20)\brisbane_water_quality.csv"

# Load data into a DataFrame
df = pd.read_csv(csv_file)

# Specify the columns for correlation calculation
names2 = ['Average Water Speed', 'Average Water Direction', 'Chlorophyll', 'Temperature',
          'Dissolved Oxygen', 'Dissolved Oxygen (%Saturation)', 'pH', 'Salinity',
          'Specific Conductance', 'Turbidity']

# Calculate Pearson correlation matrix
correlation_matrix = df[names2].corr(method='pearson').round(3)

# Plotting the correlation matrix as a heatmap
plt.figure(figsize=(16, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".3f", linewidths=.5)
plt.title('Pearson Correlation Matrix')
plt.show()






















