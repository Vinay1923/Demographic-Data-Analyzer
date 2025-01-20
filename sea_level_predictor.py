import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
data = pd.read_csv('epa-sea-level.csv')

# Scatter plot
plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

# Create a line of best fit from the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
years_extended = range(1880, 2051)
sea_levels_extended = [slope * year + intercept for year in years_extended]
plt.plot(years_extended, sea_levels_extended, label='Best Fit Line (1880-2050)', color='r')

# Create a line of best fit for data from 2000 onwards
data_recent = data[data['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])
sea_levels_recent = [slope_recent * year + intercept_recent for year in years_extended]
plt.plot(years_extended, sea_levels_recent, label='Best Fit Line (2000-2050)', color='g')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()

# Save the plot
plt.savefig('sea_level_predictor.png')
plt.show()
