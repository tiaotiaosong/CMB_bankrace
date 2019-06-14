import pandas as pd
import numpy as np
from fbprophet import Prophet
from matplotlib import pyplot as plt

def generatedata(df,i):
    df4 = pd.DataFrame()
    df4['ds'] = df.columns
    df4['y'] = list(df.loc[i])
    return df4
def find_users(df):
    dates = df.columns
    l = []
    for i in dates:
        temp = df.sort_values(by=i, axis=0, ascending=False).head(20).index
        l.extend(temp)
    users = list(set(l))
    return users
df=pd.read_csv('../sourcedata/xdata.csv',index_col=0,header=0)
df= df.set_index('xinbianhao')

users = find_users(df)
length=len(users)
print(length)

result=dict()

playoffs = pd.DataFrame({
  'holiday': 'yuandan',
  'ds': pd.to_datetime(['2016-01-01', '2016-01-02', '2016-01-03',
                        '2016-12-31','2017-01-01', '2017-01-02']),
  'lower_window': 0,
  'upper_window': 0,
})
superbowls = pd.DataFrame({
  'holiday': 'chunjie',
  'ds': pd.to_datetime(['2016-02-07', '2016-02-08', '2016-02-09','2016-02-10','2016-02-11','2016-02-12','2016-02-13',
                        '2017-01-27', '2017-01-28', '2017-01-29', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02']),
  'lower_window': 0,
  'upper_window': 0,
})
holidays = pd.concat((playoffs, superbowls))

users =find_users(df)
# 对于重要用户，逐个调参。例如下面的操作
user ='2c6683113e58c55221e5a8d07d82b056'
df2 = generatedata(df, user)

plt.figure(1)
plt.plot(df2['ds'], df2['y'])
# 在此处调整参数
prophet = Prophet(weekly_seasonality=False, changepoint_prior_scale=0.2, holidays=holidays)
prophet.fit(df2)
future = prophet.make_future_dataframe(periods=90)  # , include_history=False
forecast = prophet.predict(future)

# print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
prophet.plot_components(forecast)
remain = forecast.ix[455, ['yhat']]
result[user] = remain
print(user,remain)
plt.figure(3)
plt.plot(forecast['ds'], forecast['yhat'])
plt.grid(True)
plt.show()
