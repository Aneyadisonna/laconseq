import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]
labels = ['A', 'B', 'C', 'D', 'E']

# Plot with markers
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Annotate each data point
for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Data Points with Annotations')

plt.show()
