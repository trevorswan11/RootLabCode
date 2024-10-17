import pandas as pd
import numpy as np

def create_data_list(data_names: list) -> list:
    csvs = []
    for name in data_names:
        csvs.append(clean_2D_data(f'../model_data/{name}_data.csv'))    # data should be named a certain way, format path accordingly
    return csvs
        
def clean_2D_data(path: str) -> pd.DataFrame:
    df = rotate_column_data(path)                                       # account for column only data (e.g 1, 2, 3, 4, 5, ...)
    return (df.dropna()                       
            .apply(pd.to_numeric, errors = 'coerce')                    # force convert to numeric, replace errors with 'NaN'
            .dropna())                                                  # remove any new NaN values

def rotate_column_data(path: str, start: int = None, stop: int = None) -> pd.DataFrame:
    data = pd.read_csv(path, header=None)                               # read the data from the path without headers for ease of use
    if data.shape[0] == 1:
        data_length = data.shape[1]
        i = range(0, data_length)
        transposed_data = data.T
        result = pd.DataFrame(index=i)                                  # set the index of the data frame to the ascending values
        if start and stop:                                              # conform to users desired range if given
            step = np.linspace(start, stop, data_length)                # Similar to MATLAB linspace -> (start, stop, step) 
        else: step = i
        result[0] = step
        result[1] = transposed_data[0].values                           # transposed_data is a df, only want the values in the first column, not headers/indices
        
        # Create a new csv file for testing if desired 
        # with open('test.csv', 'w', newline='') as f:                    
        #     f.write(result.to_csv(index = False, header = None))
        return result
    return data                                                         # this is called for every file, but not every file is modified

def data_statistics(data_names, csv_files: list) -> pd.DataFrame:
    stats = pd.DataFrame(index = data_names)                              # set each row (index) to the corresponding data_name

    statistics = {                                                      # dictionary to hold stat type and lambda for value calculation
        'Mean': lambda x: x.mean(),
        'Median': lambda x: x.median(),
        'Mode': lambda x: x.mode()[0] if not x.mode().empty else None,  # use the first mode value if there was one found
        'Std Dev': lambda x: x.std(),
        'Min': lambda x: x.min(),
        'Max': lambda x: x.max() 
    }
    
    # i is the index of the csv file, f is the file itself
    for i, f in enumerate(csv_files):
        try:
            for col in f.columns:                                       # go to each column in the dataframe to add stats
                for name, func in statistics.items():                   # name is the name of the statistic and func is the lambda to calculate it in statistics
                    stats.at[data_names[i], name] = func(f[col])        # set stats for the data set at name of the statistic to evaluated function
        except Exception as e:
            print(e)                                                    # really basic and horrible error handling            
    return stats     

def save_data(data: pd.DataFrame, file_name: str, folder: str = 'sample_stats', file_type: str = 'csv', include_indices: bool = True, include_headers: bool = True) -> str:
    """ Saves a pandas dataframe to a given file name """
    path = f"{folder}/{file_name}.{file_type}"
    forbidden = ['json', 'sql']                                         # unimplemented or not properly handled data types
    fail = f"Cannot create file of type {file_type} from your data."
    if file_type in forbidden:
        raise TypeError(fail)
    with open(path, 'w', newline = '') as f:
        match file_type:                                                # python equivalent to a switch case, hardcoded here but could use f string with global?
            case 'csv':
                f.write(data.to_csv(index = include_indices, header = include_headers))
            case 'html':
                f.write(data.to_html(index = include_indices, header = include_headers))
            case 'tex':                                                 #! really lovely latex formatting, will be useful for papers
                f.write(data.to_latex(index = include_indices, header = include_headers))
            case _:                                                     # this acts as a default case, and also catches raised exceptions
                f.write(data.to_string(index = include_indices, header = include_headers)) 
    return path             
                
        
data = [
    'keplers_equation',
    'ECG_norm',
    'sample'
]

files = create_data_list(data)
data_stats = data_statistics(data, files)

if __name__ == '__main__':
    save_data(data_stats, 'sample_stats', file_type='bib')
