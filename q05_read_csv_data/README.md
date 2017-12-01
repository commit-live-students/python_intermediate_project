# Read a csv file and save it in variable.

Cool, now that you accustomed with handling data set , we should probably 
try to store it and play with it. 

## Write a function`read_ipl_data_csv` that:
- Reads the data from the csv file using the function `np.genfromtxt` and stores it into a variable named as `ipl_matches_array`.

This task will provide help you to learn how to load a structured data(csv) in tabular format.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path to the file csv |
| dtype | Float | optional |  |  |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| Numpy array | ndarray | Array containing data set values |

Note : dtype should be provided as '|S50'
