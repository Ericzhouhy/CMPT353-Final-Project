import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_csv('C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/Eric/combined.csv')

df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], format='%Y-%m')

# Keep only unemployment rate data
unempl_rate_data = df[(df['Labour force characteristics'] == 'Unemployment rate')]
unempl_rate_data = unempl_rate_data.sort_values(by='REF_DATE')
unempl_rate_data.to_csv('unemployment_rate.csv', index=False)

unempl_male = unempl_rate_data[unempl_rate_data['Sex'] == 'Males']
unempl_female = unempl_rate_data[unempl_rate_data['Sex'] == 'Females']

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

mean_unemployment = df.groupby('GEO')['Unemployment Rate'].mean()
print(mean_unemployment)
