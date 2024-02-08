import matplotlib.pyplot as plt

plt.scatter(6,8, s = 200)

# Define the chart title 
plt.title("Square Numbers", fontsize = 24)

# Define the names the axes
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set the size of tag labels
plt.tick_params(axis='both', which='major', labelsize = 14)

plt.show()