import pandas as pd
import pickle

column = ['comment']
df = pd.read_csv('dataset.csv', encoding ='utf8', sep=',')

def remove_stopwords(df_fon):
    stopwords = open('turkish-stop-words', 'r').read().split()
    df_fon['stopwords_removed'] = list(map(lambda doc:
        [word for word in doc if word not in stopwords], df_fon['comment']))

remove_stopwords(df)

X = df['comment']
y = df['positivity']

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer(encoding ='iso-8859-9').fit(X)
pickle.dump(vect, open('vect.pkl', 'wb'))

X_vectorized = vect.transform(X) 

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_vectorized, y)

pickle.dump(model, open('model.pkl','wb'))