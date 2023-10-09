import numpy as np
import matplotlib.pyplot as plt

TIME_STEPS = 50
STOP_LIMIT = 0.001

def gradient(x):
    return 2 * (x-5)

def next_step(current, stepSize):
    return current - stepSize

def main():
    error = []
    x_values = []
    X = np.arange(10)
    Y = (X - 5) ** 2
    plt.plot(X, Y)

    x = 0
    learning_rate = 0.1
    for i in range(TIME_STEPS):
        if abs(learning_rate * gradient(x)) < STOP_LIMIT:
            print("Learning Finished, Optimal Point : " + str(x))
            plt.scatter(x_values, error, c='red')
            plt.show()
            return
        x = next_step(x, learning_rate * gradient(x))
        x_values.append(x)
        y_at_newx = (x - 5)**2
        error.append(y_at_newx)

if __name__ == '__main__':
    main()