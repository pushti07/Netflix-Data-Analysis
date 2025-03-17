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

df['Vote_Average'].value_counts()

df.dropna(inplace = True)
df.isna().sum()


# We'd split genres into a list and then explode our DataFrame to have only one genre per row for each movie
df['Genre'] = df['Genre'].str.split(', ')

df = df.explode('Genre').reset_index(drop = True)
df.head()

# casting Column into Category
df['Genre'] = df['Genre'].astype('category')

df['Genre'].dtypes

df.nunique()


#visualizing genre column
sns.catplot(y = 'Genre', data = df, kind = 'count', order = df['Genre' ].value_counts().index, color = '#4287f5')
plt.title('genre column distribution' )
plt.show()


# visualizing vote_average column
sns.catplot(y = 'Vote_Average', data = df, kind = 'count', order = df['Vote_Average' ].value_counts().index, color = '#4287f5')
plt.title('votes destribution' )
plt.show()


df[df['Popularity'] == df['Popularity'].max()]


df[df['Popularity'] == df['Popularity'].min()]


df['Release_Date'].hist()
plt.title('Release_Date column distribution')
plt.show()


### Q1: What is the most frequent genre in the dataset?

#### Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the times among 19 other genres.

### Q2: What genres has highest votes ?

#### we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by being having more than 18.5% of movies popularities.

### Q3: What movie got the highest popularity ? what's its genre ?

#### Spider-Man: No Way Home has the highest popularity rate in our dataset and it has genres of Action, Adventure and Sience Fiction.

### Q3: What movie got the lowest popularity ? what's its genre ?

#### The united states, thread' has the highest lowest rate in our dataset and it has genres of music , drama , 'war', 'sci-fi' and history'.

### Q4: Which year has the most filmmed movies?

#### year 2020 has the highest filmming rate in our dataset.
