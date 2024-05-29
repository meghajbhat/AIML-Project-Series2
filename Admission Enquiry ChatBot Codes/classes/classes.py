#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import pickle

# Example data
classes = ['Location', 'classes', 'courseDuration', 'courses', 'exams', 'facilities', 'fee', 'funActivities', 'goodbye', 'greetings', 'hours', 'invalid', 'name', 'semDuration', 'semesters', 'studentRequirements', 'teachingStyle', 'thanks']

# Path to the PKL file
file_path = 'classes.pkl'

# Writing the data to a PKL file
with open(file_path, 'wb') as file:
    pickle.dump(classes, file)

print(f"Data has been written to {file_path}")
