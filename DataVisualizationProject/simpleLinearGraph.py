import matplotlib.pyplot as plt

input_values = [1, 6, 11, 12, 16, 19, 24]
plt.plot(input_values, linewidth = 5)

# Define the chart title 
plt.title("Square Numbers", fontsize = 24)

# Define the names the axes
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set the size of tag labels
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()
