from deep_translator import GoogleTranslator
import pandas as pd

def translate_reviews():
    df = pd.read_csv('./datasets/reviews.csv')
    df.head()

    df['Title'] = df['Title'].apply(lambda title: GoogleTranslator(
        source='es', target='en').translate(title))
    df.head()

    df['Opinion'] = df['Opinion'].apply(lambda opinion: GoogleTranslator(
        source='es', target='en').translate(opinion))
    df.head()

    #save file for analyzis purpose with extra data
    df.to_csv('./datasets/reviews_translated.csv', index = False)

if __name__ == "__main__":
    translate_reviews()