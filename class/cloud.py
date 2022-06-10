import numpy as np
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
from PIL import Image

text = open("cloud.txt").read()
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud)
wordcloud = WordCloud(width=800,
                      height=500,
                      max_words=30,
                      prefer_horizontal=0.1,
                      background_color="rgba(255,0,255,0)",
                      mode="RGBA").generate(text)

plt.imshow(wordcloud)
wordcloud.to_file("wordcloud.png")


dove_mask = np.array(Image.open("wordcloud.png"))
#dove_mask[230:250, 240:250]
print(dove_mask)
plt.imshow(dove_mask)
wordcloud = WordCloud(
    mask=dove_mask,
    contour_width=3,
    max_words=20,
    repeat=True,
    prefer_horizontal=0.5,
    min_font_size=3,
    background_color="rgba(0,255,0,255)",
    contour_color='black')

# Generate a wordcloud
wordcloud.generate(text)

# store to file
wordcloud.to_file("dove_wordcloud.png")

# show

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
