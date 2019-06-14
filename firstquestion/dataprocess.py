import pandas as pd
f = open('../sourcedata/b6bce3abb838406daea9af48bf059c633.txt',encoding='UTF-8')
QRTA_NUM=dict()
ISIR_NUM=dict()
next(f)
#统计出现的次数
for eachline in f:
    Record=eachline.split()
    Record[0] = pd.to_datetime(Record[0])
    if(Record[1]=='QRTA'and Record[3]=='32'):
        if(Record[0] not in QRTA_NUM):
            QRTA_NUM[Record[0]] = 1
        else:
            QRTA_NUM[Record[0]] += 1
    if(Record[1]=='ISIR'and Record[3]=='32'):
        if(Record[0] not in ISIR_NUM):
            ISIR_NUM[Record[0]] = 1
        else:
            ISIR_NUM[Record[0]] += 1
ub=pd.date_range('2016-01-01','2016-12-31')
for i in ub:
    if (i not in QRTA_NUM):
        QRTA_NUM[i]=0
df1=pd.DataFrame.from_dict(QRTA_NUM,orient='index')
df1.columns=['y']
df1=df1.reset_index()
df1=df1.reset_index(drop=True)
df1.columns=['ds', 'y']
df1 = df1.sort_values(by='ds').reset_index(drop=True)
df1.to_csv ("perdayQRTA.csv" , index=True,header=True,encoding = "utf-8")
for i in ub:
    if (i not in ISIR_NUM):
        ISIR_NUM[i]=0
df2=pd.DataFrame.from_dict(ISIR_NUM,orient='index')
df2.columns=['y']
df2=df2.reset_index()
df2=df2.reset_index(drop=True)
df2.columns=['ds', 'y']
df2 = df2.sort_values(by='ds').reset_index(drop=True)
df2.to_csv ("perdayISIR.csv" , index=True,header=True,encoding = "utf-8")