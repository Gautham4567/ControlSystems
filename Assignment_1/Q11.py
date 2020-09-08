import numpy as np
import matplotlib.pyplot as plt
import control
import signal as sg

t = np.linspace(0,25,1000)
TF = control.TransferFunction([1], [1, 2, 3])
mag, ph, w = control.bode(TF)
T, y = control.step_response(TF, t, [-1, 1])
step = np.ones(T.shape)

plt.plot()
plt.grid()
plt.show()

plt.plot(T, y, label = 'Output')
plt.plot(T, step, label = 'Step')
plt.legend()
plt.grid()
plt.show()
