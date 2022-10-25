import pandas as pd
import numpy as np

def dataset_with_rating():
    df = pd.read_csv('./datasets/dataset.csv')
    df.head()

    df['Polarity'] = df.apply(lambda x: int(x['Rating'])/10, axis = 1)
    df.head()

    # rearrange columns
    df_reorder = df[['Title', 'Opinion', 'Polarity', 'Attraction']]

    #save file
    writer = pd.ExcelWriter('./datasets/dataset_rating.xlsx')
    df_reorder.to_excel(writer, index = False)
    writer.save()
    

def compare_rating_with_sa():
    df = pd.read_csv('./datasets/dataset.csv')
    df.head()

    df['Compare'] = df.apply(
        lambda x: abs(int(x['Rating'])/10 - int(x['Polarity'])), axis = 1)
    df.head()

    del df['Compound']
    del df['Date']
    del df['Opinion']
    del df['Score']
    del df['Attraction']

    #save file
    writer = pd.ExcelWriter('./datasets/dataset_test.xlsx')
    df.to_excel(writer, index = False)
    writer.save()

#compare_rating_with_sa()

dataset_with_rating()