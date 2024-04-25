import nltk
from nltk.corpus import stopwords
import re
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
nltk.download('stopwords')
english_stopwords = stopwords.words("english")

with open("testdata/miracle_in_the_andes.txt", encoding="utf-8") as file:
    book = file.read()

pattern = re.compile("[a-zA-Z]+")
matches = re.findall(pattern, book.lower())

dict_word = {}
for word in matches:
    if word in dict_word.keys():
        dict_word[word] = dict_word[word] + 1
    else:
        dict_word[word] = 1

d_list = [(value, key) for (key, value) in dict_word.items()]
d_list = sorted(d_list, reverse=True)

filtered_words = []
for count, word in d_list:
    if word not in english_stopwords:
        filtered_words.append((word, count))


# print(filtered_words[:10])


analyzer = SentimentIntensityAnalyzer()
print(analyzer.polarity_scores("love hate"))