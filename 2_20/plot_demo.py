import matplotlib
import math

def zed(t):
    result = 5 * math.sin(t / 10 + 2) + 0.1 * math.sin(t) + 0.1 * math.sin(2 * t - 5)
    return result


z = []
t = range(0, 100)

for i in t:
    z.append(zed(i))


print z

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure()
plt.scatter(z, t)
plt.show()

fig.savefig("graph.png")
