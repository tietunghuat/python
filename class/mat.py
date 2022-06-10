import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax1 = fig.add_subplot(111)
t = np.arange (0.01, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1,"b-")
ax1.set_xlabel ("time (s) ")
# Make the y-axis label and tick labels match the line color
ax1.set_ylabel("exp", color="y")
for tl in ax1.get_yticklabels():
    tl.set_color ("b")

ax2 = ax1. twinx()
s2 = np.sin(2*np.pi*t)
ax2.plot(t, s2,"g.")
ax2.set_ylabel("sin",color="g")
for tl in ax2.get_yticklabels():
    tl.set_color ("y")
plt.show()



# plt.plot([1,2,3,4,5],[2,3,4,6,8],color="purple",linestyle="dashed",marker=">")
# plt.ylabel("y axis")
# plt.xlabel("x axis")
# plt.show()
