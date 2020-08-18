# Import libraries:
import pandas as pd
from PIL import Image
from os import path
import numpy as np
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 90%%, %d%%)" % random.randint(50, 100)

# Import the text file:
dataset = pd.read_csv('whatsapp.txt', sep=' ', names=['time', 'message'])
# print(df1)
cleandataset = dataset['message'].str.split(":", expand=True,n=1)
message = pd.concat([dataset, cleandataset], axis=1)
message = df_all.rename(columns={'message': 'total', 0:'name', 1:'message'})
message.drop('total', axis=1, inplace=True)
message.loc[df_all.time.str.contains(r'[a-zA-Z]')==True, 'message'] = message[message.time.str.contains(r'[a-zA-Z]')==True].time
message.fillna(' ', inplace=True)
text = ' '.join(message['message'])

STOPWORDS.update(["i", "me", "my", "myself", "we", "our", 
	"ours", "ourselves", "you", "your", "yours", "yourself", 
	"yourselves", "he", "him", "his", "himself", "she", "her",
	 "hers", "herself", "it", "its", "itself", "they", "them", 
	 "their", "theirs", "themselves", "what", "which", "who", "whom", 
	 "this", "that", "these", "those", "am", "is", "are", "was", "were",
	  "be", "been", "being", "have", "has", "had", "having", "do", "does"
	  , "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", 
	  "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
	  "between", "into", "through", "during", "before", "after", "above",
	   "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
	    "under", "again", "further", "then", "once", "here", "there", "when", 
	    "where", "why", "how", "all", "any", "both", "each", "few", "more", 
	    "most", "other", "some", "such", "no", "nor", "not", "only", "own",
	     "same", "so", "than", "too", "very", "s", "t",
 "can", "will", "just", "don", "should", "now", ])

image_mask = np.array(Image.open("IU.jpg"))
wc = WordCloud(background_color="black", max_words=2000, mask=image_mask, stopwords=STOPWORDS.add("said"))
wc.generate(text)
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wc.to_file("word_cloud.png")

