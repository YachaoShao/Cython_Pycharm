#import library

from sklearn import preprocessing
import numpy as np
import xlrd
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def get_num(eigvals,percent):
    sortArray = np.sort(eigVals)
    sortArray = sortArray[-1::-1]
    arraySum = sum(sortArray)
    tmp=0
    num=0
    for i in sortArray:
        tmp+=i
        num+=1
        if tmp>=arraySum*percent:
            return num

#read data from excel and write in the matrix
book = xlrd.open_workbook("Mappe1.xlsx")
table = book.sheet_by_index(0)


synape_matrix = np.zeros((table.nrows-3,table.ncols-3))
for row in range(3,table.nrows):
    for col in range(2,table.ncols-1):
        synape_matrix[row-3][col-2]= int(table.cell_value(row,col))

#save to txt
print synape_matrix.shape
synape_data= synape_matrix.T

print synape_data.shape
np.savetxt('synapse_experiment.csv',synape_data,delimiter=',')


#standlize the synapse matrix and compute the covMatrix
synape_scaled = preprocessing.scale(synape_data)
covMatrix = np.cov(synape_scaled, rowvar=0)

#compute the eigenvalues and eigenvectors
eigVals, eigVects = np.linalg.eig(covMatrix)

plt.plot(eigVals,'bs')
plt.savefig('eigval.png')

#get num from precise percentage
n= get_num(eigVals,0.99)
print n

#select the main components
eigVectsIndice = np.argsort(eigVals)
n_eigValIndice = eigVectsIndice[-1:-(n+1):-1]
n_eigVect = eigVects[:,n_eigValIndice]

lowDData = np.dot(synape_scaled,n_eigVect)





















