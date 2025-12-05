# Temel İşlemler

import pandas as pd

# pandas serisi oluşturma

seri=pd.Series([1,2,3,4,5])

# numpy arrayi üzerinden seri oluşturma

a=np.array([1,2,3,4,5])
seri=pd.Series(a)

# iki seriyi birleştirme

pd.concat([seri1,seri2])

# serilerde eleman işlemleri

seri=pd.Series([121,200,150,99],index=["reg","loj","cart","rf"])

seri.index
seri.keys
list(seri.items)
seri.values

# dataframe oluşturma

p=[1,2,3,4,5]
pd.DataFrame(p.columns=['degisken_ismi'])

# dataframe eleman işlemleri

df.drop(‘a’,axis=0,inplace=True) # Kalıcı olarak silme işlemi
df[‘var’] is df[‘var1’] # aynı mı diye sorar ve bool döner

# listeleme

df.loc[0:3]