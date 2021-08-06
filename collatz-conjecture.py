import numpy as np
import matplotlib.pyplot as plt

# main function, just applying 3n+1 to odd numbers and dividing the even numbers by 2. 
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
    
# running the test for the first thousand numbers and plotting each sequence.
def result():
    for i in range(1, 1001):
        print("Sequence= ", end="")
        collatz(i)
        plt.plot(np.array(xvalues), np.array(yvalues), color='black', marker='o', markerfacecolor='yellow', markersize=3)

# plotting
plt.title("Collatz")
plt.xlabel("Iterations/Steps")
plt.ylabel("Numbers")
result()
plt.grid()
plt.show()
