import pandas as pd

def clean_data(df):
    """Remove NaN values and empty strings"""
    df.dropna(inplace=True)
    df.drop_duplicates(subset=None, inplace=True)

    blanks = []  # start with an empty list

    for i,title,opinion,polarity,attraction in df.itertuples():
        if type(opinion) == str:
            if opinion.isspace():
                blanks.append(i)

    df.drop(blanks, inplace=True)

def prepare_dataset():
    df = pd.read_csv('./datasets/database_preprossed.csv')
    df.head()

    df['Attraction'] = 'Unknown'

    # rearrange columns
    df_reorder = df[['Title', 'Opinion', 'Polarity', 'Attraction']]
    
    clean_data(df_reorder)

    #save file
    writer = pd.ExcelWriter('./datasets/database_preprossed_2.xlsx')
    df_reorder.to_excel(writer, index = False)
    writer.save()

if __name__ == "__main__":
    prepare_dataset()