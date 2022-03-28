import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    """
    A class which generalized the Chaos Game.

    Attributes
    ----------
    n       : int
                n-amounts of edges
    r       : float, optional
                Ratio between two corners
    corners : numpy.array
                List of coordinates for n-corners
    X_0     : numpy.array
                Picks a random starting point within n-gon
    X       : numpy.array
                Generated points from starting point
    index   : numpy.array
                Array of corner index of the i-th iteration, 𝑗_i
    C       : numpy.array
                Array of gradient color values

    Methods
    -------
    _generate_ngon()
        generates an array of coordinates for n-gons.
    plot_ngon()
        plots the coordinates of the corners in xkcd style
    _starting_point()
        generates a startingpoint within the n-gon
    iterate(steps, discard)
        generates two arrays of coordinates, and the indexes of corners
    plot(color, cmap)
        plots the iterated coordinates with or without colors.
    show(color, cmap)
        plots and shows the coordinates with, or without colors.
    gradient_color()
        Returns an array that cointains gradient colors for the plot-method
    savepng(outfile, color, cmap)
        creates and saves a plot as an png with an arbitrarly chosen name.
    """

    def __init__(self, n, r=1 / 2):
        """Specifies n-edges and a ratio (default : 1/2) and generates corners

        Parameters
        ----------
        n : int
                Specifies the amount of corners
        r : float, optional
                Specifies the ratio between two corners.
                Default set to 1/2.
        """
        if not isinstance(n, int) or n < 3:
            raise ValueError(
                "input is not a valid number.Must be an integer and n<=3"
            )

        if not isinstance(r, float) or ((r < 0) or (r > 1)):
            raise ValueError(
                "input value is not valid.Must be between 0 and 1, and a float"
            )
        self.n = n
        self.r = r
        self._generate_ngon()

    # Exercise 2b)
    def _generate_ngon(self):
        """Generates an array, stores it in the class-object

        First, the function finds n equally distributed angles, and
        computes the corners with parametric equations.
        """
        n = self.n
        theta_i = np.linspace(0, 2 * np.pi, n + 1)
        self.corners = np.zeros((n, 2))
        for i in range(n):
            self.corners[i] = (np.sin(theta_i[i]), np.cos(theta_i[i]))

    def plot_ngon(self):
        """Plots the generated corners in xkcd-style"""
        with plt.xkcd():
            fig, ax = plt.subplots()
            ax.axis("equal")
            ax.scatter(*zip(*self.corners), c="mediumseagreen", ec="seagreen")

    # Exercise 2c)
    def _starting_point(self):
        """Creates an array, and stores it within the class-object

        The function will pick a starting-point: X_0, which is chosen
        within the n-corners. It will generate a starting-point by
        generating n random weights from [0,1), and scales them such that
        the sum is equal 1. Then it computes the linear combination of the
        scales weights and the corners. It then stores the starting-point in
        the class-object.
        """
        n = self.n
        corners = self.corners
        w_i = np.random.random(size=n)
        w_sum = sum(w_i)
        w_scale = w_i / w_sum
        self.X_0 = w_scale @ corners

    # Exercise 2d)
    def iterate(self, steps, discard=5):
        """Generate and store an array of points, and indecies in class-object.

        Uses the starting-point and computes the next point, and iterates an
        arbitrarily amount of times. For each iteration it will store the index
        of the randomly chosen corner, and the computed point in two
        seperate arrays which are stored in the class-object.

        Parameters
        ----------
        steps   : int
                    Specifies how many iterations will be done
        discard : int, optional
                    Discards a set of points from 0 to a arbitrarily chosen
                    number. Default is set to 5.
        """
        X_0 = self.X_0
        n = self.n
        r = self.r
        X = np.zeros((steps, 2))
        indices = np.zeros(steps)
        X[0] = X_0

        for i in range(steps - 1):
            j = np.random.randint(n)
            X[i + 1] = r * X[i] + (1 - r) * self.corners[j]
            indices[i + 1] = j
        self.X = X[discard:]
        self.index = indices[discard:]

    # Exercise 2e)
    def plot(self, color=False, cmap="jet"):
        """Plots the n-gon and all its iterated points

        Plots all the points generated from the iterate-method, which are
        stored in an array within the class-object. It plots in the xkcd-style.
        The points can be plotted with or without colors.

        Parameters
        ----------
        color : boolean, optional
                    Specify True, or False for colors
                    Default set to False.
        cmap  : string, optional
                    Specifies which colormap to use from the
                    matplotlib.pyplot package.
                    Default set to jet.
        """
        if color:
            # colors = self.index           # value for colors in 2e)
            colors = self.gradient_color  # value for colors in 2f)
        else:
            colors = "black"

        with plt.xkcd():
            fig, ax = plt.subplots()
            ax.axis("equal")
            ax.scatter(*zip(*self.X), c=colors, cmap=cmap, marker='.')

    def show(self, color=False, cmap="jet"):
        """Shows the created plot from plot-method

        Call the plot-method, in order to create a plot of the iterated points.
        In addition shows the generated plot by including plt.show().

        Parameters
        ----------
        color : boolean, optional
                    Specify True, or False for colors
                    Default set to False.
        cmap  : string, optional
                    Specifies which colormap to use from the
                    matplotlib.plt package.
                    Default set to jet.
        """
        self.plot(color=color, cmap=cmap)
        plt.show()

    # Exercise 2f)
    @property
    def gradient_color(self):
        """Returns a numpy.array

        Generated and returns a list of gradient color values corresponding
        to the iterated value: X, from iterate-method.
        The colors values will depend on the previous color value, and the
        corner index of the i-th iteration, j_i.
        """
        j = self.index
        C = np.zeros(len(self.index))
        C[0] = j[0]
        for i in range(len(j) - 1):
            C[i + 1] = (C[i] + j[i + 1]) / 2
        return C

    # Exercise 2g)
    def savepng(self, outfile, color=False, cmap="jet"):
        """Creates and saves a plot of the iterated values

        Generate a plot of the the iterated values: X, from the iterate-method.
        It will check if the input is the correct type, and it will save
        the plot as a .png-file.

        Parameters
        ----------
        outfile :  string
                    Input for name of file.
        color   :  boolean, optional
                    True or False statement regarding color-choice
                    Default set to False
        cmap    :  string, optional
                    Input for specified colormap from the matplotlib.pyplot-
                    package.
                    Default set to "jet".

        """
        if isinstance(outfile, str) is not True:
            raise TypeError("Input must be string")

        elif outfile.lower().endswith(".png"):
            self.plot(color=color, cmap=cmap)
            plt.savefig(outfile, dpi=100, format="png")

        elif outfile.lower().endswith(".png") is not True:
            for letter in outfile:
                if letter == ".":
                    raise TypeError("filetype must have .png suffix")
                    break
                continue
            self.plot(color=color, cmap=cmap)
            plt.savefig(outfile, dpi=100)


if __name__ == "__main__":
    # Test example for exercise 2b)
    for i in range(3, 9):
        test = ChaosGame(i)
        test.plot_ngon()
        plt.suptitle("Plots for exercise 2b)", size=16)
        plt.title(f"Test for n = {i}", size=12)
        plt.show()

    # Test example for exercise 2c)
    pentagon = ChaosGame(5)
    pentagon.plot_ngon()
    N = 1000
    for _ in range(N):
        pentagon._starting_point()
        plt.scatter(*zip(pentagon.X_0))
    plt.suptitle("Exercise 2c")
    plt.title(f"{N} plots of points forming within a pentagon")
    plt.axis("equal")
    plt.show()

    # Test example for exercise 2e) and 2f)
    color_tri = ChaosGame(3)
    color_tri._starting_point()
    color_tri.iterate(10000)
    color_tri.show()
    color_tri.show(color=True)
    plt.title("show-method with color = True")

    # Test example for exercise 2g)
    color_tri.savepng("test.png", color=True)

    # Exercise 2i)
    val = np.array(
        [[3, 1 / 2], [4, 1 / 3], [5, 1 / 3], [5, 3 / 8], [6, 1 / 3]]
    )
    for i in range(len(val)):
        n = int(val[i][0])
        r = val[i][1]
        outfile = f"figures/Chaos{i+1}.png"
        obj = ChaosGame(n, r)
        obj._starting_point()
        obj.iterate(10000)
        obj.savepng(outfile, color=True)
