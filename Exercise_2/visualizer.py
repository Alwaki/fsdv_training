import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Visualize:
    """
    Class which contains attributes to describe
    bounding of visualized plot and the data to be plotted.
    Also has methods for updating plot and calculating
    new values.
    """
    def __init__(self, ax, maxt=np.pi, dt=0.02):
        """Takes input axes of plot."""
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1400)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y):
        """Updates the plot boundaries and time/y data arrays."""
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,
    
    def calculate(self):
        """Calculates given periodic function for last time stamp"""
        yield 3 * np.pi * np.exp(-5*np.sin(2*np.pi*self.tdata[-1]))