import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your CSV file
csv_file = r"C:\Users\JoaquimFrancalanci\Downloads\archive (20)\brisbane_water_quality.csv"

# Load data into a DataFrame
df = pd.read_csv(csv_file)

# Convert 'Timestamp' column to datetime if necessary
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Filter rows where the year is 2023
df = df[df['Timestamp'].dt.year == 2023]

# Set figure size parameters
plt.figure(figsize=(18, 12))

# Scatter plot: Chlorophyll vs Dissolved Oxygen
plt.scatter(df['Chlorophyll'], df['Dissolved Oxygen'], alpha=0.5)
plt.title('Scatter plot: Chlorophyll vs Dissolved Oxygen')
plt.xlabel('Chlorophyll')
plt.ylabel('Dissolved Oxygen')
plt.tight_layout()

# Scatter plot: Temperature vs pH
plt.scatter(df['Temperature'], df['pH'], alpha=0.5)
plt.title('Scatter plot: Temperature vs pH')
plt.xlabel('Temperature')
plt.ylabel('pH')
plt.tight_layout()

# Scatter plot: Salinity vs Turbidity
plt.scatter(df['Salinity'], df['Turbidity'], alpha=0.5)
plt.title('Scatter plot: Salinity vs Turbidity')
plt.xlabel('Salinity')
plt.ylabel('Turbidity')
plt.tight_layout()

# Display all plots
plt.show()
