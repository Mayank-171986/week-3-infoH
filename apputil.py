import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
"""
This funtion is a recurisve function that will return the nth number of fibonacci series for a given n
Parameters:
 n: It is the position of a number in fibonacci series, it is a non-negative integer.
Returns:
 This function will return the nth number of fibonacci series for a given n
"""
def fibonacci(n):
    # This is the base case to exit the recurisve function. 
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # This is the function to call the recurisve function.
def fib(n):
    fibonacci_series = [fibonacci(i) for i in  range(n+1)]
    return(fibonacci_series[n])
"""
This is a recursive function that converts an integer into its binary representation.
Parameters:
 n: It is a non-negative integer to convert into binary representation.
Returns:
 This function will return binary representation of a given number n 
"""
def to_binary(n):
     # This is the base case to exit the recursive function.
    if n == 0:
        return '0'
    if n == 1:
        return '1'
     # This divides the number by 2 and returns the remainder until the number becomes 0.
    return to_binary(n // 2) + str(n % 2)


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
#This creates a dataframe from the csv file and read it.
df_bellevue = pd.read_csv(url)
#This replaces the null values with nan values in the dataframe.
df_bellevue.replace("", np.nan, inplace=True)
"""
This function returns list of all columns sorted in ascending order of least missing values. 
"""
def task_1():
    temp_df = df_bellevue

    # cleaning gender column
    temp_df['gender'] = temp_df['gender'].replace(['?', 'g', 'h'], np.nan)

    #counting null values in each column
    column_null_count = temp_df.isnull().sum().to_dict()
    
    #sorting the columns based on null values in ascending order
    sorted_column_null_count = dict(sorted(column_null_count.items(), key=lambda item: item[1]))
    print(sorted_column_null_count)
    
    #filtered_sorted_column_null_count = {k: v for k, v in sorted_column_null_count.items() if v != 0}
    column_list = list(sorted_column_null_count.keys())
    return column_list
"""
This function returns a Dataframe with two columns "year" and "total admissions" corresponding to each year. 
"""
def task_2():
    df_result = pd.DataFrame(columns=['year', 'total_admissions'])
    #df_filtered_data = df_bellevue.dropna(subset=['disease'])
    df_result['year'] = pd.to_datetime(df_bellevue['date_in'])
    df_result['year'] = df_result['year'].dt.year
    total_admissions = df_result.groupby('year').size().reset_index(name='total_admissions')
    return total_admissions
"""
This function returns a series with each gender and average age corresponding to each gender. 
"""
def task_3():
    average_age_by_gender = df_bellevue.groupby('gender')['age'].mean().dropna()
    return average_age_by_gender
"""
This function returns a series with each gender with top 5 professions corresponding to each gender. 
"""
def task_4():
    top_5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top_5_professions