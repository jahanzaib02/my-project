import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(categories, values)
plt.title('Sample Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
print("This line is added")
