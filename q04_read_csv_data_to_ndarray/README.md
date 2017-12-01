# Analyzing IPL Matches


Wow feeling like an expert huh!!..
Now let's grab some knowledge related to loading of data.
Your job is to create a function that returns a numpy array when given a path to csv file.


## Write a function `read_csv_data_to_ndarray` that :
- Use that `path` and `dtype` to read the CSV file and return the numpy array (using a standard numpy library function)
- Always skip the header row when reading the CSV
- Return the numpy array

By executing this task you can learn the basic operation of reading a csv file and manipulate it.


#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path to the file csv |
| dtype | Float | optional | np.float64 | data type |

#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| Numpy array | ndarray | Array containing data set values |
