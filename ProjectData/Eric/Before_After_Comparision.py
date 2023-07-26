import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/Eric/combined.csv')

df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], format='%Y-%m')

# Keep only unemployment rate data
unempl_rate_data = df[(df['Labour force characteristics'] == 'Unemployment rate')]
unempl_rate_data = unempl_rate_data.sort_values(by='REF_DATE')


start_date_1 = '2019-01-01'
end_date_1 = '2020-01-01'

# Filter the data based on the date range
before_pandemic = unempl_rate_data[(unempl_rate_data['REF_DATE'] >= start_date_1) & (unempl_rate_data['REF_DATE'] <= end_date_1)]

start_date_2 = '2022-06-01'
end_date_2 = '2023-06-01'

after_pandemic = unempl_rate_data[(unempl_rate_data['REF_DATE'] >= start_date_2) & (unempl_rate_data['REF_DATE'] <= end_date_2)]

# Display the filtered DataFrame
before_pandemic.to_csv('unemployment_rate_before_pandemic.csv', index=False)
after_pandemic.to_csv('unemployment_rate_after_pandemic.csv', index=False)