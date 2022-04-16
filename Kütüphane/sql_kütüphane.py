from kütüphane import*

print("""*****************************************
Kütüphane Program Bilgileri
 İşlemler;

 1-Kitapları Göster
 2-kitap sorgulama
 3-kitap ekle
 4-kitap sil
 5-baskı yükselt

Çıkmak için 'q' ya basın.
*****************************************""")
kütüphane=Kütüphane()
while True:
    işlem = input("Yapmak istediğiniz işlem:")

    if (işlem == "q"):
        print("PROGRAM SONLANDIRILIYOR.....")
        print("YİNE BEKLERİZ....")
        break
    elif (işlem == "1"):
        kütüphane.kitaplari_goster()
    elif (işlem == "2"):
        isim = input("Hangi kitabı istiyorsunuz ?")
        print("KİTAP SORGULANIYOR..")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)
    elif (işlem == "3"):
        isim=input("isim:")
        yazar = input("yazar:")
        yayınevi = input("yayınevi:")
        tür = input("tür:")
        baskı = int(input("baskı:"))

        yeni_kitap = Kitap(isim, yazar, yayınevi, tür, baskı)

        print("KİTAP EKLENİYOR...")
        time.sleep(2)

        kütüphane.kitap_ekle(yeni_kitap)
        print("KİTAP EKLENDİ...")


    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap = input("Emin misiniz? E/H")
        if (cevap == "E"):
            print("KİTAP SİLİNİYOR..")
            time.sleep(2)

            kütüphane.kitap_sil(isim)
            print("KİTAP SİLİNDİ..")

        elif (cevap == "H"):
            print("İŞLEM GERÇEKLEŞTİRİLMEDİ..")
        else:
            print("İŞLEM GEÇERSİZ...")
    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ?")

        kütüphane.baskı_yükselt(isim)

    else:
        print("GEÇERSİZ İŞLEM!!!")

