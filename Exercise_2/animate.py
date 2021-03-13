"""
Uses Visualize class instance to run matplotlib scripts.
The methods of the instance are passed to animation function.
The result is then plotted in a window.
"""

from visualizer import *

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plotter = Visualize(ax)
    ani = animation.FuncAnimation(fig, plotter.update, plotter.calculate, 
                                interval=50, blit=True)
    plt.show()
