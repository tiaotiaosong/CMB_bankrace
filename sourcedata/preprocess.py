import pandas as pd

def processdata():
    f = open('b6bce3abb838406daea9af48bf059c633.txt', mode='r', encoding='UTF-8')
    next(f)
    userdict = {'date': [],
                'zhaiyao': [],
                'drection': [],
                'bizhong': [],
                'trade': [],
                'remain': [],
                'bianhao': []}
    for eachline in f:
        l = eachline.split()
        userdict['date'].append(l[0])
        userdict['zhaiyao'].append(l[1])
        userdict['drection'].append(l[2])
        userdict['bizhong'].append(l[3])
        userdict['trade'].append(l[4])
        userdict['remain'].append(l[5])
        userdict['bianhao'].append(l[6])
    df = pd.DataFrame(userdict)
    df['trade']=df['trade'].map(lambda d:round(float(d),2))
    df['remain']=df['remain'].map(lambda d:round(float(d),2))
    df['start']=df['remain']-df['trade']
    df['start']=df['start'].map(lambda d:round(d,2))
    df=df[df['bizhong']=='32']
    df=df[['date','bianhao','start','remain']]
    return df

# 对所有用户一年中余额进行计算
df =processdata()
ub=pd.date_range('2016-01-01','2016-12-31')
users=set(df['bianhao'])
print((len(users)))
# l=[]
# count=0
# for user in users:
#     temp=pd.Series()
#     temp['xinbianhao']=user
#     df1=df[df['bianhao']==user]
#     df1 = df1.sort_values(by='date')
#     startday=min(df1['date'])
#     if(startday!='2016-01-01'):
#         ub1 = pd.date_range('2016-01-01', startday,freq='D')
#         df2 = df1[df1['date'] == startday]
#         df2=df2.reset_index(drop=True)
#         if (df2.shape[0] == 0):
#             continue
#         elif (df2.shape[0] == 1):
#             for day in ub1[:-1]:
#                 temp[day] = round(df2['start'].values[0],2)
#         else:
#             tempdict = dict()
#             for i in df2['start']:
#                 p = min(df2['remain'].map(lambda d: abs(d - i)))
#                 tempdict[i] = p
#             truestart = max(tempdict, key=tempdict.get)
#             for day in ub1[:-1]:
#                 temp[day] = truestart
#     for day in ub:
#         if day in temp:
#             continue
#         df2=df1[df1['date']==day]
#         if(df2.shape[0]==0):
#             temp[day] = temp[day - 1]
#         elif(df2.shape[0]==1):
#             temp[day]=round(df2['remain'].values[0],2)
#         else:
#             tempdict=dict()
#             for i in df2['remain']:
#                 p=min(df2['start'].map(lambda d:abs(d-i)))
#                 tempdict[i]=p
#             temp[day]=max(tempdict, key=tempdict.get)
#     l.append(temp)
#     count+=1
#     print(count)
#     if((count%10000)==0):
#         df1=pd.DataFrame(l)
#         df1.to_csv('data{i}.csv'.format(i=(count/10000)),index=True,header=True)
#         l=[]
# df1=pd.DataFrame(l)
# df1.to_csv('datalast.csv',index=True,header=True)
# # 由于数据量大，容易内存爆掉，所以分开保存再合并
# df3=pd.read_csv('data1.csv',index_col=0,header=0)
# df4=pd.read_csv('data2.csv',index_col=0,header=0)
# df5=pd.read_csv('datalast.csv',index_col=0,header=0)
# res=pd.concat([df3,df4,df5],axis=0,ignore_index=True)
# res.columns=[d.split()[0] for d in res.columns]
# res.to_csv('xdata.csv',index=True,header=True)