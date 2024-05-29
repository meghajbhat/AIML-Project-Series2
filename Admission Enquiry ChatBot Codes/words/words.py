#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import pickle

# Example data
words = ["'s", 'Awesome', 'BBA', 'BIT', 'Day', 'Good', 'Goodbye', 'Greetings', 'Have', 'I', 'Is', 'See', 'Thank', 'Thanks', 'That', 'What', 'a', 'activity', 'admission', 'am', 'any', 'are', 'asbhk', 'available', 'be', 'by', 'bye', 'call', 'class', 'college', 'complete', 'conduct', 'course', 'curriculum', 'cya', 'day', 'different', 'doe', 'entry', 'exam', 'extra', 'facility', 'fee', 'for', 'format', 'from', 'fun', 'going', 'good', 'guy', 'gvsd', 'hello', 'helpful', 'helping', 'hey', 'hi', 'hour', 'how', 'in', 'infrastructure', 'is', 'it', 'later', 'leaving', 'like', 'located', 'location', 'long', 'many', 'me', 'month', 'much', 'name', 'of', 'one', 'open', 'operation', 'or', 'other', 'pattern', 'program', 'provided', 'requirement', 'see', 'semester', 'should', 'single', 'structure', 'student', 'study', 'style', 'take', 'teaching', 'thanks', 'the', 'there', 'this', 'to', 'up', 'what', 'when', 'where', 'who', 'will', 'ya', 'year', 'you', 'your']

# Path to the PKL file
file_path = 'words.pkl'

# Writing the data to a PKL file
with open(file_path, 'wb') as file:
    pickle.dump(words, file)

print(f"Data has been written to {file_path}")
