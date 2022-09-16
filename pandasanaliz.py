import sqlite3
import pandas as pd
import os
os.system('cls' if os.name == 'nt' else 'clear')
import sys

print("""
    ###############################################
    # Coder: Cüneyt TANRISEVER                    #
    # Raf kodunu girip enter' basınız             #
    # Örnek= DEPO-kasa1                           #
    # Çıkmak için "ç" harfine basıp enterlayınız. #
    ###############################################""","\n")
os.system("del veritabani.db")
db = sqlite3.connect("veritabani.db")
cs = db.cursor()
cs.execute("create table urunler (raf_adi, urun_adi, adet)")
data = pd.read_excel("depo pro.xls","Depo")
df = pd.DataFrame(data)
#print(df["ÜRÜN KODU"])

df["ÜRÜN KODU"].fillna(method='ffill', inplace=True)
#print(df["ÜRÜN KODU"])
#print(df.columns.tolist())
kolonlar = df.columns.tolist()
kolonlar[kolonlar.index('Unnamed: 3')] = 'Depo0'
kolonlar[kolonlar.index('Unnamed: 5')] = 'Depo1'
kolonlar[kolonlar.index('Unnamed: 6')] = 'Depo2'
kolonlar[kolonlar.index('Unnamed: 7')] = 'Depo3'
kolonlar[kolonlar.index('Unnamed: 8')] = 'Depo4'
kolonlar[kolonlar.index('Unnamed: 9')] = 'Depo5'
kolonlar[kolonlar.index('Unnamed: 10')] = 'Depo6'
kolonlar[kolonlar.index('Unnamed: 11')] = 'Depo7'
kolonlar[kolonlar.index('Unnamed: 12')] = 'Depo8'
kolonlar[kolonlar.index('Unnamed: 13')] = 'Depo9'
kolonlar[kolonlar.index('Unnamed: 14')] = 'Depo10'
kolonlar[kolonlar.index('Unnamed: 15')] = 'Depo11'
kolonlar[kolonlar.index('Unnamed: 17')] = 'Depo12'
kolonlar[kolonlar.index('Unnamed: 18')] = 'Depo13'
kolonlar[kolonlar.index('Unnamed: 19')] = 'Depo14'
kolonlar[kolonlar.index('Unnamed: 20')] = 'Depo15'
kolonlar[kolonlar.index('Unnamed: 21')] = 'Depo16'
kolonlar[kolonlar.index('Unnamed: 22')] = 'Depo17'
df.columns = kolonlar
#print(df.columns)
#print(len(set(df["ÜRÜN KODU"])))

raflar=['Veri Analiz','Depo0','Depo1','Depo2','Depo3','Depo4','Depo5','Depo6','Depo7','Depo8','Depo9','Depo10','Depo11','Depo12','Depo13','Depo14','Depo15','Depo16','Depo17']
raf=[]
adet=[]
for i in raflar:
    for numara, row in df[[i,"ÜRÜN KODU"]][1:].iterrows():
        if (numara % 2 != 0):
            #print(row[i],"-------------------------------")
            #print(row["ÜRÜN KODU"])
            aa=row[i],row["ÜRÜN KODU"]
            raf.append(list(aa)) 
        else:
             adet.append(str(row[i]))
birles=[]
#print(raf)
for i in range (len(raf)):
    raf[i].append(str(adet[i]))
duzenlenmisdb=[]
#print(raf)
for i in range(len(raf)):
    if raf[i][0]=='0':
        pass
    else:
        if raf[i][2]=='0':
            pass
        else:
            duzenlenmisdb.append(raf[i])
#print(duzenlenmisdb)
for i in duzenlenmisdb:
    cs.execute("insert into urunler values (?, ?, ? )",(i[0],i[1],i[2]))
while 1:
    sor=input("Lütfen Raf adını giriniz = ")
    if sor =="ç":
        db.commit()
        db.close()
        sys.exit()
    else:
        sorgu="SELECT raf_adi, urun_adi, adet FROM urunler WHERE raf_adi = '"+sor+"';"
        cs.execute(sorgu)
        dataSet = cs.fetchall()
        print("KASA ADI | Ürün adı | Ürün Adedi\n")
        for  data in dataSet:
            print(str(data).replace("(","").replace(")","").replace("\'","").replace(",","   | "))
db.commit()
db.close()

