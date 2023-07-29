import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = pd.read_csv("covid_and_employment_total_included.csv")  

cities = data['GEO'].unique()

results = pd.DataFrame(columns=['City', 'MSE', 'MAE'])

for city in cities:
    city_data = data[data['GEO'] == city]
    
    features = city_data[['covid cases', 'covid deaths']]
    target = city_data['total unemployment rate(%)']

    scaler = StandardScaler()
    features = scaler.fit_transform(features)

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)

    knn = KNeighborsRegressor(n_neighbors=5)

    knn.fit(X_train, y_train)

    predictions = knn.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    
    print(f"City: {city}")
    print(f"Mean Squared Error: {mse}")
    print(f"Mean Absolute Error: {mae}")

    result = pd.DataFrame({'City': [city], 'MSE': [mse], 'MAE': [mae]})
    results = pd.concat([results, result])

results.to_csv('KNN_results.csv', index=False)
