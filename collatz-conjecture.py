import numpy as np
import matplotlib.pyplot as plt

def collatz(n):
    global yvalues, xvalues
    yvalues = []
    xvalues = []
    count = 0
    while n > 1:
        xvalues.append(count)
        count += 1
        yvalues.append(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    print(yvalues, '\n', "Iterations = ", count, '\n')

def result():
    for i in range(1, 1001):
        print("Sequence= ", end="")
        collatz(i)
        x = np.array(xvalues)
        y = np.array(yvalues)
        plt.plot(x, y, color='black', marker='.', markerfacecolor='yellow')

# plotting
plt.title("Collatz")
plt.xlabel("X axis")
plt.ylabel("Y axis")
result()
plt.grid()
plt.show()
