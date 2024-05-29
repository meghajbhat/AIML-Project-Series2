#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import pickle

# Open the PKL file in read-binary mode
with open('classes.pkl', 'rb') as file:
    # Load the contents of the file
    data = pickle.load(file)

# Print the data to verify
print(data)
