import tkinter as tk
from tkinter import *

fatihHesap={
    "isim":"Fatih Taşkın",
    "HesapNo":"12345678",
    "bakiye":5000,
    "ekHesap":2000
}

tahaHesap={
    "isim": "Taha Bayrak",
    "HesapNo": "87654321",
    "bakiye": 10000,
    "ekHesap": 3000
}
pencere = tk.Tk()
pencere.geometry("800x600")
def sign_in():
    global fatihHesap
    global girilenTutar
    
    hesapNo=entry.get()
    if hesapNo=="12345678":
        girilenTutar=0
        def tutarfonk():
            global girilenTutar
            global fatihHesap
            tutar=entry1.get()
            girilenTutar=int(tutar)

            if girilenTutar <= fatihHesap["bakiye"]:
                yazi5.config(text="")
                fatihHesap["bakiye"]-=girilenTutar
                yazi.config(text=f'hesapta {fatihHesap["bakiye"]} tl kaldı. ek hesapta {fatihHesap["ekHesap"]} tl kaldı.')
            elif girilenTutar> fatihHesap["bakiye"] and girilenTutar<=fatihHesap["bakiye"]+fatihHesap["ekHesap"]:
                yazi5.config(text="")
                fatihHesap["ekHesap"] = fatihHesap["ekHesap"]-(girilenTutar-fatihHesap["bakiye"])
                fatihHesap["bakiye"] = 0
                yazi.config(text=f'hesapta {fatihHesap["bakiye"]} tl kaldı. ek hesapta {fatihHesap["ekHesap"]} tl kaldı.')
            else:
                yazi5.config(text=f'Hesapta {girilenTutar} tl bulunmuyor. Bu parayı çekemezsiniz!',fg="red",font=("Vertana",14))
                

        def paraYatir():
            global girilenTutar
            global fatihHesap
            tutar=entry1.get()        
            girilenTutar=int(tutar)
            yazi5.config(text="")
            fatihHesap["bakiye"] = girilenTutar+fatihHesap["bakiye"]
            yazi.config(text=f'Hesapta olan para: {fatihHesap["bakiye"]} / Ek hesapta olan para: {fatihHesap["ekHesap"]} ')
        pencere.title("BANKAMATİK")
        pencere.geometry("800x600")
        yazi=tk.Label(pencere)
        yazi.config(text=f'Hesapta olan para: {fatihHesap["bakiye"]} / Ek hesapta olan para: {fatihHesap["ekHesap"]}',fg="green",font=("Vertana",14))
        yazi.pack()
        dugme=tk.Button(pencere)
        entry1=Entry(pencere)
        entry1.pack()
        dugme.config(text="para çek", width=40,height=5,command=tutarfonk)
        dugme.config(bg="black", fg="yellow",font=("Vertana",15))
        dugme.pack()
        dugme2 = tk.Button(text = "para yatır", width=40,height=5, command=paraYatir)
        dugme2.config(bg="black", fg="yellow",font=("Vertana",15))
        dugme2.pack()
        dugme3 = tk.Button(text = "ÇIKIŞ", width=38,height=5, command=pencere.quit)
        dugme3.config(bg="green", fg="red",font=("Vertana",16))
        dugme3.pack()
        etiket=Label(pencere)
        etiket.config(text="BANKAMATİK SİSTEMLERİ",bg="green",fg="yellow",font=("Vertana",24))
        etiket.place(x=195,y=500)
        yazi5=tk.Label(pencere)
        yazi5.config(text="")
        yazi5.pack()
        hosgeldin=Label(pencere)
        hosgeldin.config(text=f'Sayin {fatihHesap["isim"]} sisteme hoşgeldiniz',fg="green",font=("Vertana",12))
        hosgeldin.place(x=195,y=550)
        pencere.mainloop()
        entry.destroy()
        buton.destroy()
    else:
        print("yanlış giriş")


    hesapNo1=entry.get()
    if hesapNo1=="87654321":
        girilenTutar=0
        def tutarfonk():
            global girilenTutar
            global fatihHesap
            tutar=entry1.get()
            girilenTutar = int(tutar)
    
            if girilenTutar <= tahaHesap["bakiye"]:
                yazi5.config(text="")
                tahaHesap["bakiye"]-=girilenTutar
                yazi.config(text=f'hesapta {tahaHesap["bakiye"]} tl kaldı. ek hesapta {tahaHesap["ekHesap"]} tl kaldı.')

            elif girilenTutar> tahaHesap["bakiye"] and girilenTutar<=tahaHesap["bakiye"]+tahaHesap["ekHesap"]:
                yazi5.config(text="")
                tahaHesap["ekHesap"] = tahaHesap["ekHesap"]-(girilenTutar-tahaHesap["bakiye"])
                tahaHesap["bakiye"] = 0
                yazi.config(text=f'hesapta {tahaHesap["bakiye"]} tl kaldı. ek hesapta {tahaHesap["ekHesap"]} tl kaldı.')
       
                
            else:
                yazi5.config(text=f'Hesapta {girilenTutar} tl bulunmuyor. Bu parayı çekemezsiniz!',fg="red",font=("Vertana",14))


        def paraYatir():
            global girilenTutar
            global tahaHesap
            tutar=entry1.get()
            girilenTutar = int(tutar)
            yazi5.config(text="")
            tahaHesap["bakiye"] = girilenTutar+tahaHesap["bakiye"]
            yazi.config(text=f'Hesapta olan para: {tahaHesap["bakiye"]} / Ek hesapta olan para: {tahaHesap["ekHesap"]} ')

        pencere.title("BANKAMATİK")
        pencere.geometry("800x600")
        yazi=tk.Label(pencere)
        yazi.config(text=f'Hesapta olan para: {tahaHesap["bakiye"]} / Ek hesapta olan para: {tahaHesap["ekHesap"]}',fg="green",font=("Vertana",14))
        yazi.pack()
        dugme=tk.Button(pencere)
        entry1=Entry(pencere)
        tutar=entry1.get()
        entry1.pack()
        dugme.config(text="para çek", width=40,height=5,command=tutarfonk)
        dugme.config(bg="black", fg="yellow",font=("Vertana",15))
        dugme.pack()
        dugme2 = tk.Button(text = "para yatır", width=40,height=5, command=paraYatir)
        dugme2.config(bg="black", fg="yellow",font=("Vertana",15))
        dugme2.pack()
        dugme3 = tk.Button(text = "ÇIKIŞ", width=38,height=5, command=pencere.quit)
        dugme3.config(bg="green", fg="red",font=("Vertana",16))
        dugme3.pack()
        etiket=Label(pencere)
        etiket.config(text="BANKAMATİK SİSTEMLERİ",bg="green",fg="yellow",font=("Vertana",24))
        etiket.place(x=195,y=500)
        yazi5=tk.Label(pencere)
        yazi5.config(text="")
        yazi5.pack()
        hosgeldin=Label(pencere)
        hosgeldin.config(text=f'Sayin {fatihHesap["isim"]} sisteme hoşgeldiniz',fg="green",font=("Vertana",12))
        hosgeldin.place(x=195,y=550)
        pencere.mainloop()
        entry.destroy()
        buton.destroy()
    else:
        pencere1 = Tk()
        pencere1.geometry("400x200")
        etiket=Label(pencere1)
        etiket.config(text="HATALI ŞİFRE",bg="RED",font=("Vertana",24))
        etiket.place(x=100,y=100)
        mainloop()


label=Label(pencere)
label.config(text="Hesap nosunu giriniz",font=("Arial",20))

label.place(x=250,y=180)

entry=Entry(pencere)
entry.place(x=255,y=225)

buton=Button(pencere)
buton.config(text="Giriş yap",bg="black",fg="white",command=sign_in)
buton.place(x=289,y=250)

mainloop()