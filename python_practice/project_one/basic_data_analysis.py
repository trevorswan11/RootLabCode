import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_data_list(data_names: list) -> list:
    """
    Creates list of csv files corresponding to file path names inputted
    
    data_names should be named {file} as this function will append _data.csv to search in the model_data folder on its own. \n

    Args:
        data_names (list): list of names to be formatted (e.g test_file -> test_file_data.csv)

    Returns:
        list: a list of cleaned csv files corresponding to the data names
    """
    csvs = []
    for name in data_names:
        csvs.append(clean_data(f'../model_data/{name}_data.csv'))
    return csvs
        
def clean_data(path: str) -> pd.DataFrame:
    return (pd.read_csv(path, header=None)                              # read the csv file from the given path
            .dropna()                                                   # remove all present NaN values
            .apply(pd.to_numeric, errors='coerce')                      # force convert to numeric, replace errors with 'NaN'
            .dropna())                                                  # remove any new NaN values

def data_statistics(data_names, csv_files: list) -> pd.DataFrame:
    stats = pd.DataFrame(index=data_names)                              # set each row (index) to the corresponding data_name

    # python dictionary to hold stat type and lambda for value calculation
    statistics = {
        'Mean': lambda x: x.mean(),
        'Median': lambda x: x.median(),
        'Mode': lambda x: x.mode()[0] if not x.mode().empty else None,  # use the first mode value if there was one found
        'Std Dev': lambda x: x.std(),
        'Min': lambda x: x.min(),
        'Max': lambda x: x.max() 
    }
    
    for i, f in enumerate(csv_files):
        try:
            for col in f.columns:
                for name, func in statistics.items():
                    stats.at[data_names[i], name] = func(f[col])
        except Exception as e:
            print(e)
            
    return stats
    
def plot_data(csv_files: list):
    for file in csv_files:
        plt.figure(figsize=(8, 6))
        x = file.iloc[:, 0]                                             # First column
        y = file.iloc[:, 1]                                             # Second column
        sns.lineplot(x=x, y=y, marker='o', label=f"1234")
        plt.xlabel('X Values')
        plt.ylabel('Y Values')
        plt.legend()
        plt.show()        

data = [
    'keplers_equation',
    'ECG_norm',
]

files = create_data_list(data)
data_stats = data_statistics(data, files)
plot_data(files)
print(data_stats)
