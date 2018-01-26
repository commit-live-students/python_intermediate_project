# Default Imports
import numpy as np

def create_Nd_array(n_dimension=6):
    # create an array of 0 to N-1 numbers, (arange function is start index inclusive and end index exclusive)
    # defined default_dimension to 6 as it goes out of memory on my jupyter notbook,
    # allthough the memory size of notebook can be increased, currently this is capped to max_dimension of 6
    max_dimension = 6

    prog_dimension = n_dimension
    # check if the dimension is greater than default dimension
    if n_dimension > max_dimension:
        print "\nYou have entered a very large value, defaulting it to max dimension {}".format(max_dimension)
        prog_dimension = max_dimension

    n1 = np.arange(0,prog_dimension ** prog_dimension,dtype=np.int32)
    print "\nPrinting the created array for passed argument - range as {}-D array".format(prog_dimension,prog_dimension)
    print n1
    # Using generator expressions with tuple
    reshape_dim_tuple = tuple(prog_dimension for i in range(prog_dimension))
    # print "\nTuple created for dimensions: ",tup1
    # reshape the array using above tuple which creates symmetric dimensions of size prog_dimension
    # reshape function also accepts the tuple as an argument to specify the dimensions
    n2 = n1.reshape(reshape_dim_tuple)
    print "\nPrinting the reshaped array of values to {}-Dimensional array".format(prog_dimension)
    print n2
    return n2

# Enter solution here
def create_3d_array():
    return create_Nd_array(3)
