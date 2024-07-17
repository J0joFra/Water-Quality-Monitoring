import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Pearson correlation coefficient, often denoted as 𝑟 r, measures the linear relationship between two continuous variables.
#Pearson correlation is sensitive to outliers and assumes a linear relationship between variables.

csv_file = r"C:\Users\JoaquimFrancalanci\Downloads\archive (20)\brisbane_water_quality.csv"
df = pd.read_csv(csv_file)

names2=['Average Water Speed', 'Average Water Direction', 'Chlorophyll', 'Temperature',
        'Dissolved Oxygen', 'Dissolved Oxygen (%Saturation)',  'pH',  'Salinity',  
        'Specific Conductance', 'Turbidity', ]

correlation_matrix = df[names2].corr(method='pearson')
correlation_matrix = correlation_matrix.round(4)
correlation_matrix.head()

# Correlation matric
plt.figure(figsize=(16,10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".3f", linewidths=.5)
plt.title('Pearson Correlation Matrix')
plt.show()

#From these results, we will learn that unexpected combinations are deeply related.





















