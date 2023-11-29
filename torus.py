import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
    }
)

n = int(input("Enter in the n value of the torus: "))

u = np.linspace(0, (2 * np.pi), n)
v = np.linspace(0, (2 * np.pi), n)
u, v = np.meshgrid(u, v)
c, a = 2, 1 # Edit the c and a values on this line
x = (c + (a * np.cos(v))) * np.cos(u)
y = (c + (a * np.cos(v))) * np.sin(u)
z = a * np.sin(v)

figure = plt.figure()

ax = figure.add_subplot(111, projection="3d", facecolor="green")

ax.plot_surface(x, y, z, alpha=0.5)

ax.set_xlabel("𝑥")
ax.set_ylabel("𝑦")
ax.set_zlabel("𝑧")

ax.set_title("Torus Visualized")

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

plt.show()