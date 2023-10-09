import numpy as np
import matplotlib.pyplot as plt

TIME_STEPS = 50
STOP_LIMIT = 0.001

def gradient(x):
    return 2 * (x-5)

def next_step(current, step):
    return current + step

def main():
    y_values = []
    x_values = []
    step_values = []

    #Initial plot to visualize on
    X = np.arange(10)
    Y = (X - 5) ** 2
    plt.plot(X, Y)
   

    #Initial Value at random as GD is invariant to x_0
    x = np.random.randint(0, 10)

    #Standard learning rate for simple convex function
    learning_rate = 0.1
    for _ in range(TIME_STEPS):
        step = learning_rate * gradient(x)
        step_values.append(abs(step))

        #Stop condition
        if abs(learning_rate * gradient(x)) < STOP_LIMIT:
            print("Learning Finished, Optimal Point : " + str(x))
            #Scatter plot of gradient descent reaching minimum
            plt.scatter(x_values, y_values, c='red')
            plt.show()

            #Plot of Y values, depicting the values reaching 0
            plt.plot(y_values)
            plt.show()

            #Plot of step sizes as we get close to minimum
            plt.plot(step_values)
            plt.show()
            return
        x = next_step(x, learning_rate * -1 * gradient(x))
        x_values.append(x)
        y_at_newx = (x - 5)**2
        y_values.append(y_at_newx)

if __name__ == '__main__':
    main()