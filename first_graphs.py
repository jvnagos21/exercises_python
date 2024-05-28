#exercicio 02
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([10, 8, 7, 6])

plt.bar(x, y)
plt.show()

#exercicio 03

np.random.seed(1)
data = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(data, color="green", ec="yellow")
plt.show()