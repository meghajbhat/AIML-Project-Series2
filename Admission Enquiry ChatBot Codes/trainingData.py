#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', ',', '.']

# Process each intent and pattern
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(list(set(words)))

classes = sorted(list(set(classes)))

pickle.dump(words, open('C:\\Users\\Meghabhat\\Desktop\\2 (Admission Enquiry ChatBot)\\Admission Enquiry ChatBot Codes\\words\\words.pkl', 'wb'))
pickle.dump(classes, open('C:\\Users\\Meghabhat\\Desktop\\2 (Admission Enquiry ChatBot)\\Admission Enquiry ChatBot Codes\\classes\\classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

# Create the training data
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])

# Verify that all elements have the correct shape
for i, (bag, output_row) in enumerate(training):
    if len(bag) != len(words) or len(output_row) != len(classes):
        print(f"Error in training data at index {i}: bag length {len(bag)}, output_row length {len(output_row)}")

random.shuffle(training)
training = np.array(training, dtype=object)

# Separate features and labels
train_x = np.array(list(training[:, 0]), dtype=float)
train_y = np.array(list(training[:, 1]), dtype=float)

# Define the model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile and train the model
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)
model.save('C:\\Users\\Meghabhat\\Desktop\\2 (Admission Enquiry ChatBot)\\Admission Enquiry ChatBot Codes\\chatbotmodel\\chatbotmodel.keras')

print('Done')
