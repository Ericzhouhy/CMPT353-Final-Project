import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 读取数据
data = pd.read_csv("covid_and_employment_total_included.csv")  

# 获取数据中所有的城市名称
cities = data['GEO'].unique()

results = []

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

    # 创建模型
    model = Sequential()
    model.add(Dense(16, input_dim=X_train.shape[1], activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1))

    # 编译模型
    model.compile(optimizer=Adam(), loss='mean_squared_error', metrics=['mean_absolute_error'])

    # 训练模型
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=10, verbose=0)

    # 测试模型
    mse, mae = model.evaluate(X_test, y_test, verbose=0)

    print(f"City: {city}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")

    # 将结果保存到 list 中
    results.append({'City': city, 'MSE': mse, 'MAE': mae})

# 将结果保存到 CSV 文件中
results_df = pd.DataFrame(results)
results_df.to_csv('DNN_results.csv', index=False)
