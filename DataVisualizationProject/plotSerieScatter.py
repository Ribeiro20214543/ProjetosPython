import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_valeus = [2, 4, 8, 16, 28]

plt.scatter(x_values, y_valeus, s = 100)

# Define the chart title 
plt.title("Square Numbers", fontsize = 24)

# Define the names the axes
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set the size of tag labels
plt.tick_params(axis='both', which='major', labelsize = 14)

plt.show()