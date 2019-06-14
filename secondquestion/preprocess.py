import pandas as pd
import matplotlib.pyplot as plt
f = open('b6bce3abb838406daea9af48bf059c633.txt',encoding='UTF-8')
QRTA_NUM=dict()
next(f)
for eachline in f:
    Record=eachline.split()
    Record[0] = pd.to_datetime(Record[0])
    if(Record[1]=='QRTA'and Record[3]=='32'):
        if(Record[0] not in QRTA_NUM):
            QRTA_NUM[Record[0]] = abs(int(Record[4].split('.')[0]))
        else:
            QRTA_NUM[Record[0]] += abs(int(Record[4].split('.')[0]))
df1=pd.DataFrame.from_dict(QRTA_NUM,orient='index')
df1.columns=['y']
df1=df1.reset_index()
df1=df1.reset_index(drop=True)
df1.columns=['ds', 'y']
print(df1)
df1.to_csv ("perdayvolume.csv" , index=True,header=True,encoding = "utf-8")
