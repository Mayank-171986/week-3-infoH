import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
def fibonacci(n):
    if n<=0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fib(n):
    fibonacci_series = [fibonacci(i) for i in  range(n+1)]
    return(fibonacci_series[n])

def to_binary(n):
    if n == 0:
        return '0'
    if n == 1:
        return '1'
    return to_binary(n // 2) + str(n % 2)

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
df_bellevue.replace("", np.nan, inplace=True)

def task_1():
    column_null_count = df_bellevue.isnull().sum().to_dict()
    sorted_column_null_count = dict(sorted(column_null_count.items(), key=lambda item: item[1], reverse= True))
    
    return list(sorted_column_null_count.keys())

def task_2():
    df_result = pd.DataFrame(columns=['year', 'total_admissions'])
    df_filtered_data = df_bellevue.dropna(subset=['disease'])
    df_result['year'] = pd.to_datetime(df_filtered_data['date_in'])
    df_result['year'] = df_result['year'].dt.year

    total_admissions = df_result.groupby('year').size().reset_index(name='total_admissions')
    return total_admissions

def task_3():
    average_age_by_gender = df_bellevue.groupby('gender')['age'].mean().dropna()
    return average_age_by_gender

def task_4():
    top_5_professions = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top_5_professions