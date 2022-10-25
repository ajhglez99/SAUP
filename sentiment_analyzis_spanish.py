from sentiment_analysis_spanish import sentiment_analysis
import pandas as pd
import math

def clean_data(df):
    """Remove NaN values and empty strings"""
    df.dropna(inplace=True)
    df.drop_duplicates(subset=None, inplace=True)

    blanks = []  # start with an empty list

    for i,date,rating,title,opinion,attraction in df.itertuples():
        if type(opinion) == str:
            if opinion.isspace():
                blanks.append(i)

    df.drop(blanks, inplace=True)

def class_asigner(values):
    """Asign a class between 1 and 5 to each value"""
    class_list = []

    for value in values:
        class_value = math.ceil(value * 4)
        class_list.append(class_value)

    return class_list

def dataset_setup():
    """Preprosess the dataset for Rest_mex_DL_EDA algorithm"""
    
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    df = pd.read_csv('/content/SAUP/datasets/reviews.csv')
    df.head()

    clean_data(df)

    #calculate polarity
    df['Full Opinion'] = df.Title + ' ' + df.Opinion
    df.head()

    df['Score'] = df['Full Opinion'].apply(lambda opinion: sentiment.sentiment(opinion))
    df.head()

    df['Polarity'] = class_asigner(df['Score'])
    df.head()

    #save file for analyzis purpose with extra data
    df.to_csv('/content/SAUP/datasets/dataset.csv', index = False)

    # rearrange columns
    df_reorder = df[['Title', 'Opinion', 'Polarity', 'Attraction']]

    #save file
    writer = pd.ExcelWriter('/content/SAUP/datasets/dataset.xlsx')
    df_reorder.to_excel(writer, index = False)
    writer.save()

if __name__ == "__main__":
    dataset_setup()