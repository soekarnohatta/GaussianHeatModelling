# Pemecahan kasus persamaan  diferensial
# melalui penggunaan metode manual maupun perbantuan
# modul tertentu sebagai tugas UTS
#
# Nayef Haidir - 225090300111014
# MK: Bahasa dan Algoritma
import numpy as np
import matplotlib.pyplot as plot

# Tulis param
T = 2.0
num_steps = 50
dt = T / num_steps

# Bikin mesh
nx, ny = 30, 30
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

def boundary(x):
    return np.logical_or(np.abs(x[0]) < 1E-14, np.abs(x[1]) < 1E-14)

# Nilai awal
a = 5
u_n = np.exp(-a * (X**2 + Y**2))
u_values = [u_n]

t = 0
for n in range(num_steps):
    t += dt

    # Mulai perhitungan
    u = u_n + dt * (np.gradient(u_n, axis=(0, 1), edge_order=1)[0] +
                    np.gradient(u_n, axis=(0, 1), edge_order=1)[1])
    u_values.append(u)
    u_n = u

# Plot ke gambar
for n, u in enumerate(u_values):
    plot.figure()
    plot.contourf(X, Y, u, cmap='viridis')
    plot.colorbar()
    plot.title('t = {:.2f}'.format(n * dt))
    plot.xlabel('X')
    plot.ylabel('Y')
    plot.gca().invert_yaxis()

plot.show()
