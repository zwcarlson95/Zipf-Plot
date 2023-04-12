
from operator import itemgetter
import nltk
import pandas as pd
from nltk.corpus import stopwords
from matplotlib import pyplot as plt

frequency = {}
words_doc = nltk.Text(nltk.corpus.reuters.words())
stop_words = set(stopwords.words('english'))

words_doc = [word.lower() for word in words_doc if word.isalpha()]
words_doc = [word for word in words_doc if word not in stop_words]

for word in words_doc:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

rank = 1
column_header = ['Rank', 'Frequency', 'Frequency * Rank']
df = pd.DataFrame(columns=column_header)
collection = sorted(frequency.items(), key=itemgetter(1), reverse=True)

for word, freq in collection:
    df.loc[word] = [rank, freq, rank * freq]
    rank = rank + 1

plt.figure(figsize=(20, 20))
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.xticks(rotation=90)

for word, freq in collection[:30]:
    plt.bar(word, freq)
plt.show()

