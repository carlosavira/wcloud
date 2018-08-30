
from os import path

from wordcloud import WordCloud, STOPWORDS
import random
import os
import numpy as np
from PIL import Image

currdir = os.path.dirname(__file__)
asanakasave = input("Please enter text file path (ex: C://Users/name/):")
unsafilename = input("Enter file name of text file:")

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)
    
d = path.dirname(asanakasave)

# Read the whole text.
text = open(path.join(d, unsafilename+".txt")).read()

# Generate a word cloud image
#wordcloud = WordCloud(background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:f
import matplotlib.pyplot as plt


mask = np.array(Image.open(os.path.join(currdir,"duts.png")))
stopwords = set(STOPWORDS)
# lower max_font_size
#wordcloud = WordCloud(background_color='white',max_font_size=40, mask=mask, stopwords = stopwords).generate(text)
wordcloud = WordCloud(background_color='maroon',mask=mask, stopwords = stopwords, max_words=500).generate(text)
fig = plt.figure(figsize=(80,50))

plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")



plt.axis("off")
#plt.show()

topng = fig.savefig(asanakasave + unsafilename+'.png', bbox_inches='tight', pad_inches=0)