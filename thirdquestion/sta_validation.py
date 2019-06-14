import pandas as pd
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from matplotlib import pyplot as plt

def generatedata(df,i):
    df4 = pd.DataFrame()
    df4['ds'] = df.columns
    df4['y'] = list(df.loc[i])
    return df4
df=pd.read_csv('../sourcedata/xdata.csv',index_col=0,header=0)
df= df.set_index('xinbianhao')
dates=df.columns
l=[]
for i in dates:
    temp=df.sort_values(by=i, axis=0, ascending=False).head(20).index
    l.extend(temp)
user=set(l)
res=dict()

New_years_Day = pd.DataFrame({
  'holiday': 'yuandan',
  'ds': pd.to_datetime(['2016-01-01', '2016-01-02', '2016-01-03',
                        '2016-12-31','2017-01-01', '2017-01-02']),
  'lower_window': 0,
  'upper_window': 0,
})
Spring_Festival = pd.DataFrame({
  'holiday': 'chunjie',
  'ds': pd.to_datetime(['2016-02-07', '2016-02-08', '2016-02-09','2016-02-10','2016-02-11','2016-02-12','2016-02-13',
                        '2017-01-27', '2017-01-28', '2017-01-29', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02']),
  'lower_window': 0,
  'upper_window': 0,
})
holidays = pd.concat((New_years_Day, Spring_Festival))
for i in user:
    df2 = generatedata(df,i)
    plt.figure(1)
    plt.plot(df2['ds'], df2['y'])
    # 在此处调整模型参数
    prophet = Prophet(weekly_seasonality=False)
    prophet.fit(df2)
    df_cv = cross_validation(
        prophet, '90 days', initial='270 days', period='90 days')
    print(df_cv)
    plt.figure(2)
    plt.plot(df_cv['ds'], df_cv['y'])
    plt.plot(df_cv['ds'], df_cv['yhat'])
    plt.grid(True)
    plt.show()
