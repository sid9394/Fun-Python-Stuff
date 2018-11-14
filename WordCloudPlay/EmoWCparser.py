from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import pandas as pd
from RAKE import rake_words

path = "C:\\Users\\sidharth.m\\Desktop\\SRK tweet files\\EmoTweets\\sadtweet.xlsx"
df1 = pd.read_excel(path)
final_list = []
keyw_1 = []
keyw_2 = []
numlist = []
j = 1
list1 = []
for i, rows in df1.iterrows():

    list1.append(rows[7])
    comment_words = ' '
print(list1)
for val in list1:

    stopwords = set(STOPWORDS)

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    for words in tokens:
        comment_words = comment_words + words + ' '

text = comment_words

alice_mask = np.array(Image.open("srkoutlinefilled.jpg"))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=1, contour_color='black')

# generate word cloud
wc.generate(text)

wc.to_file("C:\\Users\\sidharth.m\\Desktop\\SRK tweet files\\EmoTweets\\sadtweet.jpg")