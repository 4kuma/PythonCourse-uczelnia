import csv
import numpy as np
from copy import copy

if __name__ == "__main__":
    movies = {}
    with open('ml-latest-small/movies.csv', 'r', encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        for row in readCSV:
            if int(row[0])>10000: break
            movies[int(row[0])-1] = row[1]
    with open('ml-latest-small/ratings.csv', 'r') as csvfile:
        np.seterr(divide='ignore', invalid='ignore')
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        userID = []
        counter = 0
        m = 10000
        x = np.zeros(shape=[610, m], dtype=float)
        currentID = '0'
        rowIndex = -1
        for row in readCSV:
            if row[0] != currentID:
                currentID = row[0]
                rowIndex += 1
                userID.append(currentID)
            if row[0] == currentID and int(row[1]) <= m:
                x[rowIndex][int(row[1]) - 1] = float(row[2])
        x_norm = np.nan_to_num(np.divide(x, np.linalg.norm(x, axis=0)))
        print("UserID : Movie")
        for y in x:
            z = np.dot(x_norm, np.nan_to_num(np.array(y) / np.linalg.norm(y)))
            z_norm = np.nan_to_num(np.divide(z, np.linalg.norm(z)))
            result = np.dot(x_norm.T, z_norm)
            top_10_results = result.copy()
            top_10_results = np.sort(top_10_results)
            top_10_results = top_10_results[-10:]
            top_10_results = top_10_results[::-1]
            print(top_10_results)
            print(f'*****{userID.pop(0)}*****')
            for i in top_10_results:
                print(f'{movies[np.where(result == i)[0][0]]}')

