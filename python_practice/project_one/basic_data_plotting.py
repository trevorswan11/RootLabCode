import matplotlib.pyplot as plt
import seaborn as sns
import basic_data_analysis as bda

def plot_data_basic(csv_files: list, labels: dict = None, title: str = None):
    if labels:
        keys = list(labels.keys())                                      # create a list of keys in the dictionary
    for i, file in enumerate(csv_files):
        plot_label = keys[i] if labels else i                           # extract first label if given
        x_label = labels[plot_label]['x'] if labels else 'X Values'     # access the key's plot labels in the dictionary  
        y_label = labels[plot_label]['y'] if labels else 'Y Values'
        plt.figure(figsize=(8, 6))                                      # set the figure size
        x = file.iloc[:, 0]                                             # entire first column
        y = file.iloc[:, 1]                                             # entire second column
        sns.lineplot(x = x, y = y, marker = 'o', label = f"Plot: {plot_label}") # following is very similar to MATLAB; add elements and then show
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title if title else 'Plotted Data')
        plt.legend()
        plt.show()                                                      # blocks=False would allow polts to be shown at the same time on a timer 
        # plt.pause()                                                   # uncomment this to show multiple plots, argument alters time on screen
    # plt.show()                                                        # having this outside the loop shows all plots at the same time

data = ['sample', 'keplers_equation']
labels = {
    'Distance over Time' : { 'x' : 'time (s)', 'y' : 'distance (m)'},
    'Ellipse distance' : {'x' : 'eccentric anomaly', 'y' : 'mean anomaly'}
}
plot_data_basic(bda.create_data_list(data), labels)