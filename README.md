# 📊 Netflix Movie Data Analysis

This project analyzes a Netflix movie dataset to uncover trends in genres, votes, and popularity over the years. The analysis includes data preprocessing, feature engineering, and visualization to extract meaningful insights.

---

## 🚀 Project Overview
This project aims to:
- Clean and preprocess the Netflix movie dataset.  
- Analyze the relationship between genres, votes, and popularity.  
- Visualize key trends using Seaborn and Matplotlib.  
- Identify the most popular movies and genres.  

---

## 📂 Dataset
**Filename:** `mymoviedb.csv`  
The dataset includes the following columns:
- `Title` – Name of the movie  
- `Genre` – Genres associated with the movie  
- `Release_Date` – Date of release  
- `Vote_Average` – Average votes received  
- `Popularity` – Popularity score of the movie  
- `Overview` – Summary of the movie  
- `Original_Language` – Language of the movie  
- `Poster_Url` – URL of the movie's poster  

---

## 🛠️ Data Preprocessing
1. **Reading and Cleaning Data**  
   - Loaded the dataset using `pandas`.  
   - Handled missing values and duplicates.  
   - Dropped irrelevant columns (`Overview`, `Original_Language`, `Poster_Url`).  
   
2. **Feature Engineering**  
   - Converted `Release_Date` to year format.  
   - Split `Genre` into separate rows using `explode`.  
   - Categorized `Vote_Average` into four categories:
     - `not_popular`
     - `below_average`
     - `average`
     - `popular`  

---

## 📈 Data Analysis and Visualization
1. **Genre Distribution**  
   - Drama is the most frequent genre, appearing in over **14%** of the movies.  
   - Visualized using a bar plot with `Seaborn`.  

2. **Vote Distribution**  
   - 25.5% of the movies are categorized as "popular."  
   - Drama has the highest popularity among fans, representing over **18.5%** of the dataset.  

3. **Most and Least Popular Movies**  
   - **Most Popular:** *Spider-Man: No Way Home* (Genres: Action, Adventure, Science Fiction)  
   - **Least Popular:** *The United States, Thread* (Genres: Music, Drama, War, Sci-Fi, History)  

4. **Release Year Distribution**  
   - 2020 had the highest number of releases.  

---

## 🎯 Insights
✅ Drama is the dominant genre.  
✅ High correlation between votes and popularity for drama.  
✅ Spider-Man: No Way Home stands out in terms of popularity.  
✅ 2020 was a major release year for Netflix.  

---

## 🖥️ Technologies Used
- **Python**  
- **Pandas**  
- **NumPy**  
- **Matplotlib**  
- **Seaborn**  

---

