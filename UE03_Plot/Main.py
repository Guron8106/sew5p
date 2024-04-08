import math

import matplotlib.pyplot as plt
import numpy as np

CNT = 1024
PI = math.pi

X = [-PI + ((2*PI)*i / (CNT-1)) for i in range(CNT)]
C = [math.cos(x) for x in X]
S = [math.sin(x) for x in X]

def plot():
    """
    Drawing PI Plot
    :return: plot
    """
    plt.figure(figsize=(10,6), dpi=80)
    plt.xlim(min(X) * 1.1, max(X) * 1.1)
    plt.ylim(min(C) * 1.1, max(C) * 1.1)
    plt.xticks([-PI, -PI / 2, 0, PI / 2, PI],
               [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    plt.yticks([-1, 0, +1],
               [r'$-1$', r'$0$', r'$+1$'])

    # Aufgabe 1 Linienart und Farbe
    plt.plot(X,C, color="gold", linewidth=2.5, linestyle='-.', label="cosine")
    plt.plot(X,S, color="green", linewidth=2.5, linestyle='-.', label="sine")



    plt.legend(loc='upper left', frameon=False)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    t = 2 * PI / 3
    plt.plot([t, t], [0, math.cos(t)], color='brown', linewidth=2.5, linestyle="--")
    plt.scatter([t, ], [math.cos(t), ], 50, color='brown')
    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                 xy=(t, math.sin(t)), xycoords='data',
                 xytext=(+10, +30), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t, t], [0, math.sin(t)], color='green', linewidth=2.5, linestyle="--")
    plt.scatter([t, ], [math.sin(t), ], 50, color='green')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                 xy=(t, math.cos(t)), xycoords='data',
                 xytext=(-90, -50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    t_34 = math.radians(45)
    plt.plot([t_34, t_34], [0, math.cos(t_34)], color='red', linewidth=2.5, linestyle="--")
    plt.scatter([t_34, ], [math.cos(t_34), ], 50, color='red')
    plt.annotate(r'$\sin(45°)=\frac{\sqrt{2}}{2}$',
                 xy=(t_34, math.sin(t_34)), xycoords='data',
                 xytext=(+10, +50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    t_34m = math.radians(-45)
    plt.plot([t_34m, t_34m], [0, math.cos(t_34m)], color='red', linewidth=2.5, linestyle="--")
    plt.scatter([t_34m, ], [math.cos(t_34m), ], 50, color='red')
    plt.annotate(r'$\sin(45°)=\frac{\sqrt{2}}{2}$',
                 xy=(t_34m, math.sin(t_34m)), xycoords='data',
                 xytext=(+10, +50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t_34m, t_34m], [0, math.sin(t_34m)], color='red', linewidth=2.5, linestyle="--")
    plt.scatter([t_34m, ], [math.cos(t_34m), ], 50, color='red')
    plt.annotate(r'$\sin(45°)=\frac{\sqrt{2}}{2}$',
                 xy=(t_34m, math.sin(t_34m)), xycoords='data',
                 xytext=(+10, +50), textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    ax.set_axisbelow(True)

    #Titelzeile
    ax.set_title("Plot von Karanbir Guron, HTL3R", fontsize=20)


    ax.quiver(np.pi + 0.25, 0, 0.2, 0, angles='xy', scale_units='xy', scale=1, color="black", clip_on=False)
    ax.quiver(0, 1.0, 0, 0.12, angles='xy', scale_units='xy', scale=1, color="black", clip_on=False)

    plt.savefig("pi.png", dpi=80)
    plt.show()

if __name__ == "__main__":
    plot()