import pandas as pd

all_tweets = pd.read_json("random_tweets.json", lines=True)

import numpy as np

median_retweets = all_tweets['retweet_count'].median()

all_tweets['is_viral'] = np.where(all_tweets['retweet_count'] > median_retweets, 1, 0)

all_tweets['tweet_length'] = all_tweets.apply(lambda tweet: len(tweet['text']), axis=1)

all_tweets['followers_count'] = all_tweets.apply(lambda tweet: tweet['user']['followers_count'], axis=1)

all_tweets['friends_count'] = all_tweets.apply(lambda tweet: tweet['user']['friends_count'], axis=1)

all_tweets['hashtag_count'] = all_tweets.apply(lambda tweet: tweet['text'].count("#"), axis=1)


from sklearn.preprocessing import scale

labels = all_tweets['is_viral']

data = all_tweets[['tweet_length', 'followers_count', 'friends_count', 'hashtag_count']]

scaled_data = scale(data, axis=0)

# Creating training and testing set
from sklearn.model_selection import train_test_split

training_data, testing_data, training_labels, testing_labels = train_test_split(data, labels, test_size=0.2, random_state=1)

# Use the classifier
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

scores = []
for k in range(1, 200):
  classifier = KNeighborsClassifier(n_neighbors=k)

  classifier.fit(training_data, training_labels)

  scores.append(classifier.score(testing_data, testing_labels))

plt.plot(scores)
plt.show()

