# Analyzing IPL Matches
## Create a function that returns a NumPy array when given a path to a CSV file

**The function should **
- Be named `read_csv_data_to_ndarray`
- Accept parameters as follows
    - First parameter is named `path`, representing the path of the file to be loaded. This is mandatory
    - Second parameter is named `dtype`, it is optional, with default value `np.float64`

- Use that `path` and `dtype` to read the CSV file and return the numpy array (using a standard numpy library function)
- Always skip the header row when reading the CSV
- Return the numpy array
