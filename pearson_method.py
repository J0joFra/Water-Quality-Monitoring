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

# Definisci le colonne da utilizzare per i grafici di dispersione
columns_to_plot = ['Average Water Speed', 'Chlorophyll', 'Temperature', 'Dissolved Oxygen', 'pH']

# Creazione dei grafici di dispersione
plt.figure(figsize=(18, 12))
for i, column in enumerate(columns_to_plot, start=1):
    plt.subplot(3, 2, i)
    plt.scatter(df[column], df['Salinity'], alpha=0.5)
    plt.title(f'Scatter plot: {column} vs Salinity')
    plt.xlabel(column)
    plt.ylabel('Salinity')

plt.tight_layout()
plt.show()




















