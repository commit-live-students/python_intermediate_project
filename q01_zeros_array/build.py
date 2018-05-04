import numpy as np

def array_zeros(): 
    zeros_array = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
    
    zeros_array = np.zeros((3,4,2))
    print(zeros_array)
    return zeros_array
    
testArray = array_zeros()
print(testArray.shape)




