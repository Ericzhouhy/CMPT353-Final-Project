import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

# 读取数据
data = pd.read_csv("covid_and_employment_total_included.csv")

# 将数据转化为时间序列格式
data['REF_DATE'] = pd.to_datetime(data['REF_DATE'])
data.set_index('REF_DATE', inplace=True)

# 创建空的 list 用于存储结果
results = []
future_forecasts = []

# 对每一个城市进行预测
cities = data['GEO'].unique()
for city in cities:
    city_data = data[data['GEO'] == city]

    # 将数据划分为训练集和测试集
    size = int(len(city_data) * 0.66)
    train, test = city_data[0:size], city_data[size:len(city_data)]
    history = [x for x in train['total employment rate(%)']]
    predictions = list()

    # 遍历测试集
    for t in range(len(test)):
        model = ARIMA(history, order=(5,1,0))  # ARIMA模型参数需要根据实际情况调整
        model_fit = model.fit()
        output = model_fit.forecast()
        yhat = output[0]
        predictions.append(yhat)
        obs = test['total employment rate(%)'].iloc[t]
        history.append(obs)

        # 将结果添加到 results list 中
        result = pd.DataFrame({"city": [city], 
                               "date": [test.index[t]], 
                               "actual": [obs], 
                               "prediction": [yhat]})
        results.append(result)
    
    # 对未来两个月进行预测
    future_forecast = model_fit.forecast(steps=1)
    future_result = pd.DataFrame({"city": city, 
                                  "date": pd.date_range(start=test.index[-1] + pd.Timedelta(days=1), periods=2, freq='M'), 
                                  "prediction": future_forecast[0]})
    future_forecasts.append(future_result)

    # 计算预测误差
    error = mean_squared_error(test['total employment rate(%)'], predictions)
    print(f'{city} Test MSE: {error}')

# 将结果合并为一个 DataFrame 并写入 CSV 文件
results_df = pd.concat(results)
results_df.to_csv("predictions_vs_actuals.csv", index=False)

# 将未来的预测合并为一个 DataFrame 并写入 CSV 文件
future_forecasts_df = pd.concat(future_forecasts)
future_forecasts_df.to_csv("future_predictions.csv", index=False)
