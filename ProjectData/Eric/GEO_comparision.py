import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from matplotlib.ticker import MaxNLocator 
from scipy.stats import mannwhitneyu

df = pd.read_csv('unempl_both_sex.csv')

plt.figure(figsize=(12, 6))
new_df = df[df['GEO'].isin(['Newfoundland and Labrador', 'Saskatchewan'])]

sns.lineplot(x='REF_DATE', y='Unemployment Rate', hue='GEO', data=new_df)

plt.title('Unemployment Rate in Newfoundland and Labrador and Saskatchewan')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(nbins=8)) 

# Show the plot
plt.legend()
plt.tight_layout()
plt.show()

Newfoundland = new_df[new_df['GEO']=='Newfoundland and Labrador']['Unemployment Rate']
Saskatchewan = new_df[new_df['GEO']=='Saskatchewan']['Unemployment Rate']
statistic, pvalue = mannwhitneyu(Newfoundland, Saskatchewan, alternative='two-sided')
print(pvalue)