import tkinter as tk
from tkinter import PhotoImage, messagebox
import sqlite3

window = tk.Tk()
window.title("Altınbaş Üniversitesi: KÜTÜPHANE")
window.geometry("1300x750+100+20")
window.attributes('-fullscreen', False)
window.resizable(False, False)
window.config(bg="white")

image = PhotoImage(file="footer.logo.png")
logo = tk.Label(window, image=image)
logo.place(x=400, y=650)

footer_image = PhotoImage(file="altinbas.png")
footer_logo = tk.Label(window, image=footer_image, borderwidth=0)
footer_logo.place(x=10, y=15)

yerleskeler_image = PhotoImage(file="yerleskeler.png")
yerleskeler_logo = tk.Label(window, image=yerleskeler_image, borderwidth=0)
yerleskeler_logo.place(x=70, y=100)

messagebox.showinfo("Altınbaş Üniversitesi", "Altınbaş Üniversitesi, Kütüphane Bilgi İşlem Sistemine Hoşgeldiniz!")


def kitaplik():
    kitaplik_window = tk.Toplevel()
    kitaplik_window.title("Altınbaş Üniversitesi: KİTAPLIK")
    kitaplik_window.geometry("1300x750+100+20")
    kitaplik_window.attributes('-fullscreen', False)
    kitaplik_window.resizable(False, False)
    kitaplik_window.config(bg="white")

    global kitaplik_image
    kitaplik_image = PhotoImage(file="altinbas.png")
    kitaplik_logo = tk.Label(kitaplik_window, image=kitaplik_image)
    kitaplik_logo.place(x=10, y=15)


    global arka_plan
    arka_plan = PhotoImage(file="arka_plan.png")
    arka_plan_logo = tk.Label(kitaplik_window, image=arka_plan)
    arka_plan_logo.place(x=0, y=0)


    def kitap_ekle():
        arka_plan_logo.place_forget()
        pass
        def kitap_verilerini_kaydet():
            kitap_id_db = kitap_id.get("1.0", tk.END)
            kitap_name_db = kitap_name.get("1.0", tk.END)
            kitap_yerleske_db = kitap_yerleske.get("1.0", tk.END)
            kitap_yazar_db = kitap_yazar.get("1.0", tk.END)
            kitap_sayfa_db = kitap_sayfa.get("1.0", tk.END)

            # Veritabanına bağlan
            db_file = "altinbas_kitaplik.db"
            veri_tabanina_bagla = sqlite3.connect(db_file)
            cursor = veri_tabanina_bagla.cursor()

            # Tablo oluştur
            cursor.execute('''CREATE TABLE IF NOT EXISTS altinbas_kitaplik_database
               (books_id INTEGER, books_name TEXT,books_campus TEXT, books_writer TEXT, books_page INTEGER) ''')

            # Verileri ekle
            cursor.execute(
                "INSERT INTO altinbas_kitaplik_database (books_id, books_name, books_campus, books_writer, books_page) VALUES(?, ?, ?, ?, ?)",
                (kitap_id_db, kitap_name_db, kitap_yerleske_db, kitap_yazar_db, kitap_sayfa_db))

            veri_tabanina_bagla.commit()
            messagebox.showinfo(kitaplik_window, message="Kayıt Başarıyla Eklendi")

        info1 = tk.Label(kitaplik_window, text="KİTAP ID", bg="white", font=("arial", 15))
        info1.place(x=20, y=150)
        kitap_id = tk.Text(kitaplik_window, width=25, height=1, bg="light blue")
        kitap_id.place(x=170, y=155)

        info2 = tk.Label(kitaplik_window, text="KİTAP ADI", bg="white", font=("arial", 15))
        info2.place(x=20, y=190)
        kitap_name = tk.Text(kitaplik_window, width=25, height=1, bg="light blue")
        kitap_name.place(x=170, y=195)

        info3 = tk.Label(kitaplik_window, text="YERLEŞKE", bg="white", font=("arial", 15))
        info3.place(x=20, y=230)
        kitap_yerleske = tk.Text(kitaplik_window, width=25, height=1, bg="light blue")
        kitap_yerleske.place(x=170, y=235)


        info4 = tk.Label(kitaplik_window, text="YAZAR", bg="white", font=("arial", 15))
        info4.place(x=20, y=275)
        kitap_yazar = tk.Text(kitaplik_window, width=25, height=1, bg="light blue")
        kitap_yazar.place(x=170, y=280)

        info5 = tk.Label(kitaplik_window, text="SAYFA SAYISI", bg="white", font=("arial", 15))
        info5.place(x=20, y=320)
        kitap_sayfa = tk.Text(kitaplik_window, width=25, height=1, bg="light blue")
        kitap_sayfa.place(x=170, y=325)

        kaydet_buton = tk.Button(kitaplik_window, text="Değişikleri Kaydet", command=kitap_verilerini_kaydet)
        kaydet_buton.place(x=20, y=400)


    def kitap_verilerini_getir():
        kitaplik_veriler_window = tk.Toplevel()
        kitaplik_veriler_window.title("Altınbaş Üniversitesi: KİTAPLIK VERİ TABANI")
        kitaplik_veriler_window.geometry("1300x750+100+20")
        kitaplik_veriler_window.attributes('-fullscreen', False)
        kitaplik_veriler_window.resizable(False, False)
        kitaplik_veriler_window.config(bg="white")

        # veri tabanı işlemleri

        def kitap_verilerini_goster():
            db_file = "altinbas_kitaplik.db"
            veri_tabanina_bagla = sqlite3.connect(db_file)
            cursor = veri_tabanina_bagla.cursor()

            # Veritabanından verileri al
            cursor.execute("SELECT * FROM altinbas_kitaplik_database")
            rows1 = cursor.fetchall()

            for index1, row in enumerate(rows1):
                null = tk.Label(kitaplik_veriler_window, font=("arial", 10), bg="white")
                null.grid(row=index1, pady=10, )

                null2 = tk.Label(kitaplik_veriler_window, font=("arial", 10), bg="white")
                null2.grid(row=index1 + 3, pady=10, )

                kitap_id_label = tk.Label(kitaplik_veriler_window, text="KİTAP ID", font=("arial", 10), bg="red", fg="white")
                kitap_id_label.place(x=70, y=100)

                kitap_name_label = tk.Label(kitaplik_veriler_window, text="KİTAP ADI", font=("arial", 10), bg="red", fg="white")
                kitap_name_label.place(x=300, y=100)

                kitap_yerleske_label = tk.Label(kitaplik_veriler_window, text="YERLEŞKE", font=("arial", 10), bg="red", fg="white")
                kitap_yerleske_label.place(x=540, y=100)

                kitap_yazar_label = tk.Label(kitaplik_veriler_window, text="YAZAR", font=("arial", 10), bg="red", fg="white")
                kitap_yazar_label.place(x=760, y=100)

                kitap_sayfa_label = tk.Label(kitaplik_veriler_window, text="SAYFA SAYISI", font=("arial", 10), bg="red", fg="white")
                kitap_sayfa_label.place(x=920, y=100)

                kitap_id_veri = tk.Label(kitaplik_veriler_window, text=row[0], font=("arial", 10), bg="white", fg="red")
                kitap_id_veri.grid(row=index1 + 3, column=10, padx=60)

                kitap_name_veri = tk.Label(kitaplik_veriler_window, text=row[1], font=("arial", 10), bg="white", fg="blue")
                kitap_name_veri.grid(row=index1 + 3, column=11, padx=60)

                kitap_yerleske_veri = tk.Label(kitaplik_veriler_window, text=row[2], font=("arial", 10), bg="white", fg="blue")
                kitap_yerleske_veri.grid(row=index1 + 3, column=12, padx=60)

                kitap_yazar_veri = tk.Label(kitaplik_veriler_window, text=row[3], font=("arial", 10), bg="white", fg="blue")
                kitap_yazar_veri.grid(row=index1 + 3, column=13, padx=60)

                kitap_sayfa_veri = tk.Label(kitaplik_veriler_window, text=row[4], font=("arial", 10), bg="white", fg="red")
                kitap_sayfa_veri.grid(row=index1 + 3, column=14, padx=60)

        kitap_verilerini_goster()

        global veriler_image
        veriler_image = PhotoImage(file="altinbas.png")
        veriler_logo = tk.Label(kitaplik_veriler_window, image=veriler_image, borderwidth=0)
        veriler_logo.place(x=10, y=15)

    veriler = tk.Button(kitaplik_window, text="Kitap Veri Ekle", width=40, height=5, command=kitap_ekle)
    veriler.place(x=1010, y=260)
    veri_ekle = tk.Button(kitaplik_window, text="Kitap Verileri", width=40, height=5, command=kitap_verilerini_getir)
    veri_ekle.place(x=1010, y=350)

# kitap verme yeni kullanıcı tanımlama kısmı
def data_base():
    data_base_window = tk.Toplevel()
    data_base_window.title("Altınbaş Üniversitesi: VERİ TABANI")
    data_base_window.geometry("1300x750+100+20")
    data_base_window.attributes('-fullscreen', False)
    data_base_window.resizable(False, False)
    data_base_window.config(bg="white")

    global data_base_image
    data_base_image = PhotoImage(file="altinbas.png")
    data_base_logo = tk.Label(data_base_window, image=data_base_image, borderwidth=0)
    data_base_logo.place(x=10, y=15)

    global arka_plan
    arka_plan = PhotoImage(file="arka_plan.png")
    arka_plan_logo = tk.Label(data_base_window, image=arka_plan)
    arka_plan_logo.place(x=0, y=0)


    def veri_ekle():
        arka_plan_logo.place_forget()

        def verileri_kaydet():
            id_db = id.get("1.0", tk.END)
            name_db = name.get("1.0", tk.END)
            fakülte_db = fakülte.get("1.0", tk.END)
            yerleske_db = yerleske.get("1.0", tk.END)
            kitap_adi_db = kitap_adi.get("1.0", tk.END)
            kitap_id_db = kitap_id.get("1.0", tk.END)

            # Veritabanına bağlan
            db_file = "altinbas_kütüphane.db"
            veri_tabanina_bagla = sqlite3.connect(db_file)
            cursor = veri_tabanina_bagla.cursor()

            # Tablo oluştur
            cursor.execute('''CREATE TABLE IF NOT EXISTS altinbas_kütüphane_database
            (id INTEGER, name TEXT, section TEXT, campus TEXT, books_name TEXT, booksID INTEGER) ''')

            # Verileri ekle
            cursor.execute("INSERT INTO altinbas_kütüphane_database (id, name, section, campus, books_name, booksID) VALUES(?, ?, ?, ?, ?, ?)",
                           (id_db, name_db, fakülte_db, yerleske_db, kitap_adi_db, kitap_id_db))

            veri_tabanina_bagla.commit()
            messagebox.showinfo(data_base_window, message="Kayıt Başarıyla Eklendi")

        info1 = tk.Label(data_base_window, text="Öğrenci ID", bg="white", font=("arial", 15))
        info1.place(x=20, y=150)
        id = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        id.place(x=170, y=155)

        info2 = tk.Label(data_base_window, text="Öğrenci Ad", bg="white", font=("arial", 15))
        info2.place(x=20, y=190)
        name = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        name.place(x=170, y=195)

        info3 = tk.Label(data_base_window, text="Fakülte/Bölüm", bg="white", font=("arial", 15))
        info3.place(x=20, y=230)
        fakülte = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        fakülte.place(x=170, y=235)

        info4 = tk.Label(data_base_window, text="Yerleşke", bg="white", font=("arial", 15))
        info4.place(x=20, y=270)
        yerleske = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        yerleske.place(x=170, y=275)

        info5 = tk.Label(data_base_window, text="Kitap Adı", bg="white", font=("arial", 15))
        info5.place(x=20, y=310)
        kitap_adi = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        kitap_adi.place(x=170, y=315)

        info6 = tk.Label(data_base_window, text="Kitap ID ", bg="white", font=("arial", 15))
        info6.place(x=20, y=350)
        kitap_id = tk.Text(data_base_window, width=25, height=1, bg="light blue")
        kitap_id.place(x=170, y=355)

        kaydet_buton = tk.Button(data_base_window, text="Değişikleri Kaydet", command=verileri_kaydet)
        kaydet_buton.place(x=20, y=400)


    def verileri_getir():
        veriler_window = tk.Toplevel()
        veriler_window.title("Altınbaş Üniversitesi: KULLANICI VERİ TABANI")
        veriler_window.geometry("1300x750+100+20")
        veriler_window.attributes('-fullscreen', False)
        veriler_window.resizable(False, False)
        veriler_window.config(bg="white")


        #veri tabanı işlemleri

        def verileri_goster():
            db_file = "altinbas_kütüphane.db"
            veri_tabanina_bagla = sqlite3.connect(db_file)
            cursor = veri_tabanina_bagla.cursor()

            # Veritabanından verileri al
            cursor.execute("SELECT * FROM altinbas_kütüphane_database")
            rows = cursor.fetchall()

            for index, row in enumerate(rows):
                null = tk.Label(veriler_window,  font=("arial", 10), bg="white")
                null.grid(row=index,  pady=10, )

                null2 = tk.Label(veriler_window, font=("arial", 10), bg="white")
                null2.grid(row=index+3, pady=10, )

                id_label = tk.Label(veriler_window, text="ÖĞRENCİ ID", font=("arial", 10), bg="red", fg="white")
                id_label.place(x=70, y=100)

                name_label = tk.Label(veriler_window, text="ÖĞRNCİ AD", font=("arial", 10), bg="red", fg="white")
                name_label.place(x=260, y=100)

                fakülte_label = tk.Label(veriler_window, text="BÖLÜM", font=("arial", 10), bg="red", fg="white")
                fakülte_label.place(x=480, y=100)

                yerleske_label = tk.Label(veriler_window, text="YERLEŞKE", font=("arial", 10), bg="red", fg="white")
                yerleske_label.place(x=650, y=100)

                kitap_adi_label = tk.Label(veriler_window, text="KİTAP ADI", font=("arial", 10), bg="red", fg="white")
                kitap_adi_label.place(x=890, y=100)

                kitapid_label = tk.Label(veriler_window, text="KİTAP İD", font=("arial", 10),bg="red", fg="white")
                kitapid_label.place(x=1127, y=100)

                id_veri = tk.Label(veriler_window, text=row[0], font=("arial", 10), bg="white", fg="red")
                id_veri.grid(row=index+3, column=10, padx=60)

                name_veri = tk.Label(veriler_window, text=row[1], font=("arial", 10), bg="white", fg="blue")
                name_veri.grid(row=index+3, column=11, padx=60)

                fakulte_veri = tk.Label(veriler_window, text=row[2], font=("arial", 10), bg="white", fg="blue")
                fakulte_veri.grid(row=index+3, column=12, padx=60)

                yerleske_veri = tk.Label(veriler_window, text=row[3], font=("arial", 10), bg="white", fg="blue")
                yerleske_veri.grid(row=index+3, column=13, padx=60)

                kitap_adi_veri = tk.Label(veriler_window, text=row[4], font=("arial", 10), bg="white", fg="blue")
                kitap_adi_veri.grid(row=index+3, column=14, padx=60)

                kitapid_veri = tk.Label(veriler_window, text=row[5], font=("arial", 10), bg="white", fg="red")
                kitapid_veri.grid(row=index+3, column=15, padx=55)

        verileri_goster()

        global veriler_image
        veriler_image = PhotoImage(file="altinbas.png")
        veriler_logo = tk.Label(veriler_window, image=veriler_image, borderwidth=0)
        veriler_logo.place(x=10, y=15)


    veriler = tk.Button(data_base_window, text="Kullanıcı Veri Ekle", width=40, height=5, command=veri_ekle)
    veriler.place(x=1010, y=260)
    veri_ekle = tk.Button(data_base_window, text="Kullanıcı Verileri", width=40, height=5, command=verileri_getir)
    veri_ekle.place(x=1010, y=350)


kitaplik_btn = tk.Button(window, text="Kitaplık", width=40, height=5, command=kitaplik)
kitaplik_btn.place(x=1010, y=260)
data_base_btn = tk.Button(window, text="Veri Tabanı", width=40, height=5, command=data_base)
data_base_btn.place(x=1010, y=350)

window.mainloop()
