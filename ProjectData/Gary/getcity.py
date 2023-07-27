import pandas as pd

# 读取包含所有城市数据的 CSV 文件
data = pd.read_csv("covid_and_employment_total_included.csv")  # 替换 "your_data.csv" 为您的数据文件路径

# 假设您希望提取名为 "CityA" 的城市的数据
city_name = "British Columbia"

# 提取特定城市的数据
city_data = data[data['GEO'] == city_name]

# 将提取的数据保存到单独的 CSV 文件中
output_file = f"{city_name}_data.csv"  # 设置输出文件名，例如 "CityA_data.csv"
city_data.to_csv(output_file, index=False)

print(f"Data for {city_name} has been saved to {output_file}.")
