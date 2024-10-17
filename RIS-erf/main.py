import random, math
import matplotlib.pyplot as plt

def coin(yes, no):
    """ Think of flipping a coin. It has a {yes} chance of landing heads
        (which will return True) and a {no} chance of landing tails
        (which will return False). """
    
    return random.uniform(0, yes + no) <= yes

def resevoirSample(samples, weights):
    """ Uses resevoir sampling to draw a single sample from the given
        samples with a probability proportional to the given weights. """
    
    currentSample = samples[0]
    totalWeight = weights[0]

    for i in range(1, len(samples)):
        if coin(weights[i], totalWeight):
            currentSample = samples[i]
        totalWeight += weights[i]

    return currentSample

def monteCarlo(f, N, M, bounds):
    """ Calculates the integral of f within the bounds using RIS. N and
        M are parameters controlling the number of samples samples. """

    NxI = 0

    for i in range(N):
        X = [random.uniform(bounds[0], bounds[1]) for j in range(M)]
        w = list(map(f, X))
        
        Y = resevoirSample(X, w)
        NxI += sum(w) / M

    return (bounds[1] - bounds[0]) * NxI / N

def erf(x, N, M):
    """ Calculates the error function erf(x). """

    return 2 / math.sqrt(math.pi) * monteCarlo(lambda t : math.exp(-t * t), N, M, [0, x])

N, M = map(int, input("Enter N and M (space separated): ").split())

xPoints = [i / 100 for i in range(-200, 201)]
yPoints = list(map(lambda x : [erf(x, N, M), print(x)][0], xPoints))

plt.plot(xPoints, yPoints, label='y = erf(x)', color='blue')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Graph of erf(x) against x')

plt.grid(True)
plt.legend()

plt.show()
