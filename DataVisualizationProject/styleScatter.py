import matplotlib.pyplot as plt

x_valeus = list(range(500))
y_values = [x**3 for x in x_valeus]

plt.scatter(x_valeus, y_values, c = y_values, cmap=plt.cm.Reds, edgecolors='none', s = 40)

# Define the chart title 
plt.title("Square Numbers", fontsize = 24)

# Define the names the axes
plt.xlabel("Value", fontsize = 12)
plt.ylabel("Square of Value", fontsize = 12)

# Sets the range for each axis
plt.axis([0, 100, 0, 11000])

plt.show()
