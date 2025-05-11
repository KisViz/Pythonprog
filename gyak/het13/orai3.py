import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 15])
y = np.array([0, 50])
plt.plot(x, y)
plt.show()

plt.title("Kis Kutya")
plt.plot(x, y, 'o--g')
plt.show()

x = np.array([0, 15, 25, 35])
y = np.array([0, 50, 80, 20])
plt.plot(x, y)
plt.title("Sample Title")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

x1 = np.array([0, 15, 30])
y1 = np.array([0, 50, 90])
plt.subplot(1, 2, 1)
plt.plot(x1, y1, 'g')

x2 = np.array([0, 5, 10, 15])
y2 = np.array([0, 25, 40, 15])
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.show()

x = np.array([12, 2, 1, 5, 15, 10, 6, 8])
y = np.array([30, 45, 70, 35, 25, 40, 55, 50])
plt.scatter(x, y)
plt.show()

x = np.array([13, 6, 9, 3, 14, 16, 8, 7, 12])
y = np.array([40, 38, 20, 30, 55, 60, 22, 25, 30])
colors = np.array(["red", "blue", "green", "yellow", "pink", "black", "orange", "purple", "brown"])
plt.scatter(x, y, color=colors)
plt.show()

x = np.array(["A", "B", "C", "D", "E"])
y = np.array([5, 3, 7, 8, 4])
plt.bar(x, y, color="blue")
plt.show()

x = np.random.normal(250, 30, 500)
plt.hist(x)
plt.show()

x = np.array([30, 20, 10, 40])
labels = ["Kacsa", "Dínó", "Quokka", "Panda"]
colors = ["pink", "purple", "gold", "turquoise"]
plt.pie(x, labels=labels, colors=colors)
plt.show()

x = np.array([30, 20, 10, 40])
labels = ["Kacsa", "Dínó", "Quokka", "Panda"]
colors = ["pink", "purple", "gold", "turquoise"]
explode = [0, 0.2, 0, 0]
plt.pie(x, labels=labels, colors=colors, explode=explode)
plt.show()
