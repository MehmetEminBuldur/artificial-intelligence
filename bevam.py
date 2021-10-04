import pandas as pd
import numpy as np
from efficient_apriori import apriori
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
#AÇILIŞ PENCERESİ-LOG DOSYASI İSMİ ALIMI
froot = tk.Tk()
fcanvas = tk.Canvas(froot, height = 500, width = 500, bg = "#260D39")
fcanvas.pack(fill=tk.BOTH,expand=True)
frame = tk.Frame(froot, bg = "cyan")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
titl = froot.title("Log Analizi Uygulamasi")
labe = Label(frame, text="Mevcut Log Dosyalari ve Isimleri\n1log20170630.txt\n2log20170630.txt\n3log20170630.txt",font="20" ,fg="black", bg="white")
labe.pack()
l1 = Label(frame, text="Log Dosyasi Ismini Giriniz", fg="black",bg="cyan")
l1.pack(side=tk.LEFT)
def ental():
    dosya = open("default.txt","w")
    docName = ent.get()
    dosya.write(docName)
    froot.destroy()

ent = Entry(frame)
ent.pack(side=tk.LEFT)
entbut = Button(frame,text = "SUBMIT", command=ental)
entbut.pack(side=tk.RIGHT)
froot.mainloop()
#
#UYARI EKRANI
wroot = tk.Tk()
wcanvas = tk.Canvas(wroot, height=300, width=300, bg="#212A43")
wcanvas.pack(fill=tk.BOTH,expand=True)
l2 = tk.Label(wcanvas, text="UYARI:Islem yaklasik 5-10 saniye surecektir,tamam'a bastiktan sonra pencerenin gelmesini bekleyiniz\n\nUyariyi okuduktan sonra tamam'a basiniz." )
l2.pack()
tit1 = wroot.title("Uyari Ekrani")
endbut = Button(wroot,text = "TAMAM", command=lambda: wroot.destroy())
endbut.pack()
wroot.mainloop()
#
#DOSYADAN VERİYİ OKUYUP DATAFRAME OLARAK TUTMA İŞLEMİ
fn = open("default.txt","r")
docName = fn.readline()
df = pd.read_table(docName,sep = ",",usecols = [0,2,4,5,6,7,8,9,12])
fordate = pd.read_table(docName,nrows=2,sep=",",usecols=[1])
#
#SESSİONLARI AYIRMA İŞLEMİ
i = 1
userintervals = []       #sessionlari tutar
start = 0
stop = 0
while i < len(df.index): #iplere göre sessionlari ayırır
    ip1 = df.iloc[i-1,0]
    ip2 = df.iloc[i,0]
    if ip1 == ip2:
        i = i + 1
    else:
        stop = i - 1
        userintervals.append(df.loc[start:stop])
        start = i
        i = i + 1
#
#ANA EKRAN-TEMEL BİLGİLER-BUTONLAR
root = tk.Tk()
root.attributes('-fullscreen', True) # make main window full-screen
canvas = tk.Canvas(root, height = 100, width = 1000, bg = "#260D39")
canvas.pack(fill=tk.BOTH, expand=True)
tit = root.title("Log Analizi Uygulamasi")
label1 = Label(canvas, text="TOPLAM ERISIM SAYISI:  " + str(len(df.index)),font="25",height=2,width=50,fg="white", bg="#260D39")
label1.pack(fill=tk.BOTH,expand=True)
label2 = Label(canvas, text="TOPLAM ERISIM SESSION'I SAYISI:  " + str(len(userintervals)),font="25",height=2,width=50,fg="white", bg="#260D39")
label2.pack(fill=tk.BOTH,expand=True)
label3 = Label(canvas, text="TARIH:  " + fordate.iloc[0,0],font="25",height=2,width=50,fg="white", bg="#260D39")
label3.pack(fill=tk.BOTH,expand=True)
label4 = Label(canvas, text="SAAT ARALIGI:  " + df.iloc[0,1] + "--" +df.iloc[-1,1],font="25",height=2,width=50,fg="white", bg="#260D39")
label4.pack(fill=tk.BOTH,expand=True)

def docTypeCount():#DOKUMAN TİPLERİ VE KULLANIM SIKLIKLARI BULMA İŞLEMİ
    filetype = []              # kullanılan farklı dosya tipleri ve kaç defa kullanıldıklarını tutan liste
    fname = []
    i = 0
    j = 0
    docount = []
    while i < len(df.index):#DOSYA TİPLERİ İŞLEMLERİ
        fname = df.iloc[i,4]   # file type fname
        fname = fname.split('.') #noktaya göre ayır
        uzanti = fname[-1] #son elemanı uzanti değişkenine atama
        if uzanti in filetype:
            j = filetype.index(uzanti)
            docount[j] = docount[j] + 1
        else:
            filetype.append(uzanti)
            docount.append(1)
        i = i + 1
    tlist = []
    hmdtfu = len(filetype)#kaç farklı dosya tipi kullanıldı
    for i in range(0,hmdtfu):#doküman tipi ile sayısını listede eşleştirme
        tlist.append([docount[i],filetype[i]])
    tlist.sort(reverse=True)

    root1 = tk.Tk()
    canvas1 = tk.Canvas(root1, height = 500, width = 1000, bg = "#260D39")
    canvas1.pack(fill=tk.BOTH, expand=True)
    title1 = root1.title("Dokuman Tipleri ve Kullanim Sayilari")
    label6 = Label(canvas1,text="En Fazla Kullanilan Dokuman Tipi:  " + tlist[0][1] + "\n\nKac Farklı Dokuman Tipi Kullanıldı:  " + str(hmdtfu)+"\n\nKullanim Sayilari--Dokuman Tipleri",fg="white",bg="#260D39",font="20",width=100)
    label6.pack(fill=tk.BOTH,expand=True)
    for elm in tlist:
        label5 = Label(canvas1,text=str(elm[0]) + " -- " + elm[1],fg="white",bg="#260D39",font="20",width=100)
        label5.pack(fill=tk.BOTH,expand=True)
    def grafik():
        plt.figure(figsize=(14,8))
        plt.title("Dokumanlar ve Kullanim Sayilari")
        plt.plot(filetype,docount)
        plt.show()
    button1 = tk.Button(canvas1, text="GRAFIK",command=grafik,padx=10,pady=10)
    button1.pack()
    def venschem():
        fig1, ax1 = plt.subplots()
        plt.title("Dokumanlarin Kullanim Sayilari Pasta Diyagrami\nDaha Ayrintili Gormek Icın Zoom Yapabilirsiniz")
        ax1.pie(docount, labels=filetype, autopct='%1.3f%%',shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()
    button2 = tk.Button(canvas1, text="PASTA DIYAGRAMI",command=venschem,padx=10,pady=10)
    button2.pack()
    root1.mainloop()

def docByte():#KULLANILAN-ERİŞİLEN TOPLAM DOKÜMAN BOYUTU BULMA İŞLEMİ
    sum = 0.0
    i = 0
    while i < len(df.index):#DOSYA BOYUTU
        sum = sum + df.iloc[i,6] #byte cinsinden dosya boyut toplamı
        i = i + 1
    fkbyte = round(sum/1024,3)
    fmbyte = round(sum/(1024*1024),3)
    fgbyte = round(sum/(1024*1024*1024),3)

    root2 = tk.Tk()
    title2 = root2.title("Toplam Dokuman Boyutu")
    canvas2 = tk.Canvas(root2, height = 500, width = 1000, bg = "#260D39")
    canvas2.pack(fill=tk.BOTH, expand=True)
    label8 = Label(canvas2,text="\nErisilen Toplam Dosya Boyutu\n" + str(sum) + " BYTE\n" + str(fkbyte) + " KBYTE\n" + str(fmbyte) + "MBYTE\n" + str(fgbyte) + " GBYTE",fg="white",bg="#260D39",font="30",height=30,width=100)
    label8.pack(fill=tk.BOTH,expand=True)
    root2.mainloop()

def accCodes():#ERİŞİM KODLARI VE BU KODLARI ETİKETLEME İŞLEMİ
    accodel = [] #access code list
    codc = [] #access code count
    for i in range(0,len(df.index)):#ERİŞİM KODLARI (HATALI VEYA BAŞARILI)
        acode = str(df.iloc[i,5])#
        if acode in accodel:
            j = accodel.index(acode)
            codc[j] = codc[j] + 1
        else:
            accodel.append(acode)
            codc.append(1)
        i = i + 1
    clist = []
    csuccessful = 0 #başarılı erişim sayacı
    cerror = 0 #hatalı erişim sayacı
    for i in range(0,len(accodel)):#code ile gerçekleşme sayısını listede eşleştirme
        if int(float(accodel[i])/100) == 2:
            csuccessful = csuccessful + codc[i]
            clist.append([accodel[i],codc[i],"successful"])
        elif int(float(accodel[i])/100) == 3:
            csuccessful = csuccessful + codc[i]
            clist.append([accodel[i],codc[i],"redirection"])
        elif int(float(accodel[i])/100) == 4:
            cerror = cerror + codc[i]
            clist.append([accodel[i],codc[i],"client error"])
        elif int(float(accodel[i])/100) == 5:
            cerror = cerror + codc[i]
            clist.append([accodel[i],codc[i],"server error"])
        else:
            clist.append([accodel[i],codc[i],"undefind"])
    root3 = tk.Tk()
    title3 = root3.title("Durum Kodlari")
    canvas3 = tk.Canvas(root3, height = 500, width = 1000, bg = "#260D39")
    canvas3.pack(fill=tk.BOTH, expand=True)
    label7 = Label(canvas3, text="\nBasarili Erisim Sayisi: " + str(csuccessful) +"\n\nHatali Erisim Sayisi: " + str(cerror) + "\n\nErisim Kodlari--Meydana Gelme Sayisi--Olay Turu",font="25",width=100,fg="white", bg="#260D39")
    label7.pack(fill=tk.BOTH,expand=True)
    for asd in clist:
        label9 = Label(canvas3,text=str(asd[0]) + " -- " + str(asd[1]) + " -- " + asd[2],fg="white",bg="#260D39",font="25",width=100)
        label9.pack(fill=tk.BOTH,expand=True)
    def venschem1():
        plt.title("Durum Kodlari Pasta Diyagrami")
        plt.pie(codc, labels=accodel, autopct='%1.3f%%',shadow=True)
        centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.axis('equal')
        plt.show()
    button3 = Button(canvas3,text="PASTA DIYAGRAMI",padx=20,pady=20,command=venschem1)
    button3.pack()
    def histo2():
        plt.figure(figsize=(10,6))
        plt.title("Durum Kodlari ve Meydana Gelme Sikliklari")
        plt.plot(accodel,codc)
        plt.show()
    button5 = Button(canvas3,text="GRAFIK",padx=20,pady=20,command=histo2)
    button5.pack()
    root3.mainloop()

def accTimeInt():#ZAMAN ARALIKLARI VE YOĞUNLUKLARI BULMA İŞLEMİ
    timeinterval = []
    fcount = []

    timeinterval.append(int((df.iloc[0,1])[3:5]))
    fcount.append(1)
    for i in range(1,len(df.index)):#en yoğun erişim olan dakikayı bulma işlemi
        time = df.iloc[i-1,1]
        ominute = time[3:5]
        ominute = int(ominute)
        time = df.iloc[i,1]
        minute = time[3:5]
        minute = int(minute)
        if minute == ominute:
            j = timeinterval.index(minute)
            fcount[j] = fcount[j] + 1
        else:
            timeinterval.append(minute)
            fcount.append(1)
    max = 0
    min = 0
    for i in range(0,len(fcount)):
        if fcount[max] < fcount[i]:
            max = i
        if fcount[min] > fcount[i]:
            min = i

    root4 = tk.Tk()
    title4 = root4.title("Erisim Yogunlugu")
    canvas4 = tk.Canvas(root4, height = 500, width = 1000, bg = "#260D39")
    canvas4.pack(fill=tk.BOTH, expand=True)
    labe1 = Label(canvas4, text="Erisimin En Yogun Oldugu Zaman Araligi 00:" + str(timeinterval[max]) + ":00 ve 00:" + str(timeinterval[max] + 1) + ":00 Dakikalari Arasi ve Erisim Sayisi: " + str(fcount[max]),font="25",width=100,fg="white", bg="#260D39")
    labe1.pack(fill=tk.BOTH,expand=True)
    labe2 = Label(canvas4, text="Erisimin En Az Yogun Oldugu Zaman Araligi 00:" + str(timeinterval[min]) + ":00 ve 00:" + str(timeinterval[min] + 1) + ":00 Dakikalari Arasi ve Erisim Sayisi: " + str(fcount[min]),font="25",width=100,fg="white", bg="#260D39")
    labe2.pack(fill=tk.BOTH,expand=True)
    for sdc in timeinterval:
        labe3 = Label(canvas4, text="00:" + str(sdc) + ":00 ve 00:" + str(sdc + 1) + ":00 Dakikalari Arasi ve Erisim Sayisi: " + str(fcount[timeinterval.index(sdc)]),font="25",width=100,fg="white", bg="#260D39")
        labe3.pack(fill=tk.BOTH,expand=True)
    def histo1():
        plt.figure(figsize=(12,8))
        plt.title("Zaman Araliklari ve Yogunluklari")
        plt.plot(timeinterval,fcount)
        plt.show()
    button4 = Button(canvas4,text="GRAFIK",padx=20,pady=20,command=histo1)
    button4.pack()
    root4.mainloop()

def transacs():#ASSOCİATİON RULE MİNİNG İŞLEMİ
    transactions = []
    oneses = []
    for a in userintervals:#her session için transaction listesi oluşturma işlemi
        oneses.clear()
        for i in range(0,len(a.index)):
            oneses.append(a.iloc[i,2])
        transactions.append(oneses.copy()) #tüm transactionlar

    root5 = tk.Tk()
    title5 = root5.title("Association Rule Mining")
    canvas5 = tk.Canvas(root5, height = 500, width = 1000, bg = "#260D39")
    canvas5.pack(fill=tk.BOTH, expand=True)
    labe9 = Label(canvas5, text="Toplam Transaction Sayisi:  " + str(len(transactions)) + "\nMinimum Support ve Minimum Confidence Degerlerini Giriniz\n(Degerler 0.01 ile 0.001 arasinda olmalidir)",font="25",width=100,fg="white", bg="#260D39")
    labe9.pack()
    def ental2():
        minsup = entr.get()
        mincon = entr2.get()
        itemsets, rules = apriori(transactions, min_support=float(minsup), min_confidence=float(mincon))
        root6 = tk.Tk()
        title6 = root6.title("Association Rule Mining")
        canvas6 = tk.Canvas(root6, height = 700, width = 700, bg = "#260D39")
        canvas6.pack(fill=tk.BOTH, expand=True)
        labe7 = Label(canvas6, text="Kurali Saglayan Transactionlar",font="25",width=100,fg="white", bg="#260D39")
        labe7.pack(side=tk.TOP)
        scrollbar = Scrollbar(canvas6)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        mylist = Listbox(canvas6, yscrollcommand = scrollbar.set, bg="#260D39",fg="white",font="25")
        for adf in rules:
           mylist.insert(END, adf)
        mylist.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        scrollbar.config(command=mylist.yview)
        root6.mainloop()
    labe5 = Label(canvas5, text="Minimum Support Degeri  ( <=0.01 olmali )",font="25",width=100,height=4,fg="white", bg="#260D39")
    labe5.pack()
    entr = Entry(canvas5)
    entr.pack()
    labe6 = Label(canvas5, text="\nMinimum Confidence Degeri  ( <=0.9 olmali )",font="25",width=100,height=4,fg="white", bg="#260D39")
    labe6.pack()
    entr2 = Entry(canvas5)
    entr2.pack()
    entbut1 = Button(canvas5,text = "SUBMIT", padx=20,pady=20,command=ental2)
    entbut1.pack(side=tk.BOTTOM)
    root5.mainloop()

docTC = tk.Button(root, text = "Dokuman Tipleri ve Kullanim Sayilari", font="25",pady = 20, padx = 10, fg = "yellow", bg = "#132D42", command = docTypeCount)
docTC.pack(fill=X)

docB = tk.Button(root, text = "Erisilen Toplam Dosya Boyutu",font="25", pady = 20, padx = 10, fg = "yellow", bg = "#132D42", command = docByte)
docB.pack(fill=X)

acC = tk.Button(root, text = "Erisim Kodlari", font="25",pady = 20, padx = 10, fg = "yellow", bg = "#132D42", command = accCodes)
acC.pack(fill=X)

acT = tk.Button(root, text = "Erisimin En Yogun ve En Az Yogun Oldugu Zaman Araliklari",font="25", pady = 20, padx = 10, fg = "yellow", bg = "#132D42",command = accTimeInt)
acT.pack(fill=X)

tran = tk.Button(root, text = "Association Rule Mining ile Request Edilen Dokumanlar",font="25", pady =20, padx = 10, fg = "yellow", bg = "#132D42", command = transacs)
tran.pack(fill=X)

button = tk.Button(root, text="Kapatmak Icin Tiklayiniz",font="25", pady = 20, padx = 10, fg = "white", bg = "red", command =lambda: root.destroy())
button.pack(fill=X)

sbutton = tk.Button(root, text="Simge Durumuna Kucult",font="25", pady = 20, padx = 10, fg = "white", bg = "black", command=lambda: root.iconify())
sbutton.pack(fill=X)

root.mainloop()
