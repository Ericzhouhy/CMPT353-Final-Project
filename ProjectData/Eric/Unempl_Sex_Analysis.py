
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns 
from matplotlib.ticker import MaxNLocator 

unempl_male = pd.read_csv('unempl_male.csv')
unempl_female = pd.read_csv('unempl_female.csv')
orig_data = pd.read_csv('unempl_rate_since_1977.csv')

unempl_canada = orig_data[orig_data['GEO'] == 'Canada']

plt.figure(figsize=(12, 6))

sns.lineplot(x='REF_DATE', y='Unemployment Rate', hue='Sex', data=unempl_canada)

plt.title('Unemployment Rate in Canada for Male and Female')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(nbins=8)) 

# Show the plot
plt.legend()
plt.tight_layout()
plt.savefig("Sex_Compar.png")

t_stat, p_value = stats.ttest_ind(unempl_canada[unempl_canada['Sex'] == 'Males']['Unemployment Rate'],
                                 unempl_canada[unempl_canada['Sex'] == 'Females']['Unemployment Rate'], equal_var=False)
print("p_value = ", p_value)
if p_value < 0.05:
    print(f'There is a significant difference in unemployment rates between male and female.')
else:
    print(f'There is no significant difference in unemployment rates between male and female.')
mean_unemployment_male = unempl_male.groupby('GEO')['Unemployment Rate'].mean()
median_unemployment_male = unempl_male.groupby('GEO')['Unemployment Rate'].median()
std_unemployment_male = unempl_male.groupby('GEO')['Unemployment Rate'].std()
min_unemployment_male = unempl_male.groupby('GEO')['Unemployment Rate'].min()
max_unemployment_male = unempl_male.groupby('GEO')['Unemployment Rate'].max()
summary_male = pd.DataFrame({
    'Mean': mean_unemployment_male,
    'Median': median_unemployment_male,
    'Standard Deviation': std_unemployment_male,
    'Minimum': min_unemployment_male,
    'Maximum': max_unemployment_male
})
summary_male.to_csv('Unemployment_Summary_Male.csv')
mean_unemployment_female = unempl_female.groupby('GEO')['Unemployment Rate'].mean()
median_unemployment_female = unempl_female.groupby('GEO')['Unemployment Rate'].median()
std_unemployment_female = unempl_female.groupby('GEO')['Unemployment Rate'].std()
min_unemployment_female = unempl_female.groupby('GEO')['Unemployment Rate'].min()
max_unemployment_female = unempl_female.groupby('GEO')['Unemployment Rate'].max()
summary_female = pd.DataFrame({
    'Mean': mean_unemployment_female,
    'Median': median_unemployment_female,
    'Standard Deviation': std_unemployment_female,
    'Minimum': min_unemployment_female,
    'Maximum': max_unemployment_female
})
summary_female.to_csv('Unemployment_Summary_Female.csv')
