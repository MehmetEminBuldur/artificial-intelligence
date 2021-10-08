#scraping data from website for home price estimation app

#Veri kümesinin hazırlandığı kod parçası
import requests
from bs4 import BeautifulSoup as bs

#İst,beylikdüzü,barış mah. deki 3+1 dairelerin listesi
with open('homefeats.txt', 'w') as f:
    f.write("")
for i in range(0,13):
    site = 'https://www.hepsiemlak.com/beylikduzu-satilik/daire-3-1?districts=beylikduzu-baris,adnan-kahveci&page='+ str(i + 1)

    headers = {'User-Agent' : ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')}
    re = requests.get(site, headers = headers)
    if re.status_code != 200:
        print('sıkıntı var')
        print(re.status_code)
    else:
        so = bs(re.content,'html.parser')
        homes = so.find("div",{"class":"listView"}).find_all('div',{"class":"listing-item"})

        for no,home in enumerate(homes,1):
            link = home.find('a',{"class":"card-link"}).get('href')
            #print(str(i*24 + no) + str(link))
            nsite = "https://www.hepsiemlak.com" + link
            #print(nsite)
            req = requests.get(nsite, headers = headers)
            if re.status_code != 200:
                print('sıkıntı var')
            else:
                sou = bs(req.content,'html.parser')
                features = sou.find("div",{"class":"spec-groups"}).find_all('li')#find_all('ul',{"class":"adv-info-list"})
                print(features)
                if no == 1 and i == 0:
                    with open('homefeats.txt','w') as f:
                        count = 0
                        for feat in features:
                            x = feat.find("span","txt").get_text(strip = True)
                            if  x == 'Brüt / Net M2' or x == 'Bulunduğu Kat' or x == 'Bina Yaşı' or x == 'Isınma Tipi' or x == 'Eşya Durumu' or x == 'Krediye Uygunluk' or x == 'Banyo Sayısı' or x == 'Tapu Durumu' or x == 'Aidat' or x == 'Site İçerisinde':
                                f.write(feat.find("span",{"class":"txt"}).get_text(strip = True))
                                f.write(',')
                                count = count + 1
                        f.write(str(count))
                        f.write("\n")
                temp = 'asd'
                with open('homefeats.txt', 'a') as f:
                    count = 0
                    for feat in features:
                        x = feat.find("span","txt").get_text(strip = True)
                        if  x == 'Brüt / Net M2' or x == 'Bulunduğu Kat' or x == 'Bina Yaşı' or x == 'Isınma Tipi' or x == 'Eşya Durumu' or x == 'Krediye Uygunluk' or x == 'Banyo Sayısı' or x == 'Tapu Durumu' or x == 'Aidat' or x == 'Site İçerisinde':
                            if (temp == 'Banyo Sayısı' and x != 'Tapu Durumu') or (temp == 'Tapu Durumu' and x != 'Aidat') or(temp == 'Aidat' and x != 'Site İçerisinde'):
                                if temp == 'Tapu Durumu':
                                    f.write("100 TL,")
                                    count = count + 1
                                else:
                                    f.write("0,")
                                    count = count + 1
                            f.write(feat.find("span","").get_text(strip = True))
                            f.write(",")
                            temp = x
                            count = count + 1
                    if count < 10:
                        f.write("0,")
                        count = count + 1
                    f.write(sou.find("p",{"class":"fontRB fz24 price"}).get_text(strip = True))
                    f.write("," + str(count))
                    f.write("\n")

#VERİ ÜZERİNDE ÇEŞİTLİ DÜZENLEMELER YAPILIP ÖZELLİKLERİ DÜZENLEME İŞLEMLERİ
df = pd.read_csv("homefeats.txt")

print(len(df))
for i in range(0,len(df)):
    if math.isnan(df["featno"][i]):
        print(df["featno"][i])
        df.drop([i], axis = 0, inplace = True)
for i in range(0,len(df)):
    print(df.iloc[i,:])
print(df)

df.drop('featno', axis = 1, inplace = True)

print(df.info())

print(df.iloc[0,:])
for i in range(0,len(df)):

    x = df.iloc[i,0].split(" ")[0]
    df.iloc[i,0] = x

    if df.iloc[i,1][0] == "Y" or df.iloc[i,1][0] == "B" or df.iloc[i,1][0] == "G":
        df.iloc[i,1] = 0
    else:
        x = df.iloc[i,1].split(" ")[0]
        df.iloc[i,1] = x

    if df.iloc[i,2][0] =="S":
        df.iloc[i,2] = 0
    else:
        x = df.iloc[i,2].split(" ")[0]
        df.iloc[i,2] = x

    if df.iloc[i,3][0] == "K":
        df.iloc[i,3] = "0,1"
    else:
        df.iloc[i,3] = "1,0"

    if df.iloc[i,4] == "Uygun":
        df.iloc[i,4] = "0,1"
    else:
        df.iloc[i,4] = "1,0"

    if len(df.iloc[i,5]) > 7:
        df.iloc[i,5] = "0,1"
    else:
        df.iloc[i,5] = "1,0"

    if df.iloc[i,7] != "0" and df.iloc[i,7].split(" ")[1][0] == "M":
        df.iloc[i,7] = "0,1"
    else:
        df.iloc[i,7] = "1,0"

    x = df.iloc[i,8].split(" ")[0]
    df.iloc[i,8] = x

    if (df.iloc[i,9][0] == "H" and df.iloc[i,9][5] == "r" ) or df.iloc[i,9] == "0":
        df.iloc[i,9] = "0,1"
    else:
        df.iloc[i,9] = "1,0"

    x = df.iloc[i,10].split(" ")[0]
    df.iloc[i,10] = x
    print(df.iloc[i,10])
    if len(df.iloc[i,10].split(".")) < 3:
        x = df.iloc[i,10].split(".")[0] + df.iloc[i,10].split(".")[1]
        df.iloc[i,10] = x
    else:
        x = df.iloc[i,10].split(".")[0] + df.iloc[i,10].split(".")[1] + df.iloc[i,10].split(".")[2]
        df.iloc[i,10] = x
df["M2"] = pd.to_numeric(df["M2"])
df["Bulundugu Kat"] = pd.to_numeric(df["Bulundugu Kat"], downcast = 'integer')
print(df)
#df = df.apply(pd.to_numeric)
print(df.info())

np.savetxt(r'np.txt', df.values, fmt='%s', delimiter=',')
