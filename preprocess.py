"""
Preprocess
@author Sydney Magee
@version 10.20.21

This file is used to combine the "Netflix Movies and TV Shows" dataset
and the "Amazon Prime Video Movies and TV Shows" dataset.

Both datasets were sourced from Kaggle, an open source data hub.
"Netflix Movies and TV Shows" - https://www.kaggle.com/shivamb/netflix-shows
"Amazon Prime Video Movies and TV Shows" - https://www.kaggle.com/shivamb/amazon-prime-movies-and-tv-shows

Output: cleaned_movie_data.csv

"""
import pandas as pd
import numpy as np
# from scipy.sparse import csr_matrix
# from sklearn.neighbors import NearestNeighbors
# import matplotlib.pyplot as plt
# import seaborn as sns

# takes a file and returns a dataframe
def readcsv(file):
    return pd.read_csv(file)

# Removes tv show data, returns only movie data
# Combines the two datasets
def makemovieset(df_a, df_n):
    newdf_a = df_a[df_a.type != 'TV Show']
    newdf_n = df_n[df_n.type != 'TV Show']
    frames = [newdf_a, newdf_n]
    combined_df = pd.concat(frames)
    return combined_df
 
# takes a dataframe and performs preprocessing techniques
def clean(df):
    df['date_added'].replace('', np.nan, inplace=True)
    df.dropna()
    df.drop_duplicates()
    print(df.head())
    return df        

# takes the preprocessed dataframe and exports a csv file
def exportcsvfile(df):
    df.to_csv('cleaned_movie_data.csv')

def main():
    df_a = []
    df_a = readcsv('./Data/amazon_prime_titles.csv')
    df_n = []
    df_n = readcsv('./Data/netflix_titles.csv')
    newdf = []
    newdf = makemovieset(df_a, df_n)
    result = clean(newdf)
    exportcsvfile(result)

if __name__ == "__main__":
    main()



