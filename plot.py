import matplotlib.pyplot as plt

def fitness(x):
    x = x[0]
    pos1 = x if x < 5 else 0
    pos2 = x - 7.5 if 10 <= x < 20 else 0
    neg1 = -x/2 + 7.5 if 5 <= x < 10 else 0
    neg2 = -x/2 + 22.5 if x >= 20 else 0
    return pos1 + pos2 + neg1 + neg2

arr = [fitness([y]) for y in range(-10, 30)]

for i in range(10):
    for i in range(-10, 30):
        plt.plot(list(range(-10, 30)), arr)
        plt.scatter(i, fitness([i]))
        plt.pause(0.05)

plt.show()
