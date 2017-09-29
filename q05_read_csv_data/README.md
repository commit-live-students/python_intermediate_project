## Create a function to read a csv file and save it in variable.


Cool, now that you accustomed with handling data set , we should probably 
try to store it and play with it. 

**The function should**
- Be named as `read_csv_data`.
- The variable should be named `ipl_matches_array`
- The dtype of the `ipl_matches_array` array should be `|S50`

This task will provide help you to learn how to load a structured data(csv) in tabular format.

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path to the file csv |
| dtype | Float | optional |  |  |

#### Returns:

| Return | dtype | description |
| --- | --- | --- |
| Numpy array | ndarray | Array containing data set values |