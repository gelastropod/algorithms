import random, math
import matplotlib.pyplot as plt

def coin(yes, no):
    x = random.uniform(0, yes + no)
    return x <= yes
def resevoirsample(samples, num):
    resevoirsamples = samples[:num]
    totalweight = sum(map(lambda x : x[1], samples[:num]))
    for i in range(num + 1, len(samples)):
        if coin(samples[i][1], totalweight):
            resevoirsamples = samples[i]
        totalweight += samples[i][1]
    return resevoirsamples, totalweight

    
def montecarlo(func, domain, samples):
    ans = 0
    for i in range(samples):
        x = random.uniform(domain[0], domain[1])
        ans += func(x)
    return (domain[1] - domain[0]) * ans / samples
def erf(z, s):
    return 2 / math.sqrt(math.pi) * montecarlo(lambda x : math.exp(-x * x), [0, z], s)
def aaa(z): return erf(z, 1000000)

plt.plot([i / 100 for i in range(-200, 200)], [[aaa(i / 100), print(f"{(i + 200) / 4}% done")][0] for i in range(-200, 200)], label='y = erf x', color='blue')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('erf x against x')

plt.grid(True)
plt.legend()

plt.show()
