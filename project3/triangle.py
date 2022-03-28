import numpy as np
import matplotlib.pyplot as plt


# Exercise 1a)
def get_point(p1, p2):
    """
    Get the third point and return the positive and negative x- and y-values.

    Parameters:
    -----------
    p1 -- point 1 (x, y)
    p2 -- point 2 (x, y)
    """
    mid_point_x = (p1[0] + p2[0]) / 2
    mid_point_y = (p1[1] + p2[1]) / 2
    origin_x = (p1[0] - mid_point_x) * (3 / 2)
    origin_y = (p1[1] - mid_point_y) * (3 / 2)

    x_point_pos = mid_point_x + origin_y
    y_point_pos = mid_point_y - origin_x
    x_point_neg = mid_point_x - origin_y
    y_point_neg = mid_point_y + origin_x

    return x_point_pos, y_point_pos, x_point_neg, y_point_neg


c_0 = (0, 0)
c_1 = (1, 0)
c_2 = get_point(c_0, c_1)
print(f"The third point is: {c_2[:2]} or {c_2[2:]}")

# Define all the corners as an array
corners = np.array([[0, 0], [1, 0], [1 / 2, 3 / 4]])


def plot_3_points():
    """Plot the corners of an equilateral triangle."""

    # Choosing the triangle with positive y-value
    plt.grid(axis='both', which='major', c='silver', ls='-', lw=1)
    plt.minorticks_on()
    plt.grid(axis='both', which='minor', c='gainsboro', ls=':', lw=1)
    plt.scatter(*zip(*corners), c='mediumseagreen', ec='seagreen')

    plt.plot([0, 1, 1 / 2, 0], [0, 0, 3 / 4, 0], c='mediumseagreen')

    plt.text(
        corners[0][0] + 0.02,
        corners[0][1],
        rf'$c_0 = $({int(corners[0][0])}, {int(corners[0][1])})',
        ha='left',
        va='bottom')
    plt.text(
        corners[1][0] - 0.03,
        corners[1][1],
        rf'$c_1 = $({int(corners[1][0])}, {int(corners[1][1])})',
        ha='right',
        va='bottom')
    plt.text(
        corners[2][0] + 0.02,
        corners[2][1],
        rf'$c_2 = $({corners[2][0]}, {corners[2][1]})',
        ha='left')

    plt.axis('equal')
    plt.suptitle("Exercise 1a)", size=16)
    plt.title(
        f'Equilateral triangle with points {c_0}, {c_1}, {c_2[:2]}', size=12)
    plt.show()


# Exercise 1b)
# Picking a starting point
w_i = np.random.random(size=3)
w_sum = sum(w_i)
w_scale = w_i / w_sum
X = w_scale @ corners


def plot_n_points():
    """
    Plot the starting point 1000 times.

    Computes an array with size 3 and then scale the array, so the sum is
    always equal to 1. Then computes the points by performing matrix
    multiplication between the to arrays, and then plot with scatter.
    """
    N = 1000
    for _ in range(N):
        w_i = np.random.random(size=3)
        w_sum = sum(w_i)
        w_scale = w_i / w_sum
        X = w_scale @ corners
        plt.scatter(X[0], X[1])

    plt.suptitle("Exercise 1b)", size=16)
    plt.title(
        f"{N} plots of points as a linear combination of corners", size=12)
    plt.show()


# Exercise 1c)
def next(X_i):
    """
    Get the next point to iterate and return it.

    Set index c_j to random integers from 0 (inclusive) to 2 (exclusive). Then
    computes the next point in the iteration, and return the next point.

    Parameter:
    ----------
    X_i -- the i'th point (x, y) in the iteration
    """
    c_j = np.random.randint(3)
    X_next = (X_i + corners[c_j]) / 2
    return X_next


# Exercise 1d)
# Iterates through the first 5 points an discarding them
for _ in range(5):
    X = next(X)


def plot_triangle():
    """
    Plot the Sierpinski Triangle.

    Iterates the next point in the x_list by using the function next, and then
    plotting the x_list with 10000 points with scatter.
    """
    N = 10000
    x_list = np.zeros((N, 2))
    x_list[0] = X

    for i in range(N - 1):
        x_list[i + 1] = next(x_list[i])

    plt.scatter(*zip(*x_list), s=0.8, marker='.')
    plt.suptitle("Exercise 1d)", size=16)
    plt.title("Equilateral triangle")
    plt.axis('equal')
    plt.axis("off")
    plt.show()


# Exercise 1e)
def next_color(X_i):
    """
    Get the next point to iterate with color and return it.

    Set index c_j to random integers from 0 (inclusive) to 2 (exclusive). Then
    computes the next point in the iteration, and return the next point and
    index.

    Parameter:
    ----------
    X_i -- the i'th point (x, y) in the iteration
    """
    c_j = np.random.randint(3)
    X_next = (X_i + corners[c_j]) / 2
    return X_next, c_j


N = 10000
# Iterates through the first 5 points an discarding them
for _ in range(5):
    X = next_color(X)[0]

x_list = np.zeros((N, 2))
colours = np.zeros(N, dtype=int)

x_list[0] = X
colours[0] = next_color(X)[1]
# Itterate through the arrays
for i in range(N - 1):
    x_list[i + 1], colours[i + 1] = next_color(x_list[i])

# Giving the points in each corner a color: red, green or blue
red = x_list[colours == 0]
green = x_list[colours == 1]
blue = x_list[colours == 2]

print(f"number of red: {len(red)}")
print(f"number of green: {len(green)}")
print(f"number of blue: {len(blue)}")


def plot_color():
    """
    Plot the Sierpinski Triangle with colors.

    Using scatter to plot all the points with the corresponding colors; red,
    green and blue for each corner.
    """
    plt.scatter(*zip(*red), s=0.8, marker='.', color="red")
    plt.scatter(*zip(*green), s=0.8, marker='.', color="green")
    plt.scatter(*zip(*blue), s=0.8, marker='.', color="blue")
    plt.suptitle("Exercise 1e)", size=16)
    plt.title("Equilateral triangle with colors")
    plt.axis('equal')
    plt.axis("off")
    plt.show()


# Exercise 1f)
def color_matrice_next(C_i, X_i):
    """
    Get the next color with corresponding point and return the color and point.

    Set index j to random integers from 0 (inclusive) to 2 (exclusive). Then
    computes the next color and the next point in the iteration.

    Parameters:
    C_i -- The RGB colors of the X_i point in form of a matrix
    X_i -- The i'th point (x, y) in the iteration
    """
    j = np.random.randint(3)
    C_next = (C_i + r[j]) / 2
    X_next = (X_i + corners[j]) / 2
    return X_next, C_next


# Define the color vectors in the C_i matrix
r = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
N = 10000

# Iterates through the first 5 points an discarding them
for _ in range(5):
    X = next_color(X)[0]

x_list = np.zeros((N, 2))
colours = np.zeros((N, 3))

x_list[0] = X


def plot_rgb_gradient():
    """
    Plot the Sierpinski Triangle with RGB gradient colors.

    First iterates through the arrays x_list and colours, which is set to the
    function color_matrice_next with the i'th iteration in the lists. Then
    plot the iterated points with gradient RGB colors with scatter.
    """
    for i in range(N - 1):
        x_list[i + 1], colours[i + 1] = color_matrice_next(
            colours[i], x_list[i])
    plt.scatter(*zip(*x_list), c=colours, s=0.2)

    plt.suptitle("Exercise 1f)", size=16)
    plt.title("Equilateral triangle with gradient color")
    plt.show()


if __name__ == '__main__':
    # Plotting figure from exercise 1a)
    plot_3_points()

    # Plotting figure from exercise 1b)
    plot_n_points()

    # Plotting figure from exercise 1d)
    plot_triangle()

    # Plotting figure from exercise 1e)
    plot_color()

    # Plotting figure from exercise 1f)
    plot_rgb_gradient()
