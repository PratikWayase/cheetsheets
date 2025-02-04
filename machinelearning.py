
#Category	                 Important Functions

#Data Loading & Saving   	pd.read_csv(), df.to_csv()
#Data Exploration	        df.info(), df.describe(), df.shape, df.columns, df.dtypes
#Handling Missing Data	    df.isnull().sum(), df.dropna(), df.fillna()
#Handling Duplicates	        df.duplicated(), df.drop_duplicates()
#Data Filtering & Selection	df.loc[], df.iloc[], df[['col1', 'col2']], df[df['col'] > val]
#Grouping & Aggregation	    df.groupby(), df.pivot_table(), df.value_counts()
#Sorting & Ordering	        df.sort_values()
#Data Transformation      	df.rename(), df.apply()
#Merging & Joining	        pd.merge()


#===============================#
import pandas as pd

#Save dataframe to a CSV file
df.to_csv('output.csv', index=False)

# Get data summary
df.info()  # Shows column names, data types, and non-null counts

# summary statistics
print(df.describe())  # Mean, min, max, std, etc.

#Get number of rows & columns
print(df.shape)  # Output: (rows, columns)

#Get column names & data types
print(df.columns)  # List of column names
print(df.dtypes)   # Data types of each column

#Check for missing values
print(df.isnull().sum())  # Count NaN values per column

#Handle missing values
df_cleaned = df.dropna()  # Remove rows with NaNs
df_filled = df.fillna(0)  # Replace NaNs with 0

#Find & remove duplicate rows
df.drop_duplicates(inplace=True)  # Remove duplicates

#Get unique values
print(df['category'].unique())  # Unique values in a column
print(df['category'].nunique())  # Count of unique values

# Count occurrences of each category
print(df['category'].value_counts())  # Count each unique value

#Group data & apply aggregation
print(df.groupby('category')['sales'].sum())  # Sum of sales per category

# Sort by column values
df_sorted = df.sort_values(by='price', ascending=False)

#Rename column
df.rename(columns={'old_name': 'new_name'}, inplace=True)

#Apply function to each row/column
df['new_col'] = df['price'].apply(lambda x: x * 1.1)  # Increase price by 10%

# Select specific columns
df_subset = df[['name', 'price']]

#Select rows by label & index
print(df.loc[0])  # First row by label
print(df.iloc[0])  # First row by index

#Filter rows
filtered_df = df[df['price'] > 100]


#Create pivot tables
pivot = df.pivot_table(index='category', values='sales', aggfunc='sum')
print(pivot)

#Merge DataFrames
df_merged = pd.merge(df1, df2, on='id', how='inner')  # Inner join on 'id'

