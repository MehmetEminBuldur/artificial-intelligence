import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
inpa1 = [0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1]
inpb1 = [1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0]
inpc1 = [0,0,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0]
inpd1 = [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0]
inpe1 = [1, 1,  1,  1,  1,  1,  1, 0, 1, 0, 0, 0, 0,  1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0,  1, 0, 0, 0, 0, 1,  1,  1, 0, 0, 0, 0, 1, 0,  1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,  1, 1, 1,  1,  1,  1,  1,  1]
inpj1 = [0,0,0,1,1,1,1, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,1,0,0,0,1,0, 0,1,0,0,0,1,0, 0,0,1,1,1,0,0]
inpk1 = [1,1,1,0,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1]
inpa2 = [0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0]
inpb2 = [1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0]
inpc2 = [0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0]
inpd2 = [1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,1,0,0]
inpe2 = [1,1,1,1,1,1,1, 1,0,0,0,0,0,0, 1,0,0,0,0,0,0, 1,0,0,0,0,0,0, 1,1,1,1,1,0,0, 1,0,0,0,0,0,0, 1,0,0,0,0,0,0, 1,0,0,0,0,0,0, 1,1,1,1,1,1,1]
inpj2 = [0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,0,0,0,0,1,0, 0,1,0,0,0,1,0, 0,1,0,0,0,1,0, 0,0,1,1,1,0,0]
inpk2 = [1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0]
inpa3 = [0,0,0,1,0,0,0, 0,0,0,1,0,0,0, 0,0,1,0,1,0,0, 0,0,1,0,1,0,0, 0,1,0,0,0,1,0, 0,1,1,1,1,1,0, 1,0,0,0,0,0,1, 1,0,0,0,0,0,1, 1,1,0,0,0,1,1]
inpb3 = [1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,1,1,1,0]
inpc3 = [0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,1,0,0]
inpd3 = [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0]
inpe3 = [1,1,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1,1,1]
inpj3 = [0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0]
inpk3 = [1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1]
oneepo = [ inpa1, inpb1, inpc1, inpd1, inpe1, inpj1, inpk1, inpa2, inpb2, inpc2, inpd2, inpe2, inpj2, inpk2, inpa3, inpb3, inpc3, inpd3, inpe3, inpj3, inpk3]
weighta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weightb = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weightc = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weightd = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weighte = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weightj = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weightk = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
weights = [weighta,weightb,weightc,weightd,weighte,weightj,weightk]#ağırlık matrisi implementasyonu
targeta = [1,0,0,0,0,0,0]
targetb = [0,1,0,0,0,0,0]
targetc = [0,0,1,0,0,0,0]
targetd = [0,0,0,1,0,0,0]
targete = [0,0,0,0,1,0,0]
targetj = [0,0,0,0,0,1,0]
targetk = [0,0,0,0,0,0,1]
target = [targeta,targetb,targetc,targetd,targete,targetj,targetk]
count7 = 0#target dizisinde index olarak kullanmak için
lrate = 0.01
epoch = 1000
bias = [1,1,1,1,1,1,1]
biasw = [0,0,0,0,0,0,0]
accuracy = 0
c = 0 #epoch sayısı için index

while c < epoch and accuracy < 100 : #1000 epoch
    c = c + 1
    correct = 0
    wrong = 0
    for arr in oneepo: #1 epochun tamamlanması
        net = [0,0,0,0,0,0,0] #outputları hesaplamak için
        for i in range(0,63): #ağırlıklarla 63 inputu çerpıp toplama işlemi
            for j in range(0,7):
                net[j] = net[j] + arr[i] * weights[j][i]
        for k in range(0,7):
            net[k] = net[k] + bias[k] * biasw[k]

        #print("output  " + str(net))
        #print("target  " + str(target[count7]))

        for i in range(0,7):
            net[i] = sigmoid(net[i])#aktivasyon fonksiyonu
            net[i] = round(net[i])

        if net == target[count7]: #eğer target ve output uyuşuyorsa değişiklik yapma
            correct = correct + 1
            #print("eşitlik")
        else:
            print("output  " + str(net))
            print("target  " + str(target[count7]))
            wrong = wrong + 1
            for y in range(0,7):
                for x in range(0,63):#target ve net değer uyuşmuyorsa ağırlıkları güncelle
                    weights[y][x] = weights[y][x] + lrate * (target[count7][y] - net[y]) * arr[x] #DELTA KURALI
                biasw[y] = biasw[y] + lrate * (target[count7][y] - net[y])                        #DELTA KURALI

        count7 = count7 + 1
        if count7 == 7:     #target'a doğru şekilde erişmek için değişken çünkü her 7 tekrarda aynı harf geliyor
            count7 = 0      #

    print(str(c) + ".epoch")
    accuracy = (correct/(wrong + correct))*100
    print("tutarlılık = " + str(accuracy) + "% \n \n ")

print("işlem tamamlandı   epoch sayıs = " + str(c))
while 1:
    tname = input("test dosyasının ismini şu formatta giriniz ---> (Font_1_A.txt)   (ÇIKMAK İÇİN e GİRİNİZ):")
    f = open(tname)
    inpt = f.read()
    i = 0
    j = 0
    testarr = inpa1
    while inpt[i] != "\n" and i < 1000:
        if inpt[i] == " " or inpt[i] == ",":
             i = i + 1
        elif inpt[i] == "1":
            testarr[j] = 1
            j = j + 1
            i = i + 1
        elif inpt[i] == "-":
            testarr[j] = -1
            j = j + 1
            i = i + 2
        elif inpt[i] == "0":
            testarr[j] = 0
            j = j + 1
            i = i + 1

    f.close()
    net = [0,0,0,0,0,0,0]
    for i in range(0,63): #ağırlıklarla 63 inputu çerpıp toplama işlemi TEST İÇİN
        for j in range(0,7):
            net[j] = net[j] + testarr[i] * weights[j][i]
    for k in range(0,7):
        net[k] = net[k] + bias[k] * biasw[k]

    for i in range(0,7): #binary sigmoid
        net[i] = sigmoid(net[i])
        net[i] = round(net[i])

    print(str(net))

    if net == target[6]:# SONUÇ YAZDIRMA
        print("verilen input K harfine ait")
    elif net == target[5]:
        print("verilen input J harfine ait")
    elif net == target[4]:
        print("verilen input E harfine ait")
    elif net == target[3]:
        print("verilen input D harfine ait")
    elif net == target[2]:
        print("verilen input C harfine ait")
    elif net == target[1]:
        print("verilen input B harfine ait")
    elif net == target[0]:
        print("verilen input A harfine ait")
    else:
        print("hatalı sonuç")
