def cay_satis_sistemi():
    defter_numaralari = {"1": ("Ali", 100, 0), "2": ("Ayşe", 150, 0), "3": ("Mehmet", 200, 0), "4": ("Zeynep", 120, 0),
                         "5": ("Ahmet", 80, 0), "6": ("Elif", 50, 0), "7": ("Hasan", 180, 0), "8": ("Selin", 90, 0),
                         "9": ("Emre", 110, 0), "10": ("Nazlı", 70, 0)}
    hatali_secim_sayisi = 0

    #Diziye çiftçi kaydı eklemek için varsa uyarı verme
    def defter_numarasi_ekle():
        defter_numarasi = input("Defter numarası: ")
        
        if defter_numarasi in defter_numaralari:
            print("Bu defter numarası zaten mevcut!")
        else:
            isim_ekleme = input("İsim giriniz: ")
            kontenjan = int(input("Kontenjan: "))
            defter_numaralari[defter_numarasi] = (isim_ekleme, kontenjan)

    #Toplanan çayı kilosuna göre kontejanı aşmadıysa TL cinsinden hesaplayıp çıktısını veriyor
    def cay_toplama():
        defter_numarasi = input("Defter numarası: ")
        isim_ekleme, kontenjan, toplam_cay = defter_numaralari.get(defter_numarasi, ("", 0, 0))
        miktar = int(input("Toplanan çay miktarı (kg): "))

        if defter_numarasi in defter_numaralari:
            if miktar <= kontenjan - toplam_cay:
                tl_miktar = miktar * 11.3  # Kilogram başına TL fiyat
                print(f"{defter_numarasi} numaralı {isim_ekleme} adlı çiftçinin defterdeki çay toplamı: {toplam_cay + miktar} kg")
                print(f"Toplam TL tutar: {tl_miktar} TL")
                print(f"Kalan Kontejan: {kontenjan - toplam_cay}")
                defter_numaralari[defter_numarasi] = (isim_ekleme, kontenjan, toplam_cay + miktar)             
            else:
                print("Belirtilen miktar, defter numarasının kontenjanını aşıyor!")
        else:
            print("Belirtilen defter numarası kayıtlı değil!")
            
    #İşlem menüsü
    def menu_goster():
        print("1. Çiftçi Kaydı Ekleme")
        print("2. Çay Toplama")
        print("3. Menüye Dön")
        print("4. Çıkış")
        
    #Güvenlik   
    def kullanici_giris():
        parola = input("Şifre: ")
        return parola == "53"  # Doğru şifre burada kontrol edilir    

    #Menüde yapılan işlem seçimi ve doğru yanlış seçim kontrolü
    if kullanici_giris():
        while True:
            menu_goster()
            secim = input("Seçiminizi yapın (1-4): ")

            if secim == "1":
                defter_numarasi_ekle()
                hatali_secim_sayisi = 0
            elif secim == "2":
                cay_toplama()
                hatali_secim_sayisi = 0
            elif secim == "3":
                menu_goster()
            elif secim == "4":
                print("Programdan çıkılıyor...")
                break
            else:
                hatali_secim_sayisi += 1
                print("Geçersiz bir seçim yaptınız!")

                if hatali_secim_sayisi > 5:
                    print("Uygulamayı kullanmayı bilmiyor gibi görünüyorsunuz.")
                    print("Geçerli seçimler 1, 2 veya 3 olmalıdır.")
                    print("Lütfen doğru seçimi yapmayı deneyin.")
                    menu_goster()
cay_satis_sistemi()
