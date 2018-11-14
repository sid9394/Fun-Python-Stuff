from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
from RAKE import rake_words

filename = 'AllTweetText.txt'

with open(filename) as myfile:
    data = myfile.read()

    final = rake_words(data)
    print(final)

    comment_words = ' '

for val in final:

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

wc.to_file("C:\\Users\\sidharth.m\\Desktop\\srk_tweetwc.jpg")