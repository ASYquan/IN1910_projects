import numpy as np
import matplotlib.pyplot as plt
from chaos_game import ChaosGame


# Exercise 4a)
class Variations:
    """
    A class which alters the appereance of figures

    Attributes
    ----------
    x     : array_like
            x coordinates
    y     : array_like
            y coordinates
    name  : string
            name of variation to be used
    _func : function-type
            function that transforms the coordinates

    Methods
    -------
    linear(x, y)
        Return arrays x and y
    handkerchief(x, y)
        Returns computation of the handkerchief formula
    swirl(x, y)
        Returns computation of the swirl formula
    disc(x, y)
        Returns computation of the disc formula
    power(x, y)
        Returns computation of the power formula
    exponential()
        Returns computation of the exponential formula
    transform()
        Method that uses _func to retrieve static-method and returns
        the transformed coordinates.
    from_chaos_game(instance, name)
        Alternative method to create class-instance.
        Uses the iterateded values from an instance of ChaosGame-class
        as x- and y-coordinates.
    from_chaos_game(cls, instance, name)
        Take an instance of ChaosGame and return an instance of Variations
    """

    def __init__(self, x, y, name):
        """
        Parameters
        ----------
        x    : numpy.array or array_like
                The X coordinates.
        y    : numpy.array or array_like
                The Y coordinates.
        name : string
                string which specifies staticmethod
        _func: function
                uses the name-variable to retrieve staticmethod
        """
        self.x = x
        self.y = y
        self.name = name
        self._func = getattr(Variations, name)

    @staticmethod
    def linear(x, y):
        """Return the arrays x and y"""
        return x, y

    @staticmethod
    def handkerchief(x, y):
        """
        Compute the handkerchief formula and return the computed value.

        Parameters:
        -----------
        x       :   array
        An array of values for x in staticmethod
        y       :   array
            An array of values for y staticmethods
        """
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(x, y)
        return r * (np.sin(theta + r)), r * (np.cos(theta - r))

    @staticmethod
    def swirl(x, y):
        """
        Compute the swirl formula and return the computed value.

        Parameters:
        -----------
        x       :   array
        An array of values for x in staticmethod
        y       :   array
            An array of values for y staticmethods
        """
        r = np.sqrt(x ** 2 + y ** 2)
        return x * np.sin(r ** 2) - y * np.cos(r ** 2), \
            x * np.cos(r ** 2) + y * np.sin(r ** 2)

    @staticmethod
    def disc(x, y):
        """
        Compute the disc formula and return the computed value.

        Parameters:
        -----------
        x       :   array
        An array of values for x in staticmethod
        y       :   array
            An array of values for y staticmethods
        """
        theta = np.arctan2(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        return (theta / np.pi) * (np.sin(np.pi * r), np.cos(np.pi * r))

    @staticmethod
    def power(x, y):
        """
        Compute the power formula and return the computed value.

        Parameters:
        -----------
        x       :   array
        An array of values for x in staticmethod
        y       :   array
            An array of values for y staticmethods
        """
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(x, y)
        return (r ** np.sin(theta)) * (np.cos(theta), np.sin(theta))

    @staticmethod
    def exponential(x, y):
        """
        Compute the exponential formula and return the computed value.

        Parameters:
        -----------
        x       :   array
        An array of values for x in staticmethod
        y       :   array
            An array of values for y staticmethods
        """
        return np.exp(x - 1) * (np.cos(np.pi * y), np.sin(np.pi * y))

    def transform(self):
        """Return a static method with x- and y-values from the constructor."""
        return self._func(self.x, self.y)

    @classmethod
    def from_chaos_game(cls, instance, name):
        """
        Take an instance of ChaosGame and return an instance of Variations

        Parameters:
        -----------
        instance    :   ChaosGame-instance
            An object of ChaosGame
        name        :   string
            Takes in a string, which speicifies staticmethod to use
        """
        instance._starting_point()
        instance.iterate(10000)
        X = instance.X
        cls.C = instance.gradient_color
        return cls(X[:, 0], -X[:, 1], name)


# Exercise 4d)
def linear_combination_wrap(V1, V2):
    """
    Return a linear combination of two instances of the Variations-class.

    Parameters:
    -----------
    V1  :   any
        Variation 1 of a linear combination
    V2  :   any
        Variation 2 of a linear combination
    """
    u1, v1 = V1.transform()
    u2, v2 = V2.transform()

    def lin_comb(w):
        """
        The linear combination which consists of two Variations-class objects.
        Argument:
        w   :   any
            A weight/coefficient between 0 and 1
        """
        u, v = w * u1 + (1 - w) * u2, w * v1 + (1 - w) * v2

        return u, v

    return lin_comb


if __name__ == "__main__":
    # Exercise 4b)
    grid_values = np.linspace(-1, 1, 150)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()

    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [
        Variations(x_values, y_values, version) for version in transformations
    ]
    with plt.xkcd():
        fig, axs = plt.subplots(2, 2, figsize=(9, 9))
        for i, (ax, variation) in enumerate(zip(axs.flatten(), variations)):
            u, v = variation.transform()
            ax.plot(u, -v, ms=1, m=".", ls="", c="black")
            ax.scatter(u, -v, s=0.2, marker=".", color="black")
            ax.set_title(variation.name)
            ax.axis("off")
    fig.savefig("figures/variations_4b.png")
    plt.show()

    # Exercise 4c)
    obj = ChaosGame(4, 1 / 3)
    transformations = [
        "linear",
        "handkerchief",
        "swirl",
        "disc",
        "exponential",
        "power",
    ]
    with plt.xkcd():
        fig, axs = plt.subplots(3, 2, figsize=(9, 9))
        for i, ax in enumerate(axs.flatten()):
            variation = Variations.from_chaos_game(obj, transformations[i])
            u, v = variation.transform()
            colors = variation.C
            ax.scatter(u, -v, s=0.2, marker=".", c=colors)
            # ax.scatter(u, -v, s=0.2, marker=".", color="black")
            ax.set_title(variation.name)
            ax.axis("off")
    plt.show()

    # Exercise 4d - test)
    coeffs = np.linspace(0, 1, 4)
    ngon = ChaosGame(4, 1 / 3)
    variation1 = Variations.from_chaos_game(ngon, "linear")
    variation2 = Variations.from_chaos_game(ngon, "disc")

    variation12 = linear_combination_wrap(variation1, variation2)
    with plt.xkcd():
        fig, axs = plt.subplots(2, 2, figsize=(9, 9))
        for ax, w in zip(axs.flatten(), coeffs):
            u, v = variation12(w)
            n_color = "black"
            ax.scatter(u, -v, s=0.2, marker=".", c=n_color)
            ax.set_title(f"weight = {w:.2f}")
            ax.axis("off")

    plt.show()
