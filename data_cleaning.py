import pandas as pd
import contractions
from sqlite3 import connect
import nltk
import re
from nltk.corpus import stopwords

def clean(text):
    text = text.lower()
    # get rid of contractions
    text = contractions.fix(text)
    text = re.sub(r'@\w+|#\w+|http\S+', '', text)
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = nltk.word_tokenize(text, preserve_line=True)
    # removing stop words
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    # join the clean words back to a sentence
    clean_word = ' '.join(tokens)
    return clean_word

def main():
    nltk.download('stopwords')
    nltk.download('punkt')
    conn = connect("youtube_data_db.sqlite")
    df = pd.read_sql_query('SELECT text_original FROM Comments', conn)
    df['cleaned_text'] = df['text_original'].apply(clean)
    print(df[['text_original', 'cleaned_text']].head())






if __name__ == "__main__":
    main()