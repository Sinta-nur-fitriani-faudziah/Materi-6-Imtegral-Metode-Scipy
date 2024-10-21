# -*- coding: utf-8 -*-
"""untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/Sinta-nur-fitriani-faudziah/177d49d7ab74448efaf1fe2c22f45cd0/untitled3.ipynb
"""

# Import pustaka yang diperlukan
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# Batas-batas integral
x_start = 0
x_stop = np.pi

# Fungsi yang akan diintegralkan
def f(x):
    return x**2 * np.cos(x) + 3 * np.sin(2 * x)

# Menghitung integral dengan quad
integral, _ = integrate.quad(f, x_start, x_stop)

# Menampilkan hasil integrasi
print("Nilai Integral:", integral)

# Membuat array data x dan menghitung nilai y untuk plotting
x_values = np.linspace(x_start, x_stop, 1000)
y_values = f(x_values)

# Memplot kurva fungsi
plt.plot(x_values, y_values, label=r'$x^2 \cos(x) + 3 \sin(2x)$', color='blue')

# Mengisi area di bawah kurva (hasil integral)
plt.fill_between(x_values, y_values, color='orange', alpha=0.4)

# Menambahkan label dan judul pada grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik Fungsi $x^2 \cos(x) + 3 \sin(2x)$ dan Area di Bawah Kurva')
plt.legend()

# Menampilkan grafik
plt.show()