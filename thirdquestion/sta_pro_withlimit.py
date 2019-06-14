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
result =dict()
# 对于重要用户，逐个调参。例如下面的操作
user = 'add06affbce0ba91833434932f6ed808'
df2 = generatedata(df,user)
df2['cap'] = 1.1 * (np.max(df2['y']))
df2['floor'] = 0.9*(np.min(df2['y']))
# print(df1)
plt.figure(1)
plt.plot(df2['ds'], df2['y'])
# 在此处调整模型参数
prophet = Prophet(growth='logistic',weekly_seasonality=False,changepoint_prior_scale=0.2)
prophet.fit(df2)
future = prophet.make_future_dataframe(periods=90)
future['cap'] = 1.1 * (np.max(df2['y']))
future['floor'] = 0.9 * (np.min(df2['y']))
forecast = prophet.predict(future)
# 输出预测数据
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
plt.figure(2)
plt.plot(forecast['ds'], forecast['yhat'])
plt.grid(True)
plt.show()
remain = forecast.ix[455, ['yhat']]
result[user] = remain
print(user,remain)

# 此处注释了的部分是用一种参数，跑所有的用户，但是性能不佳
# users = find_users(df)
# print(len(users))
# result =dict()
# for user in users:
#     df2 = generatedata(df, user)
#     df2['cap'] = 1.1 * (np.max(df2['y']))
#     df2['floor'] = 0.9 * (np.min(df2['y']))
#     # plt.figure(1)
#     # plt.plot(df2['ds'], df2['y'])
#     prophet = Prophet(growth='logistic', weekly_seasonality=False, changepoint_prior_scale=0.2)
#     prophet.fit(df2)
#     future = prophet.make_future_dataframe(periods=90)  # , include_history=False
#     future['cap'] = 1.1 * (np.max(df2['y']))
#     future['floor'] = 0.9 * (np.min(df2['y']))
#     forecast = prophet.predict(future)
#     # print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
#     # prophet.plot_components(forecast)
#     # plt.grid(True)
#     # plt.figure(3)
#     # plt.plot(forecast['ds'], forecast['yhat'])
#     # plt.grid(True)
#     # plt.show()
#     remain = forecast.ix[455, ['yhat']]
#     result[user] = remain
# df3 = pd.DataFrame.from_dict(result, orient='index')
# df3.columns=['a']
# p = df3.sort_values(by='a', axis=0,ascending=False)
# p.to_csv('beixuan.csv', index=True, header=True)
