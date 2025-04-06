import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy

# Task 1: Load and Explore the Dataset with Error Handling
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

try:
    df = pd.read_csv(url)
    print("Dataset Loaded Successfully")
except FileNotFoundError:
    print("Error: The dataset file was not found.")
    exit()
except pd.errors.ParserError:
    print("Error: Failed to parse the CSV file.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while loading the file: {e}")
    exit()

# Display first few rows
print(df.head())

# Explore structure and check missing values
try:
    print(df.info())
    print("Missing Values:\n", df.isnull().sum())
except Exception as e:
    print(f"Error analyzing structure: {e}")

# Clean missing data
try:
    df.dropna(inplace=True)
    print("Missing values dropped.")
except Exception as e:
    print(f"Error during cleaning: {e}")

# Task 2: Basic Data Analysis
try:
    print("Descriptive Statistics:\n", df.describe())

    # Group by Vehicle Type
    grouped_sales = df.groupby("Vehicle_Type")["Automobile_Sales"].mean()
    print("\nAverage Automobile Sales by Vehicle Type:\n", grouped_sales)

    # Group by Recession
    recession_sales = df.groupby("Recession")["Automobile_Sales"].mean()
    print("\nAverage Sales During Recession vs Non-Recession:\n", recession_sales)

except KeyError as e:
    print(f"Column error during analysis: {e}")
except Exception as e:
    print(f"Unexpected error during analysis: {e}")

# Task 3: Data Visualizations
try:
    # Line Chart
    plt.figure(figsize=(10, 6))
    df.groupby("Year")["Automobile_Sales"].sum().plot(kind="line", marker="o")
    plt.title("Total Automobile Sales Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Automobile Sales")
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Bar Chart
    plt.figure(figsize=(10, 6))
    sns.barplot(x=grouped_sales.index, y=grouped_sales.values)
    plt.title("Average Automobile Sales by Vehicle Type")
    plt.xlabel("Vehicle Type")
    plt.ylabel("Average Sales")
    plt.tight_layout()
    plt.show()

    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df["Automobile_Sales"], bins=20, kde=True)
    plt.title("Distribution of Automobile Sales")
    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Price", y="Automobile_Sales", hue="Vehicle_Type")
    plt.title("Relationship between Price and Automobile Sales")
    plt.xlabel("Price")
    plt.ylabel("Automobile Sales")
    plt.tight_layout()
    plt.show()

# Error Handling 
except KeyError as e:
    print(f"Missing column for plotting: {e}")
except Exception as e:
    print(f"Error during visualization: {e}")
