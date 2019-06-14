import pandas as pd
df =pd.read_csv('beixuandata.csv',index_col=0,header=0)
p = df.sort_values(by='b', axis=0,ascending=False).head(20)
print(p)
x=p.index

def save_result(re_na, QRTA, ISIR, VOLUME, top20):
    with open(re_na+'.txt', 'w') as fr:
        fr.writelines(['QRTA'+'\t'+str(QRTA)+'\n', 'ISIR'+'\t'+str(ISIR)+'\n', 'VOLUME'+'\t'+str(VOLUME)+'\n'])
        fr.write('TOP20')
        for i in top20:
            fr.write('\t')
            fr.write(i)
save_result("result",1614,2078,255003720,x)