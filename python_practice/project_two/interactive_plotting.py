import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))             # allows importing across projects
import project_one.basic_data_analysis as p1_bda
import plotly.graph_objects as go                                                           # can also use matplotlib but its not as fun and this allows html outputting

def make_plot(file_path: str, plot_size: tuple, horizontal_shift: int = 0, output_folder: str = 'sample_files', output_file: str = 'sample_output.html'):  
    """Creates an interactive plot scaled properly based on a given path to a csv

    Args:
        file_path (str): The path of the csv file
        plot_size (tuple): the desired width and height to use
        horizontal_shift (int, optional): A value to shift the x-data. Defaults to zero.
    """    
    try:
        file_data = p1_bda.clean_2D_data(file_path)
        file_data[0] = file_data[0] + horizontal_shift                                      # shift the data if desired
        path = os.path.join(output_folder, output_file)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)                                                                         # exit with error message
    data_stats = p1_bda.data_statistics(['voltage data'], [file_data])
    text_stats = "<br>".join([f"{col}: {data_stats[col].values[0]}" for col in data_stats.columns])
    fig = go.Figure(data = go.Scatter(x = file_data.iloc[:,0], y = file_data.iloc[:,1], mode = 'lines+markers'))
    fig.update_layout(
        width = plot_size[0],                                                               # specify the plot size based on tuple entries
        height = plot_size[1],
        title = 'Interactive Data Plot',
        xaxis_title = 'X-axis Label',
        yaxis_title = 'Y-axis Label',
        template = 'plotly',                                                                # specifies the pre made layout for the template
    )
    fig.add_annotation(
        text = text_stats,
        xref = 'paper', yref = 'paper',                                                     # position of text is placed with respect to the figure, not the data
        x = 0.95, y = 0.95,                                                                 # positions the text box in the top right corner
        showarrow = False,                                                                  # True would point an arrow to the data point, False keeps text on the figure
        font = dict(size = 10),
        bgcolor = 'rgba(255, 255, 255, 0.7)',
        bordercolor = 'black',
        borderwidth = 1,
        borderpad = 4,
        )
    
    import webbrowser                                                                       # allows direct interaction with an html file
    fig.write_html(path)
    webbrowser.open(path)                                                                   # bonus!

if __name__ == "__main__":
    path = sys.argv[1]
    try:
        width = 1000 if sys.argv[2] < 1000 else sys.argv[2]
        height = 1000 if sys.argv[3] < 1000 else sys.argv[3]
        shift = sys.argv[4]
        output_file_name = sys.argv[5]
        output_folder_name = sys.argv[6]
    except:
        width = height = 1000
        shift = 0
        output_file_name = 'sample_output.html'
        output_folder_name = 'sample_files'
    
    make_plot(path, (int(width), int(height)), horizontal_shift = int(shift), output_folder = output_folder_name, output_file = output_file_name)