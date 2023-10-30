pilihan = int(input("""Silahkan pilih tools dibawah ini dengan mengirimkan nomornya
==============================
Tools yang tersedia
==============================
1. Menghitung luas persegi 
2. Menghitung luas lingkaran 
3. Menghitung luas segitiga 
==============================
Pilihanmu? """))

match pilihan :

    case 1 | "persegi" | "Persegi":
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas_persegi = sisi * sisi
        print("Luas persegi dengan panjang sisi", sisi, "adalah", luas_persegi)

    case 2 | "lingkaran" | "Lingkaran":
        jari2 = float(input("Masukkan panjang jari-jari lingkaran: "))
        luas_lingkaran = 3.14 * jari2 * jari2
        print("Luas lingkaran dengan jari-jari", jari2, "adalah", luas_lingkaran)

    case 3 | "segitiga" | "Segitiga":
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas_segitiga = 0.5 * alas * tinggi
        print("Luas segitiga dengan alas", alas, "dan tinggi", tinggi, "adalah", luas_segitiga)

    case _:
        print("Masukkan Inputan Yang Benar!")
