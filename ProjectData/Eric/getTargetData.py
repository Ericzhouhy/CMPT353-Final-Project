import pandas as pd

df = pd.read_csv('C:/Users/ericz/Desktop/CMPT353/CMPT353-Final-Project/ProjectData/Eric/combined.csv')

# Convert REF_DATE column to datetime type
df['REF_DATE'] = pd.to_datetime(df['REF_DATE'], format='%Y-%m')
start_date_1 = '2019-01-01'
end_date_1 = '2019-06-01'

# Filter the data based on the date range
filtered_df_1 = df[(df.iloc[:, 0] >= start_date_1) & (df.iloc[:, 0] <= end_date_1)]

start_date_2 = '2023-01-01'
end_date_2 = '2023-06-01'

filtered_df_2 = df[(df.iloc[:, 0] >= start_date_2) & (df.iloc[:, 0] <= end_date_2)]

# Display the filtered DataFrame
filtered_df_1.to_csv('data_2019.csv', index=False)
filtered_df_2.to_csv('data_2023.csv', index=False)