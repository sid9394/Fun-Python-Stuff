from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
from RAKE import rake_words
import matplotlib.pyplot as plt

filename = 'AllTweetText.txt'

with open(filename) as myfile:
    data = myfile.read()

    final = rake_words(data)
    final = str(final)
    print(final)

    alice_coloring = np.array(Image.open("maxresdefault_burned.png"))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(final)

    wc.to_file("C:\\Users\\sidharth.m\\Desktop\\srk_tweetcolor.jpg")
    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    fig, axes = plt.subplots(1, 3)
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()

