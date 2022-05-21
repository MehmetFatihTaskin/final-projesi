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