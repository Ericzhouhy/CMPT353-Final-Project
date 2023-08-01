import pandas as pd

# 读取CSV文件
df = pd.read_csv('unempl_rate_since_1977.csv')

# 提取sex为'both sexes'的所有行
df_filtered = df[df['Sex'] == 'Both sexes']

# 将结果保存为新的CSV文件
df_filtered.to_csv('un_1997.csv', index=False)
