def gerbangA():
    tiket = input("Ada tiket? [Y/N] ")
    if tiket == "Y":
        jam = float(input("parkir berapa jam? "))
        if 0 < jam <= 24:
            print ("Tarif Parkir sejumlah Rp3.000,00-")
        elif jam >= 25:
            hari = float(input("Anda masuk tarif inap \nBerapa hari anda menginap?"))
            tarif = 25000 * hari
            print ("Tarif Parkir sejumlah Rp",tarif,",-")
        else: 
            typo = input("Typo Kali Bro? \nInput ulang? (Y/N)")
            if typo == "Y":
                gerbangA()
            else:
                 print("Terima kasih telah menggunakan sistem ini")
    elif tiket == "N":
        print("Anda terkena denda parkir sejumlah Rp50.000,00-")
    else: 
        typo = input("Typo Kali Bro? \nInput ulang? (Y/N)")
        if typo == "Y":
            gerbangA()
        else:
            print("Anda dikembalikan ke menu pertama")
                 
def gerbangB():
    roda = input("Roda berapa? \n[A] Roda 4 \n[B] Roda 6 \nInput = ")
    if roda == "A":
        roda4()
    elif roda == "B":
        roda6()
    else:
        typo = input("Typo Kali Bro? \nInput ulang? (Y/N)")
        if typo == "Y":
            gerbangB()
        else:
            print("Anda dikembalikan ke menu pertama")
                 
def roda4():
    tiket = input("Ada tiket? [Y/N] ")
    if tiket == "Y":
        jam = float(input("parkir berapa jam? "))
        if jam == 1:
            print ("Tarif Parkir sejumlah Rp6.000,00-")
        elif 1 < jam <= 5:
            tarif = 6000 + 2000 * (jam - 1)
            print ("Tarif Parkir sejumlah Rp",tarif,",-")
        elif 5 < jam <= 12:
            print ("Tarif Parkir sejumlah Rp25.000,00-")
        elif 12 < jam <= 24:
            print ("Tarif Parkir sejumlah Rp55.000,00-")
        else:
            hari = float(input("Anda masuk tarif inap \nBerapa hari anda menginap?"))
            tarif = 50000 * hari
            print ("Tarif Parkir sejumlah Rp",tarif,",-")
    elif tiket == "N":
        print("Anda terkena denda parkir sejumlah Rp100.000,00-")
    else:
        typo = input("Typo Kali Bro? \nInput ulang? (Y/N)")
        if typo == "Y":
            roda4()
        else:
            print("Anda dikembalikan ke menu pertama")

def roda6():
    tiket = input("Ada tiket? [Y/N] ")
    if tiket == "Y":
        jam = float(input("parkir berapa jam? "))
        if jam == 1:
            print ("Tarif Parkir sejumlah Rp8.000,00-")
        elif 1 < jam <= 5:
            tarif = 8000 + 3500 * (jam - 1)
            print ("Tarif Parkir sejumlah Rp",tarif,",-")
        elif 5 < jam <= 12:
            print ("Tarif Parkir sejumlah Rp35.000,00-")
        elif 12 < jam <= 24:
            print ("Tarif Parkir sejumlah Rp70.000,00-")
        else:
            hari = float(input("Anda masuk tarif inap \nBerapa hari anda menginap?"))
            tarif = 70000 * hari
            print ("Tarif Parkir sejumlah Rp",tarif,",-")
    elif tiket == "N":
        print("Anda terkena denda parkir sejumlah Rp100.000,00-") 
    else:
        typo = input("Typo Kali Bro? \nInput ulang? (Y/N)")
        if typo == "Y":
            roda6()
        else:
            print("Terima kasih telah menggunakan sistem ini")

while True :
    print("")
    print("")
    print("===============================")
    print("    GERBANG KELUAR BANDARA     ")
    print("-------------------------------")
    print("         TARIF PARKIR          ")
    print("===============================")
    print("[A] Lewat Gerbang Motor")
    print("[B] Lewat Gerbang Mobil")
    gerbang = input("Tadi lewat jalur gerbang mana?(Tekan sembarang jika ingin keluar) \nInput = ")
    if gerbang == "A":
        gerbangA()
    elif gerbang == "B":
        gerbangB()
    else:
        print("Terima kasih telah menggunakan sistem ini")
        break
