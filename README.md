# P1_Komnum_B-12
## Praktikum 1 Komputasi Numerik : Metode Bolzano

| **No** | **Nama** | **NRP** | 
| :-------------: | ------------- | :---------: |
| 1 | Adhira Riyanti Amanda  | 5025211102 | 
| 2 | Gabriella Natasya Br Ginting | 5025211081 |
| 3 | Cavel Ferrari | 5025211198 |

### **Dokumentasi Hasil**
- Tabel
** screenshot
- Grafik 
** screenshot

### **Penjelasan Hasil Praktikum**
Program ini adalah implementasi algoritma dari metode Bolzano yang dimana metode Bolzano merupakan metode **Setengah Interval (*Interval Halving*)**.<br><br>
Metode ini dilakukan dengan cara mencari nilai titik tengah dari suatu *range* yang ditentukan. Nilai titik tengah tersebut dicari dengan tujuan untuk mendapatkan nilai f(x) yang mendekati angka nol. Apabila hasil f(x) yang didapatkan mendekati angka nol ataupun hampir mencapai angka nol, dapat disimpulkan bahwa nilai titik tengah tersebut merupakan akar persamaan.<br><br>
Algoritma yang didapatkan untuk mencari akar persamaan dengan metode Bolzano, sebagai berikut : <br>
**Keterangan :** <br>
xi = titik awal range yang diasumsikan<br>
xi+1 = titik akhir range yang diasumsikan<br>
xt = titik tengah <br>
**Rumus untuk mencari xt**<br>
**xt** = ( xi + xi+1 ) / 2<br>
**Langkah-langkah:**<br>

1. Hitung fungsi pada range yang diasumsikan hingga terjadi **perubahan tanda** dari f(xi) dan f(xi+1). Sehingga f(xi) * f(xi+1) < 0
2. Cari estimasi pertama akar persamaan (xt)
3. Lakukan evaluasi untuk menentukan akar persamaan berada pada interval mana :
- Jika **f(xi) * f(xi+1) < 0** = akar persamaan berada dalam sub-interval pertama, maka terapkan **xi+1 = xt**
- Jika **f(xi) * f(xi+1) > 0** = akar persamaan berada dalam sub-interval kedua, maka terapkan **xi = xt**
- Jika **f(xi) * f(xi+1) = 0** = akar persamaan adalah xt, dan perhitungan selesai
4. Kembali ke langka 2 untuk mencari nilai perkiraan akar yang baru
5. Jika nilai yang didapat pada langkah keempat sudah sesuai dengan batasan yang ditentukan, maka proses selesai dan xt adalah akar yang dicari.

Dengan algoritma diatas, diterapkan pada pemograman praktikum.py dengan ketentuan berikut :
- Range yang diasumsikan diinput dengan syarat f(xi) * f(xi+1) < 0
- Persamaan harus di modifikasi secara manual pada program
- Dapat menyelesaikan akar persamaan dari persamaan polinomial, trigonometri, eksponensial.






