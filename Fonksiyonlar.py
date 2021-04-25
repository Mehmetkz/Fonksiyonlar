# Dry Prensibi
# Dont Repeat Yourself

sayi1 = float(input("1.Sayıyı girin:\t"))
sayi2 = float(input("2.Sayıyı girin:\t"))
secenek = input("Yapılacak işlemi seçiniz:\n[1] Toplama \n[2] Çıkarma\n[3]Çarpma\n[4]Bölme")
if secenek == "1":
    print(f"{sayi1} + {sayi2} = {sayi2+sayi1}")
elif secenek == "2":
    print(f"{sayi1} - {sayi2} = {sayi2 - sayi1}")
elif secenek == "3":
    print(f"{sayi1} * {sayi2} = {sayi2 * sayi1}")
elif secenek == "4":
    print(f"{sayi1} / {sayi2} = {sayi2 / sayi1}")
else:
    print("Hatalı Seçenek Girdiniz!")

try:
    sayi1 = float(input("1.Sayıyı girin:\t"))
    sayi2 = float(input("2.Sayıyı girin:\t"))
    secenek = input("Yapılacak işlemi seçiniz:\n[1] Toplama \n[2] Çıkarma\n[3]Çarpma\n[4]Bölme")

    hesap_makinesi = {"1": ["+", (sayi1 + sayi2)],
                      "2": ["-", (sayi1 - sayi2)],
                      "3": ["*", (sayi1 * sayi2)],
                      "4": ["/", (sayi1 / sayi2)]}

    print(f"{sayi1} {hesap_makinesi[secenek][0]} {sayi2} = {hesap_makinesi[secenek][1]}")

except KeyError:
    print("Hatalı Seçenek Girdiniz!!")
except ValueError:
    print("Ondalık değer giriniz!!")

# Fonksiyonlar
# Kodların daha az tekrar etmesini sağlar

# Ekrana merhaba yazan fonksiyon yazdırma
def merhaba():
    print("Merhaba")

merhaba()

# iki sayıyı toplayan ve yazdıran fonksiyon
def topla():
    sayi1 = int(input("Sayi1:"))
    sayi2 = int(input("Sayi2:"))
    print(sayi1+sayi2)

topla()

# Sayi listelerini seçeneğe göre çift, tek, ortalama gibi değerleri yazdıran program
liste1 = [1,2,3,4,5,6,7,5]
liste2 = [56,57,45,32,32,122,65,76,56]
liste3 = [563,527,456,352,324,1232,625,716,516]
liste4 = [51,52,45,31,74,12,5,7,5]

secenek = "tek"

def ortalama(liste:list,secenek:str):
    toplam = 0
    if secenek == "tüm":
        for sayi in liste1:
            toplam += sayi
        print(f"{liste} listesinin {secenek.title()} seçeneğine göre ortalaması: {(toplam / len(liste))}")
    elif secenek == "tek":
        for sayi in liste1:
            if sayi % 2 != 0:
                toplam += sayi
        print(f"{liste} listesinin {secenek.title()} seçeneğine göre ortalaması: {(toplam / len(liste))}")
    elif secenek == "cift":
        for sayi in liste1:
            if sayi % 2 == 0:
                toplam += sayi
        print(f"{liste} listesinin {secenek.title()} seçeneğine göre ortalaması: {(toplam / len(liste))}")
    else:
        print("Hatalı secenek girdiniz!")

ortalama(liste3,"tek")

sayi_liste =[liste1,liste2,liste3,liste4]
sayi_sozluk = {0:"tüm",1:"tek",2:"cift",3:"tüm"}
for i in range(len(sayi_liste)):
    ortalama(liste=sayi_liste[i],secenek=sayi_sozluk[i])

# Yarıçap ve cisim bilgileri ile alan hesabı

def alan_hesabı(yarıcap,cisim,pi=3.14):
    if cisim.lower() == "daire":
        print("Daire alanı:",pi*yarıcap*yarıcap)
    elif cisim.lower() == "küre":
        print("Küre alanı:",4*pi*yarıcap*yarıcap)
    else:
        print("Tanımlanamayan cisim")

alan_hesabı(yarıcap=3,cisim="Daire")
alan_hesabı(cisim="Daire",yarıcap=3)
alan_hesabı(3,"Daire",3.1415)

# isim listesi oluşturup merhaba {isim} olarak yazdırmak

def isim_topla():
    return input("İsim giriniz: ")

def mesaj_yaz(isim):
    print(f"Merhaba {isim}")

isim_liste = [isim_topla() for i in range(3)]
for isim in isim_liste:
    mesaj_yaz(isim)

# Dışarıdan girilen sayıların toplamını liste şeklinde yazmak
def topla(*args): #parametre sayısı önemsiz olan tupple
    toplam = 0
    for sayi in args:
        toplam += sayi
    return toplam

topla(2,3,4,3,2,1)

# isim, posta,numara bilgilerini sözlüğe eklemek
def bilgiler(**kwargs): # parametre sayısı önemsiz olan dict
    return kwargs

sozluk = {}
for i in range(3):
    isim = input("Bir isim giriniz: ")
    posta = input("Bir posta adresi giriniz: ")
    numara = input("Numara: ")
    sozluk[i] = bilgiler(isim=isim,
                         posta=posta,
                         numara=numara)

# Decorator
def en(func):
    def wrapper(liste):
        en_kucuk = 100
        for i in liste:
            if i < en_kucuk:
                en_kucuk = i
        print(f"Listedeki en kucuk deger {en_kucuk}")

        print(func(liste))

        en_buyuk = 0
        for i in liste:
            if i > en_buyuk:
                en_buyuk = i
        print(f"Listedeki en buyuk deger {en_buyuk}")
    return wrapper

@en   #Decorator
def ortalama(liste):
    toplam = 0
    for sayi in liste:
        toplam += sayi
    return toplam / len(liste)

liste5 = [12,33,54,65,41,21]
ortalama(liste5)

# Toplama işlemi : isimsiz fonksiyon
toplama = lambda a,b: a + b
toplama(4,3)

# Tek-cift bulma : isimsiz fonksiyon
tek_cift = lambda sayi: "çift" if sayi % 2 == 0 else "tek"
tek_cift(34)

# Map, filter, reduce

# Map
liste = [1,2,3,4,5,6]
yeni_liste = list(map(lambda sayi: sayi**2,liste))

# Filter
liste = [1,2,3,4,5,6]
yeni_liste2 = list(filter(lambda sayi: sayi % 2 == 0, liste))

# reduce
from functools import reduce
reduce(lambda x,y: x+y, [12,32,13,43,23,53,65,43])

#zip
id = [1,2,3,4,5]
isim = ["a","b","c","d","e"]
zip_list = list(zip(id,isim))

# Numpy
import numpy as np
np.random.seed(10)
a = np.random.randint(10,size=(3,3))
v = np.random.randint(10,size=10)

# fancy index

v[[4,3,1]]     # 4.,3. ve 1. elemanları
a[[1,1],[2,0]] # 1.satır 2.sutun & 1.satır 0.sutun
a[[1,2],1:3]   # 1. ve 2. satırlarda 1. ve 2. sutun değerleri
a[1:2,[1,2]]   # 1. ve 2. sutunlarda sadece 1.satır 1den 2'ye