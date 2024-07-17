# Brisbane Water Quality Analysis

This project involves analyzing water quality data from Brisbane using Python and several data analysis libraries. The data is sourced from a CSV file containing various parameters measured over time.

## Project Structure

The project consists of three Python scripts:

### 1. Script 1: Visualizing Time Series Data

- **File:** `visualize_data.py`
- **Libraries Used:** `pandas`, `matplotlib`, `seaborn`
- **Functionality:** This script performs the following tasks:
  - Loads the Brisbane water quality dataset from a CSV file.
  - Cleans the dataset by dropping unnecessary columns and filtering for data from the year 2023.
  - Converts the 'Timestamp' column to datetime format and sets it as the index.
  - Generates time series plots for each remaining water quality parameter, showcasing trends over time.

### 2. Script 2: Correlation Analysis and Scatter Plots

- **File:** `correlation_and_scatter.py`
- **Libraries Used:** `pandas`, `matplotlib`, `seaborn`
- **Functionality:** This script performs the following tasks:
  - Loads the Brisbane water quality dataset from the CSV file.
  - Filters the dataset to include only data from the year 2023.
  - Calculates the Pearson correlation matrix among selected water quality parameters.
  - Visualizes the correlation matrix using a heatmap for quick insights into parameter relationships.
  - Generates scatter plots to explore relationships between pairs of water quality parameters: Chlorophyll vs Dissolved Oxygen, Temperature vs pH, and Salinity vs Turbidity.

### 3. Script 3: Predictive Modeling

- **File:** `predictive_model.py`
- **Libraries Used:** `pandas`, `sklearn`, `matplotlib`
- **Functionality:** This script performs the following tasks:
  - Loads the Brisbane water quality dataset from the CSV file.
  - Cleans the dataset by dropping columns with quality information and filtering for data from August to December 2023.
  - Imputes missing values using mean imputation for selected variables.
  - Trains a Linear Regression model to predict Dissolved Oxygen based on Chlorophyll, Temperature, and Salinity.
  - Evaluates the model performance using R^2 score and Mean Squared Error (MSE).
  - Generates scatter plots comparing observed vs predicted Dissolved Oxygen values for each predictor variable.

## Getting Started

To run the scripts, ensure you have Python installed along with the necessary libraries: `pandas`, `matplotlib`, `seaborn`, and `sklearn`. You can install these libraries using `pip`:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Usage

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory containing the scripts and the CSV file.
3. Open a terminal or command prompt and run each script using Python:

```bash
python visualize_data.py
python correlation_and_scatter.py
python predictive_model.py
```

4. Each script will execute its respective analysis and generate plots to visualize different aspects of the Brisbane water quality data.

## Notes

- Ensure that the CSV file path (`brisbane_water_quality.csv`) is correctly specified in each script (`visualize_data.py`, `correlation_and_scatter.py`, and `predictive_model.py`) to match the location where you have stored the dataset on your machine.

- Make sure your Python environment is set up correctly with the required libraries to avoid any dependency issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

