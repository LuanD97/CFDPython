import matplotlib.pyplot as plt
import numpy as np

# differencing schemes to approximate the true shape of the underlying function
# the more the number of discretisation, the smaller the error between the approximated line and the actual function.
# Backward difference: approximate using x_i and x_(i-1)
# forward difference: use x_i and x_(i+1)
# central difference: use x_(i-1) and x_(i+1)

nx = 80  # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (nx - 1)
nt = 25  # nt is the number of timesteps we want to calculate
dt = 0.025  # dt is the amount of time each timestep covers (delta t)
c = 1  # assume wavespeed of c = 1

u = np.ones(nx)  # numpy function ones()
u[int(0.5 / dx) : int(1 / dx + 1)] = (
    2  # setting u = 2 between 0.5 and 1 as per our I.C.s
)

plt.plot(np.linspace(0, 2, nx), u)

# temporary array for n+1 timestep
un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(1, nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

plt.plot(np.linspace(0, 2, nx), u)
plt.show()
