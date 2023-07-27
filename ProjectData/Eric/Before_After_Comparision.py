import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu

# Assuming your data is in a CSV file called 'unemployment_data.csv'
df = pd.read_csv('Unemployment_rate_AllGender.csv')

# Preprocess the data
df['REF_DATE'] = pd.to_datetime(df['REF_DATE'])

# Data filtering based on date ranges
before_pandemic = df[(df['REF_DATE'] >= '2019-01-01') & (df['REF_DATE'] <= '2020-01-31')]
during_pandemic = df[(df['REF_DATE'] >= '2020-02-01') & (df['REF_DATE'] <= '2021-02-28')]
after_pandemic = df[(df['REF_DATE'] >= '2022-06-01') & (df['REF_DATE'] <= '2023-06-30')]


# Data Visualization - Box Plots
plt.figure(figsize=(10, 6))
sns.boxplot(x='GEO', y='Unemployment rate', hue='Period', data=pd.concat([before_pandemic.assign(Period='Before'), during_pandemic.assign(Period='During'), after_pandemic.assign(Period='After')]))
plt.xlabel('Province')
plt.ylabel('Unemployment Rate')
plt.title('Unemployment Rate Distribution Comparison')
plt.legend(title='Period')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Unemployment_rate_boxplot.png')

# Statistical Analysis - T-Tests
results_df = pd.DataFrame(columns=['Province' , 'p-value (Before vs During)' ,'p-value (Before vs After)','p-value (During vs After)'])

for province in df['GEO'].unique():
    before_values = before_pandemic[before_pandemic['GEO'] == province]['Unemployment rate']
    during_values = during_pandemic[during_pandemic['GEO'] == province]['Unemployment rate']
    after_values = after_pandemic[after_pandemic['GEO'] == province]['Unemployment rate']
    
    statistic_before_vs_during, pvalue_before_vs_during = mannwhitneyu(before_values, during_values, alternative='two-sided')
    statistic_before_vs_after, pvalue_before_vs_after = mannwhitneyu(before_values, after_values, alternative='two-sided')
    statistic_during_vs_after, pvalue_during_vs_after = mannwhitneyu(during_values, after_values, alternative='two-sided')
    
    results_df = results_df.append({
        'Province': province,
        'p-value (Before vs During)': pvalue_before_vs_during,
        'p-value (Before vs After)': pvalue_before_vs_after,
        'p-value (During vs After)': pvalue_during_vs_after
    }, ignore_index=True)

# Save the results to a CSV file
results_df.to_csv('ttest_results.csv', index=False)
