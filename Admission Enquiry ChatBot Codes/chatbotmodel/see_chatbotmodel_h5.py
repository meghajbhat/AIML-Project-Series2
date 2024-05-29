#NAME : MEGHA BHAT
#EMAIL : meghajbhat@gmail.com

import h5py

# Path to your .h5 file
file_path = 'chatbotmodel.h5'

# Open the .h5 file in read mode
with h5py.File(file_path, 'r') as file:
    # List all groups
    print("Keys: %s" % file.keys())
    a_group_key = list(file.keys())[0]

    # Get the data from the first group
    data = list(file[a_group_key])

    # Print the data
    print(data)
