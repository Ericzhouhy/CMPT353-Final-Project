import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 读取数据
data = pd.read_csv("covid_and_employment_total_included.csv")  

# 获取数据中所有的城市名称
cities = data['GEO'].unique()

results = pd.DataFrame(columns=['City', 'MSE', 'MAE'])

# 对每个城市进行循环处理
for city in cities:
    # 选取当前城市的数据
    city_data = data[data['GEO'] == city]
    
    # 定义特征和目标变量
    features = city_data[['covid cases', 'covid deaths']]
    target = city_data['total unemployment rate(%)']

    # 数据标准化
    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    # 拆分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

    # 创建模型，假设我们选取5个邻居
    knn = KNeighborsRegressor(n_neighbors=5)

    # 训练模型
    knn.fit(X_train, y_train)

    # 预测结果
    predictions = knn.predict(X_test)

    # 计算和打印 MSE 和 MAE
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    
    print(f"City: {city}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")

    # 将结果保存到 DataFrame 中
    result = pd.DataFrame({'City': [city], 'MSE': [mse], 'MAE': [mae]})
    results = pd.concat([results, result])

# 将结果保存到 CSV 文件中
results.to_csv('KNN_results.csv', index=False)
