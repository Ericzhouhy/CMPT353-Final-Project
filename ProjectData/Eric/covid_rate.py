import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

df = pd.read_csv('covid19-download.csv')

df = df.dropna(subset=['ratecases_last7'])

# Convert 'date' column to datetime type in pandas for proper plotting
df['date'] = pd.to_datetime(df['date'])

# Group the data by 'prnameFR' and calculate the average rate of cases per day for each group
grouped_df = df.groupby(['prnameFR', pd.Grouper(key='date', freq='M')])['ratecases_last7'].mean().reset_index()

# Create a plot with multiple lines, one for each province
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

unique_provinces = df['prnameFR'].unique()

for province in unique_provinces:
    data_for_province = grouped_df[grouped_df['prnameFR'] == province]
    plt.plot(data_for_province['date'], data_for_province['ratecases_last7'], label=province)

# Format x-axis to show only the month
plt.gca().xaxis.set_major_locator(MonthLocator())
plt.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))

plt.xlabel('Date')
plt.ylabel('Rate of Cases (Last 7 days)')
plt.title('Rate of COVID-19 Cases by Province')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Covid-19-case-rate.png')