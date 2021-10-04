#Home price estimation app using 10 different features and 5 different estimator models


# encoding:utf-8
import pandas as pd #dataframe için
import math
import numpy as np #dizi ve matematik işlemleri için
from sklearn.datasets import make_regression #regresyon için
from sklearn.linear_model import LinearRegression#lineer regresyon için
from sklearn.model_selection import KFold, train_test_split, cross_val_predict, cross_val_score#çapraz geçerleme için
from sklearn import metrics #modellerin başarısını ölçmek için
import matplotlib.pyplot as plt #ekran gösterimleri için
from sklearn.tree import DecisionTreeRegressor #desicion tree tahminleyicisi için
from sklearn.preprocessing import PolynomialFeatures #polynomial regresyon için
from sklearn.ensemble import RandomForestRegressor #random forest için
from sklearn.preprocessing import StandardScaler #support vector regresyon için
from sklearn.svm import SVR #support vector regresyon için
from sklearn.datasets import make_classification #özellik seçimi için
from sklearn.feature_selection import SelectKBest #özellik seçimi için
from sklearn.feature_selection import f_classif #özellik seçimi için
from sklearn.decomposition import PCA #özellik dönüşümü için
from sklearn import preprocessing

#mkare,kat,yas,isi1,isi2,kr1,kr2,es1,es2,banyo,tapu1,tapu2,aidat,site1,site2,fiyat   --- özellikler

def scoreResults(model, x_train, x_test, y_train, y_test):#model başarısını ölçmek için fonksiyon

    y_train_predict = model.predict(x_train)
    y_test_predict = model.predict(x_test)

    r2_train = metrics.r2_score(y_train, y_train_predict)
    r2_test = metrics.r2_score(y_test, y_test_predict)

    mse_train = metrics.mean_squared_error(y_train, y_train_predict)
    mse_test = metrics.mean_squared_error(y_test, y_test_predict)

    return [r2_train, r2_test, mse_train, mse_test]

df = pd.read_csv("np.txt")#hazırlanmış veri setini dataframe'e çekme

option = 1#5 farklı tahminleyici için 5 farklı seçenek 1-lineer 2-polynomial 3-desicion tree 4-random forest 5-support vector

print(df)
print(df.info())
features = df.iloc[:,0:15] #örnekler, özellikler
target = df.iloc[:,15:16] #hedefler, fiyat bilgisi
if option == 2:
    target = df["fiyat"]

print(features)
print(target)
#k-cross validation yapmadan önce sadece lineer regresyonla nasıl sonuç veriyor ona bakalım
x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle = False, random_state = 0)
veri_kesitleri = {"x_train"  : x_train, "x_test"  : x_test, "y_train" : y_train, "y_test"  : y_test}

for i in veri_kesitleri:#eğitim ve test verisi kaç örnekten oluşuyor
    print(f"{i}: satır sayısı {veri_kesitleri.get(i).shape[0]}")

lr = LinearRegression()#modelin lr ye atanması
lr.fit(x_train,y_train)#model eğitimi

tahmin = lr.predict(x_test) #tahminleme işlemi

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.ylim(0,2000000)##tahminlerle gerçek fiyatın karşılaştırılması grafiğini ekrana basma
plt.xlabel('index')
plt.ylabel('fiyat x1.000.000')
a = [t for t in range(1,53,1)]
plt.plot(a,y_test, label = "gerçek fiyat")
plt.plot(a,tahmin, label = "tahmin fiyatı")
plt.legend()
plt.show()

result_lr = scoreResults(model = lr, x_train = x_train, x_test = x_test, y_train = y_train, y_test = y_test)#sonuçların kaydı

print(f"Train R2 Score: {result_lr[0]:.4f} MSE: {result_lr[2]:.4f}")#sonuçların ekrana basılması
print(f"Test R2 Score: {result_lr[1]:9.4f} MSE: {result_lr[3]:.4f}")

os = 0 #özellik seçimi parametresi
od = 0 #özellik dönüşümü parametresi
nor = 0 #normalizasyon parametresi
"""
###özellik seçimi
fs = SelectKBest(score_func=f_classif, k=2)# k seçilecek özellik sayısı. arttıkça performans artar
features = fs.fit_transform(features, np.ravel(target))
target = np.ravel(target)
print(features.shape)
os = 1
###özellik seçimi
"""
"""
###özellik dönüşümü
features = StandardScaler().fit_transform(features)
pca = PCA(n_components=3)
features = pca.fit_transform(features)
target = np.ravel(target)
od = 1
###
"""

###normalizasyon
features[['mkare','kat','yas']] = preprocessing.minmax_scale(features[['mkare','kat','yas']])
#target = np.ravel(target)
nor = 1
###


scores = []#sonuçlar dizisi
#####modellerin hazırlanması
lr_cv = LinearRegression()
poly = PolynomialFeatures(degree=3)#2,3,4,5... yapılabilir derece arttıkça başarı artar
feat_poly = poly.fit_transform(features)
dtr = DecisionTreeRegressor(random_state=0)
rfg = RandomForestRegressor(n_estimators=10,random_state=0)#n_estimators desicion tree sayısını belirtir
if option == 5:
    sc_feat = StandardScaler()
    feat_scale = sc_feat.fit_transform(features)
    sc_target = StandardScaler()
    target_scale = sc_target.fit_transform(target)
    svr_reg = SVR(kernel = 'rbf')
#####
k = 10#çapraz geçerlemenin 10 katlı olacağı bilgisi
iter = 1
cv = KFold(n_splits=k, shuffle=False)#çapraz geçerleme
if option == 2:#polynomial regresyon için özellik ayarlaması
    features = feat_poly
elif option == 5:#support vector için özellik ayarlaması
    features = feat_scale
    target = target_scale
for train_index, test_index in cv.split(features):# verilerin 10 katlı çapraz geçerlemeye göre bölünüp sınanması
    if (option == 1 or option == 3 or option == 4) and os == 0 and od == 0:
        x_train, x_test, y_train, y_test = features.iloc[train_index], features.iloc[test_index], target.iloc[train_index], target.iloc[test_index]
    elif option == 5 or option ==2 or os == 1 or od == 1:
        x_train, x_test, y_train, y_test = features[train_index], features[test_index], target[train_index], target[test_index]

    if option == 5 or option == 4:#support vector için veri düzenlemesi
        y_train = np.ravel(y_train)

    ####model eğitimleri
    lr_cv.fit(x_train, y_train)

    dtr.fit(x_train, y_train)

    if option == 4:
        rfg.fit(x_train,y_train)
    if option == 5:
        svr_reg.fit(x_train,y_train)
    ####

    if option == 1 or option == 2:#tahminleyiciye göre sonuçların kaydı
        result = scoreResults(model = lr_cv, x_train = x_train, x_test = x_test, y_train = y_train, y_test = y_test)
    elif option == 3:
        result = scoreResults(model = dtr, x_train = x_train, x_test = x_test, y_train = y_train, y_test = y_test)
    elif option == 4:
        result = scoreResults(model = rfg, x_train = x_train, x_test = x_test, y_train = y_train, y_test = y_test)
    elif option == 5:
        result = scoreResults(model = svr_reg, x_train = x_train, x_test = x_test, y_train = y_train, y_test = y_test)
    result =  [abs(ele) for ele in result]

    print(f"{iter}. veri kesiti")
    print(f"Train R2 Score:  {result[0]:.4f} MSE: {result[2]:.4f}")
    print(f"Test R2 Score:{result[1]:9.4f} MSE: {result[3]:.4f}\n")
    iter += 1
    if option == 1:#testlerin skor listesi grafik olarak ekrana basmak için
        scores.append(abs(lr_cv.score(x_test, y_test)))
    elif option == 2:
        scores.append(abs(lr_cv.score(x_train, y_train)))
    elif option == 3:
        scores.append(abs(dtr.score(x_test, y_test)))
    elif option == 4:
        scores.append(abs(rfg.score(x_test, y_test)))
    elif option == 5:
        scores.append(abs(svr_reg.score(x_test, y_test)))

b = [t for t in range(1,k+1,1)]#kaçıncı veri parçası dizisi
x_pos = np.arange(len(b))####veri parçalarındaki başarıların skorlarının grafiğinin ekrana basılması
plt.bar(x_pos, scores, color=(0.2, 0.4, 0.6, 0.6))
plt.ylim(0,1)
plt.xlabel('veri parçaları')
plt.ylabel('R2 Skoru')
plt.xticks(x_pos, b)
plt.show()
print(scores)
