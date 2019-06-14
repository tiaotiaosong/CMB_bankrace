import pandas as pd
import numpy as np
from fbprophet import Prophet
from matplotlib import pyplot as plt

# 此模型利用箱型图原理，去掉异常值，进行预测。
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
print('用户 = ',len(users))
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

result=dict()
# for user in users:
for i in range(1):
    user='7786339eb7b3e47e79ddadeff5c24cd6'
    df2 = generatedata(df,user)
    plt.figure(1)
    plt.plot(df2['ds'], df2['y'])
    UpperLimit = df2[['y']].quantile(0.75, axis=0) + (df2[['y']].quantile(0.75, axis=0) - df2[['y']].quantile(0.25, axis=0)) * 0.8
    LowerLimit = df2[['y']].quantile(0.25, axis=0) - (df2[['y']].quantile(0.75, axis=0) - df2[['y']].quantile(0.25, axis=0)) * 0.8
    middle = float(df2[['y']].quantile(0.5, axis=0))
    templist = []
    for d in df2['y']:
        if ((d <= float(UpperLimit)) and (d >= float(LowerLimit))):
            templist.append(d)
        else:
            templist.append(np.NaN)
    df2['y'] = templist
    df2['cap'] = 2 * (np.max(df2['y']))
    df2['floor'] = 0
    plt.figure(2)
    plt.plot(df2['ds'], df2['y'])

    # 在此处调整模型参数
    prophet = Prophet(growth='logistic',weekly_seasonality=False,changepoint_prior_scale=0.2)
    prophet.fit(df2)
    future = prophet.make_future_dataframe(periods=90,include_history=False)#, include_history=False
    future['cap'] = 2 * (np.max(df2['y']))
    future['floor'] = 0
    forecast = prophet.predict(future)
    # 输出预测结果
    # print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])
    remain = forecast.ix[89, ['yhat']]
    result[user] = remain
    print(user, remain)

    plt.figure(3)
    plt.plot(forecast['ds'], forecast['yhat'])
    plt.grid(True)
    plt.show()
