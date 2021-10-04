#Finds the path of the maximum field scanning drone with genetic algorithm

import numpy as np
import random as ra
import matplotlib.pyplot as plt

x = 4 #popülasyon büyüklüğü

mu = 0.03 #mutasyon oranı

function = 2 #2 değerlendirme fonksiyonundan hangisinin seçildiği

g = 500 #jenerasyon sayısı

co = 2 #crossover kaç noktadan

m = 81 #maks gidilebilecek nokta 9*9

cgo = x/2 #eski jenerasyondan kopyalanacak birey sayısı

start = 0#3 farklı başlangıç için 0, 1, 2 olabilir
starts = [[0,8],[4,4],[4,8]]

gens = np.zeros(shape=(x,m))# bireylerin tutulacağı dizi
fitnessv = np.zeros(shape=(1,x))#fitness fonksiyonu sonuçlarını tutan dizi

moves = [[0,0],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]] #[x,y]

for i in range(0,x): #ilk jenerasyon
    cond=1
    while cond == 1:#drone başladığı yerde bitirene kadar random ata
        k = starts[start][1] #y ekseninde bulunulan nokta
        l = starts[start][0] #x ekseninde bulunulan nokta
        for j in range(0,m):
            gens[i][j] = ra.randint(1,8)
            while ((k + moves[int(gens[i][j])][1])>8) or ((k + moves[int(gens[i][j])][1])<0) or ((l + moves[int(gens[i][j])][0])<0) or ((l + moves[int(gens[i][j])][0])>8): #alan dışına çıkmama kontrolü
                gens[i][j] = ra.randint(1,8)#random jenerasyonları oluşturma
            k = k + moves[int(gens[i][j])][1]
            l = l + moves[int(gens[i][j])][0]
        if abs(k-starts[start][1])>abs(l-starts[start][0]):#başlangıca uzaklık
            distToStart = abs(k-starts[start][1])
        else:
            distToStart = abs(l-starts[start][0])
        if distToStart == 0:#başladığı yerde bitiyor mu kontrolü eğer bitmiyorsa tekrar random atama yap
            cond = 0

passfield = [] #jenerasyonlar ilerledikçe taranan alanın değişimi
bestFitness = []# her jenerasyondaki en iyi fitnesslar
meanFitness = []# her jenerasyondaki fitnessların ortalaması
time = []
x1 = []
y1 = []
x2 = []
y2 = []
maxGen = 0
#alanda rotayı çizdirme
for a in range(0,g):
    fitnessv = np.zeros(shape=(1,x))
    maxFit = 0
    sumpass =  0
    x2.clear()
    y2.clear()
    for i in range(0,x):
        k = starts[start][1] #y ekseninde bulunulan nokta
        l = starts[start][0] #x ekseninde bulunulan nokta
        field = np.zeros(shape=(9,9))
        field[starts[start][1]][starts[start][0]] = 1
        sumAng = 0
        x1.clear()  #alanın ekran gösterimini yapmak için
        y1.clear()  #alanın ekran gösterimini yapmak için
        x1.append(starts[start][0] + 1)#alanın ekran gösterimini yapmak için
        y1.append(8 - starts[start][1] + 1)#alanın ekran gösterimini yapmak için
        for j in range(0,m):
            while ((k + moves[int(gens[i][j])][1])>8) or ((k + moves[int(gens[i][j])][1])<0) or ((l + moves[int(gens[i][j])][0])<0) or ((l + moves[int(gens[i][j])][0])>8):
                gens[i][j] = ra.randint(1,8)#eğer alandan çıkma varsa alanın içine döndür
            k = k + moves[int(gens[i][j])][1]
            l = l + moves[int(gens[i][j])][0]
            field[k][l] = j + 1 #alanda şekli çizme
            x1.append(l + 1)  #alanın ekran gösterimini yapmak için
            y1.append(8-k + 1)#alanın ekran gösterimini yapmak için
            #min açı hesaplama
            if j>0:
                angDiff = abs(gens[i][j] - gens[i][j-1])
                if angDiff == 1 or angDiff == 7:#45 derece dönüş
                    sumAng = sumAng + (4-1) #45 derece 1birim sayılıyor, açı ne kadar az ise o kadar büyük değer eldesi için 4'ten çıkarılır
                elif angDiff == 2 or angDiff == 6:#90 derece dönüş
                    sumAng = sumAng + (4-2)
                elif angDiff == 3 or angDiff == 5:#135 derece dönüş
                    sumAng = sumAng + (4-3)
                else:                               #180 derece dönüş
                    sumAng = sumAng + (4-4)
        sumAng = (sumAng*100)/(m*4) #yapılan birim açılar toplamını yapılabilecek max birim açısına bölüp yüzdesini aldık
        x2.append(x1.copy())
        y2.append(y1.copy())
        #başlangıca yakınlık hesaplama(fitness için)
        if abs(k-8)>abs(l-0):#başlangıca uzaklık
            distToStart = abs(k-starts[start][1])
        else:
            distToStart = abs(l-starts[start][0])
        distToStart = ((8-distToStart)*100)/8 #uzaklık olan değer yakınlığın yüzdesi şeklinde değişmiş oldu
        #max taranan alan hesabı(fitness için)
        maxf = len(np.nonzero(field)[0])
        maxf = (maxf*100)/81 #jenerasyonun taradığı tam alanın tarayabileceği alana göre yüzdesi
        sumpass = sumpass + maxf
        print(field)
        print("\n")
        #fitness fonksiyonu
        if function == 1:
            fitnessv[0][i] = distToStart*0.4 + maxf*0.4 + sumAng*0.2 #fitness fonksiyonu
        else:
            fitnessv[0][i] = maxf*0.5 + sumAng*0.5
        #fitness fonksiyonu
        if fitnessv[0][i] > maxFit:
            maxFit = fitnessv[0][i]
            bestBx = x1.copy()#jenerasyonun en iyisi
            bestBy = y1.copy()#jenerasyonun en iyisi
        print(sumAng)
        print(distToStart)
        print(maxf)
        print(fitnessv)
    if maxFit > maxGen:
        maxGen = maxFit
        maxGenx = x2.copy()
        maxGeny = y2.copy()
        goatx = bestBx.copy()#tüm jenerasyonların en iyisi
        goaty = bestBy.copy()#tüm jenerasyonların en iyisi
    passfield.append(sumpass/x)
    bestFitness.append(maxFit)
    meanFitness.append(np.sum(fitnessv)/x)
    time.append(a)
    print(gens)
    fitPer = fitnessv*100/np.sum(fitnessv)#fitness fonksiyonlarının şans yüzdeleri
    #selection = np.zeros(shape=(1,100))
    selection = []
    print(fitPer)
    b = 0
    for i in range(0,x):
        for j in range(0,int(fitPer[0][i])):#fitness oranları kadar diziye koyulup rastgele seçim yapılacak
            selection.append(i)
        b = b + j
    print(selection)
    choosen = np.zeros(shape=(1,int(x/2)))#seçimlerin koyulacağı dizi
    if x > 1:
        choosen[0][0] = selection[ra.randint(0,len(selection)-1)]
    tmp = 1
    for i in range(1,int(x/2)):#crossover yapılacakların seçim işlemi
        temp = selection[ra.randint(0,len(selection)-1)]
        if temp in choosen[0]:
            while tmp == 1:
                temp = selection[ra.randint(0,len(selection)-1)]
                if temp in choosen[0]:
                    tmp = 1
                else:
                    choosen[0][i] = temp
                    tmp = 0
        else:
            choosen[0][i] = temp
    print(choosen)
    #crossover işlemi
    i = 0
    ng = np.zeros(shape=(x,m))#yeni jenerasyon
    while i < len(choosen[0]):
        if co == 1:
            ind = ra.randint(1,m-1)#crossover yapılacak nokta
            gen1 = gens[int(choosen[0][i])][:ind]
            if i+1 > len(choosen[0])-1:
                gen2 = gens[i*2][ind:]
                gen4 = gens[i*2][:ind]
            else:
                gen2 = gens[int(choosen[0][i+1])][ind:]
                gen4 = gens[int(choosen[0][i+1])][:ind]
            ng[i] = np.concatenate((gen1,gen2),axis=None)
            gen3 = gens[int(choosen[0][i])][ind:]
            ng[i+1] = np.concatenate((gen4,gen3),axis=None)
        elif co == 2:
            ind = ra.randint(1,int(m/2))#crossover yapılacak nokta
            gen1 = gens[int(choosen[0][i])][:ind]
            ind2 = ra.randint(ind + 1,m-1)#crossover yapılacak 2.nokta
            if i+1 > len(choosen[0])-1:
                gen2 = gens[i*2][ind:ind2]
                gen6 = gens[i*2][ind2:]
                gen4 = gens[i*2][:ind]
            else:
                gen2 = gens[int(choosen[0][i+1])][ind:ind2]
                gen6 = gens[int(choosen[0][i+1])][ind2:]
                gen4 = gens[int(choosen[0][i+1])][:ind]
            gen3 = gens[int(choosen[0][i])][ind:ind2]
            gen5 = gens[int(choosen[0][i])][ind2:]
            ng[i] = np.concatenate((gen1,gen2,gen5),axis=None)
            ng[i+1] = np.concatenate((gen4,gen3,gen6),axis=None)
        i = i + 2
    #crossover tamamlandı
    tmp = 1
    for i in range(1,int(x/2)):#eski nesilden yeni nesile geçecek bireylerin seçimi
        temp = selection[ra.randint(0,len(selection)-1)]
        if temp in choosen[0]:
            while tmp == 1:
                temp = selection[ra.randint(0,len(selection)-1)]
                if temp in choosen[0]:
                    tmp = 1
                else:
                    choosen[0][i] = temp
                    tmp = 0
        else:
            choosen[0][i] = temp
    print(choosen)
    for i in range(0,int(x/2)):
        ng[int(x/2)+i] = gens[int(choosen[0][i])]
    if x == 1:
        ng[0] = gens[0]
    #şimdi mutasyon
    for j in range(0,x):
        for i in range(0,int(m*mu)):
            ng[j][ra.randint(1,8)] = ra.randint(1,8) #mutasyon işlemi
    #mutasyon bitti
    gens = ng #yeni nesili jenerasyona ata
    print(gens)
    print("\n")

#ekran gösterimleri
for i in range(0,x):
    plt.plot(maxGenx[i],maxGeny[i],label = str(i) + ". birey")
plt.ylim(0,10)
plt.xlim(0,10)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('En iyi bireyin jenerasyonu')
plt.legend()
plt.show()

plt.plot(goatx,goaty,label = "en iyi birey")
plt.ylim(0,10)
plt.xlim(0,10)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('en iyi birey')
plt.legend()
plt.show()

plt.plot(time,passfield,label = "Jenerasyonun ortalama taradığı alan")
plt.ylim(0,100)
plt.xlim(0,g)
plt.xlabel('Kaçıncı jenerasyon')
plt.ylabel('Ortalama taranan alan')
plt.title('Taranan alanın değişimi')
plt.legend()
plt.show()

plt.plot(time,bestFitness,label = "En iyi bireyin fitness'ı")
plt.plot(time,meanFitness,label = "Jenerasyonun ortalama fitness'ı")
plt.ylim(0,100)
plt.xlim(0,g)
plt.xlabel('Kaçıncı jenerasyon')
plt.ylabel('Uygunluk yüzdesi')
plt.title('Fitness fonksiyonunun değişimi')
plt.legend()
plt.show()
