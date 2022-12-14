# Praktikum 1 - Komputasi Numerik B - Kelompok 12
# Anggota :
# Adhira Riyanti Amanda - 5025211102
# Gabriella Natasya Br Ginting  - 5025211081
# Cavel Ferrari - 5025211198

import matplotlib.pyplot as plt
import numpy as np
import tabulate as tb
import math

# Membuat Array untuk nilai x1,x2,x3 dan f(x1),f(x2),f(x3)
x1_list = np.array([])
fx1_list = np.array([])
x2_list = np.array([])
fx2_list = np.array([])
x3_list = np.array([])
fx3_list = np.array([])

# Mendefinisikan fungsi persamaan
def func(x):
        return pow(x,3) + pow(x,2) - 3*x - 3
        # return pow(x,3)- 3*x + 1
        # return math.cos(x) - 3x
        # return pow(10,x)-100+2*x
        # return np.log(x) - 1 - 1/pow(x,2)
        # return math.exp(x) - np.log(x) - 20
        # return pow(10,x)-1

# Menggunakan Metode Bolzano untuk mencari akar persamaan 
def BolzanoMethod(a,b):

    # Mendeklarasikan variabel global
    global x1_list, fx1_list, x2_list, fx2_list, x3_list, fx3_list
  
    while ((b-a) >= 0.00001):

        x1_list = np.insert(x1_list,len(x1_list),a)
        x2_list = np.insert(x2_list,len(x2_list),b)
        fx1_list = np.insert(fx1_list,len(fx1_list),func(a))
        fx2_list = np.insert(fx2_list,len(fx2_list),func(b))
 
        # Mencari titik tengah
        c = (a+b)/2
        x3_list = np.insert(x3_list,len(x3_list),c)
        fx3_list = np.insert(fx3_list,len(fx3_list),func(c))

        # Mengecek apakah titik tengah merupakan akar persamaan
        if (fx3_list[len(fx3_list)-1] == 0.0):
            break
  
        # Iterasi perulangan
        if (fx3_list[len(fx3_list)-1]*fx1_list[len(fx1_list)-1] < 0):
            b = c
        else:
            a = c
             
    print("\nNilai akar persamaan : ","%.5f"%c)

# Input nilai interval
print ('Masukkan interval nilai akar persamaan :')
print ('x1 = ', end='')
a = int(input ())
print ('x2 = ', end='')
b = int(input ())

# Mengecek apakah persamaan terdapat dalam interval a sampai b
while (func(a) * func(b) >= 0):
        print("Kamu memasukkan interval yang kurang tepat\n")
        print ('Masukkan kembali interval nilai akar persamaan :')
        print ('x1 = ', end='')
        a = int(input ())
        print ('x2 = ', end='')
        b = int(input ())

# Mencari akar persamaan menggunakan metode Bolzano
BolzanoMethod(a, b)

# Membuat figur baru untuk grafik persamaan
plt.figure("Grafik Metode Bolzano", dpi = 120)
plt.title("Metode Bolzano")

plt.xlim(-100, 100)
plt.ylim(-100, 100)

# Membuat grafik persamaan
graph_x = np.linspace(-100, 100, num = 10000)
graph_y = np.vectorize(func)
graph_y = graph_y (graph_x)

plt.plot(graph_x,graph_y, label="f(x)")

# Membuat garis x-axis dan y-axis
axis_list = np.linspace(-100, 100, num = 1000)
zeros_list = axis_list * 0

plt.plot(axis_list, zeros_list, 'k--')
plt.plot(zeros_list, axis_list, 'k--')

# Menandai lokasi titik titik tengah
plt.scatter(x3_list,fx3_list, color = 'red', label = "middle point")

for x,y in zip(x3_list,fx3_list):
    label = ("{:.4f}".format(x),"{:.4f}".format(y))
    plt.annotate(
                label, 
                (x,y),
                textcoords = "offset points",
                xytext=(0,10),
                ha = 'center'
                )

# Membuat tabel iterasi
set_value = {'X1': x1_list, 'X2': x2_list, 'X3': x3_list, 'F(X1)': fx1_list, 'F(X2)': fx2_list,'F(X3)': fx3_list}
print(tb.tabulate(set_value, headers = 'keys', tablefmt='fancy_grid', numalign = 'center', showindex=range(1,len(x1_list)+1)))

# Menambahkan tampilan legend pada figur grafik
plt.legend()

# Menampilkan grafik yang telah terbuat
plt.show()