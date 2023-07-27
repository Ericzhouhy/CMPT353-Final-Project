import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from scipy.stats import linregress
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

def to_datetime(date_str):
    return datetime.strptime(date_str, '%Y-%m')

data = pd.read_csv('../covid_and_employment_total_included.csv')


y = data['total unemployment rate(%)']
result = linregress(data['covid cases'], y)
result_2 = linregress(data['covid deaths'], y)
x_model_3 = pd.concat([data['covid cases'], data['covid deaths']], axis=1)
model_3 = LinearRegression(fit_intercept = True)
model_3.fit(X = x_model_3, y = y)
score_3 = model_3.score(x_model_3, y)
model_4 = make_pipeline(
    PolynomialFeatures(4),
    LinearRegression(fit_intercept = True)
)
model_4.fit(x_model_3, y)
score_4 = model_4.score(x_model_3, y)

print(f'p value for linear regression of unemployment rate and covid cases is {result.pvalue}')
print(f'the coeffecients are slope:{result.slope} and intercept{result.intercept}')
print(f'p value for linear regression of unemployment rate and covid deaths is {result_2.pvalue}')
print(f'the coeffecients are slope:{result_2.slope} and intercept{result_2.intercept}')
print(f'multi linear regression got score of {score_3}')
print(f'polynomial regression got score of {score_4}')

def predict_line(x):
    return result.slope * x + result.intercept

def predict_line_2(x):
    return result_2.slope * x + result_2.intercept

data_corr = data[['total population(1000)','total labor force(1000)',
                  'total fulltime employments(1000)',
                  'total unemployed',
                  'total unemployment rate(%)',
                  'total participation rate(%)',
                  'total employment rate(%)',
                  'covid cases',
                  'covid deaths']]
data_corr = data_corr.corr(method='pearson', numeric_only = True)
data_corr.to_csv('covid_employment_correlations.csv')

data['datetime'] = data['REF_DATE'].map(to_datetime)
data = data[data['GEO'] == 'Canada']

x_model_3 = pd.concat([data['covid cases'], data['covid deaths']], axis=1)
plt.scatter(data['datetime'], data['total unemployment rate(%)'])
plt.plot(data['datetime'], data['covid cases'].map(predict_line))
plt.plot(data['datetime'], data['covid deaths'].map(predict_line_2))
plt.plot(data['datetime'], model_3.predict(x_model_3))
plt.plot(data['datetime'], model_4.predict(x_model_3))

plt.legend(['unemployment',
            'prediction with covid cases',
            'prediction with covid deaths',
            'predictions with both',
            'polynomial regression of both'])
plt.show()
