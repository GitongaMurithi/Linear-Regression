# import modules
import matplotlib.pyplot as plt
from scipy import stats

# create the arrays that represents the values of x and y-axis

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# Execute a method that returns some important key values of linear regression
slope, intercept, r, p, std_err = stats.linregress(x, y)


# Create a function that uses the slope and intercept values to return a new value.
# This new value represents where on the y-axis the corresponding x value will be placed:
def myfunc(x):
    return slope * x + intercept


# Run each value of the x array through the function.
# This will result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x))

# Draw the original scatter plot:
plt.scatter(x, y)

# Draw the line of linear regression:
plt.plot(x, mymodel)

# Display the diagram:
plt.show()

print(r)
