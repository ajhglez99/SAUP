from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

def class_asigner(value):
    """Asign a class between 1 and 5 to each value"""
    class_value = round(value * 2.4999) + 3

    return class_value

def dataset_setup():
    """Preprosess the dataset for Rest_mex_DL_EDA algorithm"""
    
    sid = SentimentIntensityAnalyzer()

    with open('/content/SAUP/datasets/database.csv', 'r', encoding="utf-8") as file_obj:
        reader = csv.reader(file_obj)
        row_list = list(reader)

        for row in row_list:
            if row == row_list[0]:
                row_list[0].append('Polarity')
            else:
                try:
                    score = sid.polarity_scores(row[1] + ' ' + row[2])
                    polarity = class_asigner(score['compound'])
                    row.append(polarity)
                except:
                    row.append(-1000)
                    print("unknown character in the review")

    with open('/content/SAUP/datasets/database_preprosses.csv', 'a', encoding="utf-8") as file_obj:
        writer = csv.writer(file_obj, lineterminator='\n')

        for row in row_list:
            writer.writerow(row)

if __name__ == "__main__":
    dataset_setup()