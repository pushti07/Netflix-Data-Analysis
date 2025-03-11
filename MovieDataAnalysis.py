import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("mymoviedb.csv" , lineterminator='\n')

df.head()

df.info()

df.isnull().sum()

df['Genre'].head(10)

df['Release_Date'].dtypes

df.duplicated().sum()

df.describe()

df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)

df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes

df.head()

cols = ['Overview','Original_Language','Poster_Url']
df.drop(cols, axis = 1, inplace = True)

def categorize_col(df, col, label):
    edges = [
        df[col].describe()['min'],
        df[col].describe()['25%'],
        df[col].describe()['50%'],
        df[col].describe()['75%'],
        df[col].describe()['max']
    ]
    
    df[col] = pd.cut(df[col], bins = edges, labels = label, duplicates = 'drop')
    return df


labels = ['not_popular', 'below_average', 'average', 'popular']
categorize_col(df, 'Vote_Average', labels)
print(df['Vote_Average'].unique())