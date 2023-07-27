import pandas as pd
from scipy.stats import linregress

data = pd.read_csv('../covid_and_employment_total_included.csv')

result = linregress(data[['total unemployment rate(%)', 'covid cases']])
result_2 = linregress(data[['total unemployment rate(%)', 'covid deaths']])

print(f'the p value for linear regression of unemployment rate and covid cases is {result.pvalue}')
print(f'the p value for linear regression of unemployment rate and covid deaths is {result_2.pvalue}')
