import matplotlib.pyplot as plt

x_valeus = list(range(1, 1001))
y_values = [x**2 for x in x_valeus]

plt.scatter(x_valeus, y_values, s = 40)

# Define the chart title 
plt.title("Square Numbers", fontsize = 24)

# Define the names the axes
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

# Sets the range for each axis
plt.axis([0, 1100, 0, 110000])

plt.show()