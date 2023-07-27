import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 读取数据
data = pd.read_csv("covid_and_employment_total_included.csv")

# 获取数据中所有的城市名称
cities = data['GEO'].unique()

# 创建一个空的DataFrame来保存结果
results = pd.DataFrame(columns=['City', 'MSE', 'MAE', 'Feature Importance'])

# 对每个城市进行循环处理
for city in cities:
    # 选取当前城市的数据
    city_data = data[data['GEO'] == city]

    # 定义特征和目标变量
    features = city_data[['covid cases', 'covid deaths']]
    target = city_data['total unemployment rate(%)']

    # 拆分数据集为训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

    # 创建随机森林回归模型
    rf_model = RandomForestRegressor(n_estimators=100, min_samples_split=2, min_samples_leaf=1)

    # 训练模型
    rf_model.fit(X_train, y_train)

    # 对测试数据进行预测
    predictions = rf_model.predict(X_test)

    # 计算 MSE 和 MAE
    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)

    # 获取特征重要性
    feature_importances = rf_model.feature_importances_

    # 将结果添加到结果DataFrame中
    result = pd.DataFrame({'City': [city], 'MSE': [mse], 'MAE': [mae], 
                          'Feature Importance': [feature_importances]})
    results = pd.concat([results, result], ignore_index=True)

# 将结果保存到CSV文件
results.to_csv('results.csv', index=False)
