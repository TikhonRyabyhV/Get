import matplotlib.pyplot as plt
import numpy as np

tmp = np.loadtxt("settings.txt", dtype = float)
freq = tmp[0]
step = tmp[1]
dt = 1 / freq


data = np.loadtxt("data.txt", dtype = int) 
T = dt * len( data )

data = data * ( 3.3 / 256 )
X = np.arange( 0, T, dt )

char_time = X[np.argmax(data)]
dischar_time = X[len(X) - 1] - char_time

fig, ax = plt.subplots(figsize = (16, 9), dpi = 200)
ax.plot( X, data, 'b',label = r"$U_{C}(t)$" + "\n\n" + "Charging time: " + "{:.3f}".format(char_time) + " sec" + "\nDischarging time: " + "{:.3f}".format(dischar_time) + " sec"  )

ax.set_xticks( np.arange( 0, T + 10, 10 ))
ax.set_yticks( np.arange( 0, 3.7, 0.5 ))
ax.set_xticks( np.arange( 0, T + 10, 2 ), minor = True)
ax.set_yticks( np.arange( 0, 4, 0.1 ), minor = True)

plt.xlim(0, 130)
plt.ylim(0.0, 3.5)

plt.xlabel("Time, sec")
plt.ylabel("Voltage, V")

plt.grid( which = 'major', linestyle = '-' )
plt.grid( which = 'minor', linestyle = '--' )

X_markers = np.arange( 0, T, 20*dt )
Y_markers = [data[i] for i in range(0, len(data), 20)]

plt.plot(X_markers, Y_markers, 'o')

plt.title("Process of charging and discharging of capacitor in RC-circuit" )
plt.legend()

plt.show()
fig.savefig('plot.svg')
