import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


new_york_tweets = pd.read_json("new_york.json", lines=True)
london_tweets = pd.read_json("london.json", lines=True)
paris_tweets = pd.read_json("paris.json", lines=True)

# Classifying using language: Naive Bayes Classifier

new_york_text = new_york_tweets["text"].tolist()
london_text = new_york_tweets["text"].tolist()
paris_text = new_york_tweets["text"].tolist()

all_tweets = new_york_text + london_text + paris_text
labels = [0] * len(new_york_text) + [1] * len(london_text) + [2]* len(paris_text)

# Train and test set
train_data, test_data, train_labels, test_labels = train_test_split(all_tweets, labels, test_size=0.2, random_state=1)

# Making the count vectors
counter = CountVectorizer()

counter.fit(train_data)

train_counts = counter.transform(train_data)

test_counts = counter.transform(test_data)

# Training the classifier
classifier = MultinomialNB()

classifier.fit(train_counts, train_labels)

predictions = classifier.predict(test_counts)

print(accuracy_score(test_labels, predictions))

