
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
grouped_male = unempl_male.groupby('GEO')
grouped_female = unempl_female.groupby('GEO')
for geo, group_data in grouped_male:
    ax1.plot(group_data['REF_DATE'], group_data['VALUE'],label=geo)
ax1.set_title('Plot Grouped by GEO for Males')
for geo, group_data in grouped_female:
    ax2.plot(group_data['REF_DATE'], group_data['VALUE'],label=geo)
ax2.set_title('Plot Grouped by GEO for Females')
plt.xlabel('Date')
ax1.set_ylabel('Value')
ax2.set_ylabel('Value')
plt.legend() 
plt.xticks(rotation=45)
plt.tight_layout() 
plt.savefig('Unemployment_rate.png')
plt.close()
unempl_canada = unempl_rate_data[unempl_rate_data['GEO'] == 'Canada']
t_stat, p_value = stats.ttest_ind(unempl_canada[unempl_canada['Sex'] == 'Males']['VALUE'],
                                 unempl_canada[unempl_canada['Sex'] == 'Females']['VALUE'], equal_var=False)
print("p_value = ", p_value)
if p_value < 0.05:
    print(f'There is a significant difference in unemployment rates between male and female.')
else:
    print(f'There is no significant difference in unemployment rates between male and female.')
mean_unemployment_male = unempl_male.groupby('GEO')['VALUE'].mean()
median_unemployment_male = unempl_male.groupby('GEO')['VALUE'].median()
std_unemployment_male = unempl_male.groupby('GEO')['VALUE'].std()
min_unemployment_male = unempl_male.groupby('GEO')['VALUE'].min()
max_unemployment_male = unempl_male.groupby('GEO')['VALUE'].max()
summary_male = pd.DataFrame({
    'Mean Unemployment': mean_unemployment_male,
    'Median Unemployment': median_unemployment_male,
    'Standard Deviation': std_unemployment_male,
    'Minimum Unemployment': min_unemployment_male,
    'Maximum Unemployment': max_unemployment_male
})
summary_male.to_csv('Unemployment_Summary_Male.csv')
mean_unemployment_female = unempl_male.groupby('GEO')['VALUE'].mean()
median_unemployment_female = unempl_male.groupby('GEO')['VALUE'].median()
std_unemployment_female = unempl_male.groupby('GEO')['VALUE'].std()
min_unemployment_female = unempl_male.groupby('GEO')['VALUE'].min()
max_unemployment_female = unempl_male.groupby('GEO')['VALUE'].max()
summary_female = pd.DataFrame({
    'Mean Unemployment': mean_unemployment_female,
    'Median Unemployment': median_unemployment_female,
    'Standard Deviation': std_unemployment_female,
    'Minimum Unemployment': min_unemployment_female,
    'Maximum Unemployment': max_unemployment_female
})
summary_female.to_csv('Unemployment_Summary_Female.csv')