# Python Practice

This folder contains the projects/scripts I worked on to learn how to analyze data with python.

## I created an 8-project lineup using ChatGPT as follows:

### Basic Data Analysis on Experimental Data
---

**Objective**: Get familiar with Python basics and data handling using Pandas.

**Description**: Use a CSV file (e.g., temperature and pressure data) and perform basic operations such as reading the data, cleaning it (handling missing values), and performing simple analysis (mean, median, standard deviation).

**Tools**: `Pandas`, `NumPy`

**Key Concepts**:
- Reading CSV files with `pandas.read_csv()`.
- Data manipulation (filtering, grouping, etc.).
- Basic descriptive statistics.

**Bonus**: Create simple visualizations (bar charts, histograms) using `Matplotlib`.

*Folder: project_one*

### Interactive Data Plotting
---

**Objective**: Learn data visualization and interactivity.

**Description**: Load an experimental dataset (e.g., voltage vs time) and create an interactive plot where users can zoom in, pan, and inspect data points.

**Tools**: `Matplotlib`, `NumPy`

**Key Concepts**:
- Basic plotting: line plots, scatter plots, labels, and legends.
- Customizing plots (axes labels, color schemes).
- Adding interactivity (zooming, hovering over data points).

**Bonus**: Try exporting the plot as an interactive HTML file.

*Folder: project_two*

### Linear Regression on Experimental Data
---

**Objective**: Introduction to machine learning using Scikit-learn.

**Description**: Use a dataset (e.g., chemical concentration vs reaction rate) to predict one variable from another using linear regression. Split the dataset into training and testing sets, train a model, and evaluate it.

**Tools**: `Scikit-learn`, `Pandas`, `Matplotlib`

**Key Concepts**:
- Train-test split of data.
- Linear regression model (`LinearRegression` in Scikit-learn).
- Model evaluation: Mean Squared Error (MSE), R-squared score.

**Bonus**: Plot the regression line on the scatter plot of the data.

*Folder: project_three*

### Time Series Analysis
---

**Description**: Use time-series data (e.g., temperature readings over days) and perform basic operations like calculating rolling averages and plotting trends.

**Tools**: `Pandas`, `Matplotlib`

**Key Concepts**:
- Date and time parsing in Pandas.
- Rolling averages and cumulative sums.
- Plotting trends and seasonal patterns.

**Bonus**: Decompose the time series into trend, seasonal, and residual components using `statsmodels`.

*Folder: project_four*

### K-Means Clustering of Experimental Data
---

**Description**: Use a dataset (e.g., material properties like density, conductivity, etc.) and apply K-means clustering to group the data into clusters based on similarity.

**Tools**: `Scikit-learn`, `Pandas`, `Matplotlib`

**Key Concepts**:
- K-means clustering algorithm.
- Feature scaling (`StandardScaler` in Scikit-learn).
- Visualizing clusters with different colors.

**Bonus**: Implement elbow method to choose the optimal number of clusters.

*Folder: project_five*

### Predictive Model for Polymer Properties
---

Objective: Apply machine learning to predict material properties.

**Description**: Use a dataset of polymer compositions and properties (e.g., tensile strength, elasticity) to train a predictive model for one of the properties. Experiment with different algorithms like Decision Trees and Random Forests.

**Tools**: `Scikit-learn`, `Pandas`, `Matplotlib`

**Key Concepts**:
- Decision Trees and Random Forest models.
- Cross-validation for model evaluation.
- Feature importance analysis.

**Bonus**: Try hyperparameter tuning using `GridSearchCV`.

*Folder: project_six*

### Image Classification Using Neural Networks
---

**Description**: Build a basic image classification model (e.g., classify images of different materials or objects) using a neural network.

**Tools**: `Keras` (from `TensorFlow`), `NumPy`, `Pandas`

**Key Concepts**:
- Building a simple neural network using Keras.
- Image data preprocessing.
- Training and evaluating the model.

**Bonus**: Improve performance by adding more layers or using Convolutional Neural Networks (CNNs).

*Folder: project_seven*

### Automated Report Generation
---

**Objective**: Automate the process of generating data analysis reports.

**Description**: Write a script that takes a dataset (e.g., experimental results) and generates an automated PDF report with analysis, plots, and key insights.

**Tools**: `Pandas`, `Matplotlib`, `Fpdf` or `ReportLab`

**Key Concepts**:
- Automating data analysis and plotting.
- Exporting results as a formatted PDF document.

**Bonus**: Include interactive plots using `plotly`.

*Folder: project_eight*


## Projects are to be completed in order according to:
- **Project 1 (Basic Data Analysis on Experimental Data)**: This introduces you to Python basics, especially Pandas and NumPy, which are critical for data manipulation in future projects. You'll get used to Python syntax and working with data files.
- **Project 2 (Interactive Data Plotting)**: After handling and manipulating data, you’ll learn how to visualize it with Matplotlib. Visualization is an important step in data analysis, and this will provide the foundation for more advanced visualizations later.
- **Project 3 (Linear Regression on Experimental Data)**: By this point, you’ll have experience with data handling and visualization, so you can start exploring machine learning. This project introduces basic machine learning concepts (regression), which are simpler than unsupervised learning (Project 5).
- **Project 4 (Time Series Analysis)**: Once you’re comfortable with regression, this project exposes you to working with temporal data, an important concept in experimental data analysis.
- **Project 5 (K-Means Clustering of Experimental Data)**: Now you move into unsupervised learning, grouping similar data points without labels, which builds on the machine learning foundation from Project 3.
- **Project 6 (Predictive Model for Polymer Properties)**: This is a more advanced version of Project 3, introducing new machine learning models like Decision Trees and Random Forests. By now, you'll be ready to work with more complex datasets and predictive tasks.
- **Project 7 (Image Classification Using Neural Networks)**: This project is an introduction to deep learning and neural networks, which requires an understanding of machine learning fundamentals (covered in previous projects). You'll also apply Python to image data.
- **Project 8 (Automated Report Generation)**: By this point, you’ll have solid Python skills. Automating report generation is a practical way to integrate all the previous concepts and present your analysis efficiently.

## Using code
Data used in this folder is not public out of respect to potentially referencing real unpublished research. That being said, you can create your own data to place in the data folder with proper names. 

Download all packages using:
```
pip install -r requirements.txt
```
You may need to be in an elevated shell for the installation to work.
