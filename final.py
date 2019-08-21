print("====================================TRI-FLEK COWORKING SPACE=========================================")
print("[Sign Up]")

nama = input("Masukan namamu: ") # Halo, <nama!>! Selamat datang di COWORKING!
print('Halo '+nama+'! Selamat Datang di Tri-Flek Coworking Space\n')

# input 
org = int(input('Jumlah orang: '))

jumlah_pintu = float(input('Jumlah Pintu: '))
panjang_pintu = float(input('Panjang Pintu: '))
lebar_pintu = float(input('Lebar Pintu: '))

jumlah_jendela = float(input('Jumlah Jendela: '))
panjang_jendela = float(input('Panjang Jendela: '))
lebar_jendela = float(input('Lebar Jendela: '))

luas_org = 2 # meter persegi
tinggi_tembok = 3 # meter
panjang_bata = 0.5 # meter
lebar_bata = 0.5 # meter
sisi_keramik = 1 # meter

def hitung_luas_lantai_total():
    luas_lantai_total = org*luas_org # meter persegi
    return luas_lantai_total

def hitung_jumlah_keramik(sisi_keramik,luas_lantai_total,luas_keramik_solo):
    luas_keramik_solo = sisi_keramik*sisi_keramik # meter persegi
    jumlah_keramik = luas_lantai_total/luas_keramik_solo # jumlah
    return jumlah_keramik

# hitung jumlah bata dari luas tembok total (4 sisi), dikurangi pintu dan jendela
def hitung_luas_pintu(panjang_pintu,lebar_pintu):
    luas_pintu = panjang_pintu*lebar_pintu # meter persegi
    return luas_pintu

def hitung_luas_jendela(lebar_jendela,panjang_jendela):
    luas_jendela = lebar_jendela*panjang_jendela # meter persegi
    return luas_jendela

def hitung_luas_tembok_asli():
    panjang_sisi_tembok = 5 # meter
    luas_tembok_total = panjang_sisi_tembok*panjang_sisi_tembok # meter persegi
    luas_tembok_asli = luas_tembok_total - jumlah_pintu*luas_pintu - jumlah_jendela*luas_jendela # meter persegi
    return luas_tembok_asli

def hitung_jumlah_bata(luas_tembok_asli,lebar_bata,panjang_bata):
    luas_bata_solo = panjang_bata*lebar_bata # meter persegi
    jumlah_bata = luas_tembok_asli/luas_bata_solo # jumlah
    return jumlah_bata


# estimasi harga
harga_bata_solo = 5000
harga_keramik_solo = 30000
profit = 20000

def hitung_harga_bangunan(harga_bata_solo,harga_keramik_solo):
    harga_bata_total = harga_bata_solo*hitung_jumlah_bata
    harga_keramik_total = harga_keramik_solo*hitung_jumlah_keramik
    return harga_bangunan

def hitung_harga_jual(profit,harga_jual):
    harga_jual = profit # berapa yang harus kamu jual agar tidak rugi? agar mendapatkan keuntungan?
    return harga_jual


# run all the functions
luas_lantai_total = hitung_luas_lantai_total()
jumlah_keramik = hitung_jumlah_keramik(sisi_keramik,luas_lantai_total,luas_keramik_solo)
luas_pintu = hitung_luas_pintu(panjang_pintu,lebar_pintu)
luas_jendela = hitung_luas_jendela(lebar_jendela,panjang_jendela)
luas_tembok_asli = hitung_luas_tembok_asli()
jumlah_bata = hitung_jumlah_bata(luas_tembok_asli,lebar_bata,panjang_bata)
harga_bangunan = hitung_harga_bangunantung_harga(harga_bata_solo,harga_keramik_solo)
harga_jual = hitung_harga_jual(profit,harga_jual)


print("===========================================================================================")
print('Jumlah bata yang dibutuhkan: '+str(jumlah_bata))
print('Jumlah keramik yang dibutuhkan: '+str(jumlah_keramik))
print('Harga total yang harus dibayar: '+str(harga_jual))                      

print("================================Thanks For Using COWORKING!======================")
