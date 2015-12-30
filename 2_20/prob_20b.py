import matplotlib
import math

def zed(t):
    result = 5 * math.sin(t / 10 + 2) + 0.1 * math.sin(t) + 0.1 * math.sin(2 * t - 5)
    return result

def zed_hat(t, z):
    if t < 3:
        return 0
    else:
        return 3 * z[t - 1] - 3 * z[t - 2] + z[t - 3]
    
z = []
zh = []
t = range(0, 1000)

for i in t:
    z.append(zed(i))
    zh.append(zed_hat(i, z))

sum_of_errors_squared = 0
sum_of_zs_squared = 0

for i in range(3,1000):
    error = zh[i] - z[i]
    error_squared = error ** 2
    z_squared = z[i] ** 2
    
    sum_of_errors_squared += error_squared
    sum_of_zs_squared += z_squared

relative_rms = (sum_of_errors_squared / sum_of_zs_squared) ** 0.5

print "Relative RMS error is {0}".format(relative_rms)

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(t, z, 'b-', t, zh, 'r-')
plt.show()

fig.savefig("prob_20b.png")
