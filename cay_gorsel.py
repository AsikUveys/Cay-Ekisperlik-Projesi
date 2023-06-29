import tkinter as tk

def cay_satis_sistemi():
    defter_numaralari = {"1": ("Ali", 100, 0), "2": ("Ayşe", 150, 0), "3": ("Mehmet", 200, 0), "4": ("Zeynep", 120, 0),
                         "5": ("Ahmet", 80, 0), "6": ("Elif", 50, 0), "7": ("Hasan", 180, 0), "8": ("Selin", 90, 0),
                         "9": ("Emre", 110, 0), "10": ("Nazlı", 70, 0)}
    hatali_secim_sayisi = 0


    def defter_numarasi_ekle():
        defter_numarasi = input_defter_numarasi.get()
        
        if defter_numarasi in defter_numaralari:
            label_durum.config(text="Bu defter numarası zaten mevcut!", fg="red")
        else:
            isim_ekleme = input_isim.get()
            kontenjan = int(input_kontenjan.get())
            defter_numaralari[defter_numarasi] = (isim_ekleme, kontenjan, 0)
            label_durum.config(text="Çiftçi bilgileri eklendi", fg="green")


    def cay_toplama():
        defter_numarasi = input_defter_numarasi.get()
        isim_ekleme, kontenjan, toplam_cay = defter_numaralari.get(defter_numarasi, ("", 0, 0))
        miktar = int(input_miktar.get())

        if defter_numarasi in defter_numaralari:
            if miktar <= kontenjan - toplam_cay:
                tl_miktar = miktar * 11.3  # Kilogram başına TL fiyat
                toplam_cay += miktar
                defter_numaralari[defter_numarasi] = (isim_ekleme, kontenjan, toplam_cay)
                label_durum.config(text=f"{defter_numarasi} numaralı {isim_ekleme} adlı çiftçinin defterdeki çay toplamı: {toplam_cay} kg\nToplam TL tutar: {tl_miktar} TL", fg="green")
            else:
                label_durum.config(text="Belirtilen miktar, defter numarasının kontenjanını aşıyor!", fg="red")
        else:
            label_durum.config(text="Belirtilen defter numarası kayıtlı değil!", fg="red")


    root = tk.Tk()
    root.title("Çay Satış Sistemi")
    root.geometry("300x300")
    root.configure(bg="#f2f2f2")

    frame_defter_numarasi = tk.Frame(root, bg="#f2f2f2")
    frame_defter_numarasi.pack(pady=10)

    label_defter_numarasi = tk.Label(frame_defter_numarasi, text="Defter Numarası:", bg="#f2f2f2")
    label_defter_numarasi.pack(side="left")

    input_defter_numarasi = tk.Entry(frame_defter_numarasi)
    input_defter_numarasi.pack(side="left")

    frame_isim = tk.Frame(root, bg="#f2f2f2")
    frame_isim.pack(pady=10)

    label_isim = tk.Label(frame_isim, text="İsim:", bg="#f2f2f2")
    label_isim.pack(side="left")

    input_isim = tk.Entry(frame_isim)
    input_isim.pack(side="left")

    frame_kontenjan = tk.Frame(root, bg="#f2f2f2")
    frame_kontenjan.pack(pady=10)

    label_kontenjan = tk.Label(frame_kontenjan, text="Kontenjan:", bg="#f2f2f2")
    label_kontenjan.pack(side="left")

    input_kontenjan = tk.Entry(frame_kontenjan)
    input_kontenjan.pack(side="left")

    frame_miktar = tk.Frame(root, bg="#f2f2f2")
    frame_miktar.pack(pady=10)

    label_miktar = tk.Label(frame_miktar, text="Çay Miktarı (kg):", bg="#f2f2f2")
    label_miktar.pack(side="left")

    input_miktar = tk.Entry(frame_miktar)
    input_miktar.pack(side="left")

    frame_button = tk.Frame(root, bg="#f2f2f2")
    frame_button.pack(pady=10)

    button_ekle = tk.Button(frame_button, text="Çiftçi Ekle", command=defter_numarasi_ekle)
    button_ekle.pack(side="left")

    button_topla = tk.Button(frame_button, text="Çay Topla", command=cay_toplama)
    button_topla.pack(side="left")

    label_durum = tk.Label(root, text="", bg="#f2f2f2", fg="black")
    label_durum.pack(pady=10)

    root.mainloop()

cay_satis_sistemi()
