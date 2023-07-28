
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
df = pd.read_csv('C:/Users/ericz/Desktop/data_since_1977.csv')
df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], format='%Y-%m')
# Keep only unemployment rate data
unempl_rate_data = df[(df['Labour force characteristics'] == 'Unemployment rate')]
unempl_rate_data = unempl_rate_data[(unempl_rate_data['Age group'] == '15 years and over')]
unempl_rate_data = unempl_rate_data[(unempl_rate_data['Data type'] == 'Seasonally adjusted')]
unempl_rate_data = unempl_rate_data[(unempl_rate_data['Statistics'] == 'Estimate')]
unempl_rate_data = unempl_rate_data.sort_values(by='REF_DATE')
unempl_male = unempl_rate_data[unempl_rate_data['Sex'] == 'Males']
unempl_female = unempl_rate_data[unempl_rate_data['Sex'] == 'Females']
unempl_both_sexs = unempl_rate_data[unempl_rate_data['Sex'] == 'Both sexes']
columns_to_drop = ['DGUID', 'Labour force characteristics',  'Age group', 'Statistics', 'Data type', 'UOM', 'UOM_ID', 'SCALAR_FACTOR', 'SCALAR_ID', 'VECTOR', 'COORDINATE', 'STATUS', 'SYMBOL', 'TERMINATED', 'DECIMALS']
unempl_rate_data.drop(columns=columns_to_drop, inplace=True)
unempl_rate_data.rename(columns={'VALUE': 'Unemployment Rate'}, inplace=True)

unempl_rate_data.to_csv('unempl_rate_since_1977.csv', index=False)
unempl_male = unempl_rate_data[unempl_rate_data['Sex'] == 'Males']
unempl_female = unempl_rate_data[unempl_rate_data['Sex'] == 'Females']
unempl_both_sexs = unempl_rate_data[unempl_rate_data['Sex'] == 'Both sexes']
unempl_male.to_csv('unempl_male.csv', index=False)
unempl_female.to_csv('unempl_female.csv', index=False)
unempl_both_sexs.to_csv('unempl_both_sex.csv', index=False)
