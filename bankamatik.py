import _tkinter as tk
from tkinter import *

fatihhesap = {
    "isim" : "Fatih Taskin",
    "hesapno": "12345678",
    "bakiye": "5000",
    "ekhesap": "2000"

}

tahahesap = {
    "isim" : " Taha Bayrak",
    "hesapno" : "87654321",
    "bakiye" : "10000",
    "ekhesap" : "2000"

}

pencere = tk.Tk()
pencere.geometry("800x600")
def sign_in() :
    global fatihhesap
    global girilenTutar 

    hesapNo=entry.get()

    if hesapNo == "12345678" :
        girilenTutar=0
        def tutarfonk():
            global girilenTutar
            global fatihhesap
            tutar=entry1.get()
            girilenTutar=int(tutar)

            if girilenTutar <= fatihhesap["bakiye"]:
                yazi5.config(text="")
                fatihhesap["bakiye"]-=girilenTutar
                yazi.config(text=f'hesapta {fatihhesap["bakiye"]} tl kaldı. ek hesapta {fatihhesap["ekHesap"]} tl kaldı.')
            else:
                yazi5.config(text=f'Hesapta {girilenTutar} tl bulunmuyor. Bu parayı çekemezsiniz!',fg="red",font=("Vertana",14))
        def paraYatir():
            global girilenTutar
            global fatihhesap
            tutar=entry1.get()        
            girilenTutar=int(tutar)
            yazi5.config(text="")
            fatihhesap["bakiye"] = girilenTutar+fatihhesap["bakiye"]
            yazi.config(text=f'Hesapta olan para: {fatihhesap["bakiye"]} / Ek hesapta olan para: {fatihhesap["ekHesap"]} ')        
        pencere.title("BANKAMATİK")
        pencere.geometry("800x600")
        yazi=tk.Label(pencere)
        yazi.config(text=f'Hesapta olan para: {fatihhesap["bakiye"]} / Ek hesapta olan para: {fatihhesap["ekHesap"]}',fg="green",font=("Vertana",14))    
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