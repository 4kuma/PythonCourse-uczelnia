import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def check_linear_regression(m, x, y):
    x = x[:, :m]
    model = LinearRegression()
    model.fit(x, y)
    return model.score(x, y)


def predict(m, x, y):
    x_200 = x[:200, :m]
    y_200 = y[:200]
    y_15 = y[-15:]
    model = LinearRegression()
    model.fit(x_200, y_200)
    x_15 = x[-15:, :m]
    x_predicted = model.predict(x_15)
    print(f'****************** m = {m} ******************')
    print('Actual Predicted')
    for i in range(15):
        print(f'{y_15[i]}    {x_predicted[i]}')


if __name__ == "__main__":
    with open('ml-latest-small/ratings.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        counter = 0
        m = 10000
        x = np.zeros(shape=[215, m], dtype=float)
        y = []
        currentID = '0'
        rowIndex = -1
        for row in readCSV:
            if row[1] == '1':
                currentID = row[0]
                rowIndex += 1
                y.append(float(row[2]))
            if row[0] == currentID and int(row[1]) <= m:
                x[rowIndex][int(row[1]) - 1] = float(row[2])
        x = np.nan_to_num(x, copy=False)
        y = np.array(y)

        m_1 = [10, 100, 200, 500, 1000, 10000]
        result_1 = []
        for i in m_1:
            result_1.append(check_linear_regression(i, x, y))
            predict(i, x, y)
        plt.plot(m_1, result_1, linewidth=8)
        plt.xscale('log')
        plt.xlabel('m')
        plt.ylabel('determination R^2')
        plt.show()
