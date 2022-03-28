import numpy as np
import matplotlib.pyplot as plt


# Exercise 3a)
class AffineTransform:
    """
    The class represent affine transformations.

    Attributes:
    -----------
    a, b, c, d, e, f    :   int
        Free parameters/coefficients in matrices (default 0)

    Special method:
    ---------------
    __call__(x, y)      :   float
        Take in x- and y-values and return the function f(x, y)

    """
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0):
        """
        The constructor of the class.

        Keyword arguments:
        ------------------
        a, b, c, d, e, f    :   int
            Free parameters/coefficients in matrices (default 0)
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, x, y):
        """
        Take in x- and y-values and return the function f(x, y)

        Computes the arrays A, xy_vec and ef_vec as matrices and then
        performing matrix multiplication between A and xy_vec and add the
        ef_vec to be able to return the linear function f_xy.
        """
        A = np.array([[self.a, self.b], [self.c, self.d]])
        xy_vec = np.array([x, y])
        ef_vec = np.array([self.e, self.f])
        f_xy = A @ xy_vec + ef_vec
        return f_xy


# Exercise 3c)
def select_func_prob(functions, p_cumulative):
    """
    Select function with corresponding probability and return function nr. j

    Set r as a random point in the interval r ∈ [0, 1), which maps to one of
    the four probabilities. Then iterating for index, j, and point, p, in
    p_cumulative (which is computed in the main block). Then the function
    return the chosen function with index j if r is less than p.
    """
    r = np.random.random()
    for j, p in enumerate(p_cumulative):
        if r < p:
            return functions[j]


# Exercise 3d)
def iterate(N):
    """
    Compute the next point and returning the current point.

    Set the point X to an array of zeros with shape (N, 2), i.e an N⨯2-matrix,
    with the starting point is X_0 = (0, 0). Then we iterate N - 1 points,
    where the next point is a randomly picked function according to their
    probability, and then return the array X with all the points which has
    been iterated.

    Argument:
    ---------
    N       :   int
        Number of iterations
    """
    X = np.zeros((N, 2))
    X[0] = (0, 0)
    for i in range(N - 1):
        X[i + 1] = select_func_prob(functions, p_cumulative)(X[i][0], X[i][1])
    return X


# Exercise 3e)
def plot(X):
    """
    Plot the Barnsley Fern figure.

    Parameter:
    ----------
    X       :   array
        An array of iterated points
    """
    plt.style.use('default')
    with plt.xkcd():
        plt.scatter(*zip(*X), s=0.02, c='forestgreen')
        plt.axis('equal')
        plt.savefig("figures/barnsley_fern.png")
        plt.show()


if __name__ == '__main__':
    # Exercise 3b)
    """
    Defining the functions f_1, f_2, f_3 and f_4 as affine transformation as
    instancec of the class.
    """
    f_1 = AffineTransform(d=0.16)
    f_2 = AffineTransform(a=0.85, b=0.04, c=-0.04, d=0.85, f=1.60)
    f_3 = AffineTransform(a=0.20, b=-0.26, c=0.23, d=0.22, f=1.60)
    f_4 = AffineTransform(a=-0.15, b=0.28, c=0.26, d=0.24, f=0.44)
    functions = [f_1, f_2, f_3, f_4]

    # Test to check that ∑(p_i) = 1 from exercise 3c)
    probabilities = [0.01, 0.85, 0.07, 0.07]
    total_prob = sum(probabilities)
    assert total_prob == 1

    p_cumulative = np.cumsum(probabilities)

    # Test example for exercise 3d)
    N = 50000
    points = iterate(N)
    print(points)

    # Test example for exercise 3f)
    fern = plot(points)
