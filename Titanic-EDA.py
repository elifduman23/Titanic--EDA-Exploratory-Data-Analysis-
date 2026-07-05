import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None) # tüm kolonları gösterir
pd.set_option('display.max_rows', None) # tüm satırları gösterir
data=pd.read_csv("titanic.csv") 
names=data["Name"]
print(names)# yolcuların adlarını verir
print(data.head()) # ilk 5 satırı yazdırır
print(data.tail()) # son 5 satırı yazdırır
print(data.info()) #datasetteki kolonlar hakkında bilgi verir.
print(data.describe()) # her bir kolondaki verilerin sayısı,ortalaması,standart sapması gibi değerleri verir.
print(data.count()) #her bir kolonda kaç veri varsa sayar
print(data.isna()) #boş olan datalarda true değerini döndürür
print(data.dropna()) #en az bir satırda boş olan dataları almıyor, tamamı dolu olan dataları alıyor.
print(data.dropna(axis=1)) # kolonlara bakıyor kolonda boş data yoksa o kolonu alıyor.
print(data.fillna(20)) #boş olan dataları 20 ile dolduruyor
print(data.drop("Sex",axis=1).head()) #cinsiyet kolonunu siliyor.
print(data["Pclass"].mean()) # yolculuk edenlerin seçtiğin yolculuk sınıfının ortalaması
print(data["Age"].mean()) #yolcuların yaş ortalaması
print(data["Survived"].mean()) #yolcuların hayatta kalma ortalaması
print(data["Age"].median()) #yolcuların yaşlarının medyanını buluyor.
print(data["Fare"].median()) #yolcuların ödedikleri ücretin medyanını buluyor.
print(data["Age"].max()) #en büyük yolcunun yaşını bulur.
print(data["Age"].min()) #en küçük yolcunun yaşını bulur
print((data["Sex"] != "male").head()) #kadınlara true erkeklere false yazar.
print(data.loc[1]) #index i 1 olan datayı yazar
data_groupby=data.groupby('Sex')
print(data_groupby.count()) #cinsiyete göre gruplandırır
