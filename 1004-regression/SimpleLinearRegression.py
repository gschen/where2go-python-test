import numpy as np
import matplotlib.pyplot as plt

class SimpleLinearRegressionSelf:
    def __init__(self):
        self.a_ = None
        self.b_ = None
    
    def fit(self, x_train, y_train):
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        numerator = 0.0
        denominator = 0.0

        for x_i, y_i in zip(x_train, y_train):
            numerator += (x_i - x_mean) * (y_i - y_mean)
            denominator += (x_i - x_mean) ** 2
        
        self.a_ = numerator / denominator
        self.b_ = y_mean - self.a_ * x_mean

        return self
    
    def predict(self, x_test):
        return np.array([self._predict(x) for x in x_test])

    def _predict(self, x):
        return self.a_ * x + self.b_

    def mean_squared_error(self, y_true, y_predict):
        return np.sum((y_true - y_predict) ** 2)

    def r_square(self, y_true, y_predict):
        return 1 - (self.mean_squared_error(y_true, y_predict)) / np.var(y_true)

if __name__ == '__main__':
    x = np.array([1,2,4,6,8])
    y = np.array([2,5,7,8,9])


    lr = SimpleLinearRegressionSelf()
    lr.fit(x, y)
    print(lr.predict([10,12,14]))
    



    