import os

# Define the current directory
current_directory = '.'

# Filter and list only files
files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

# Display the files
print("Files in the current directory:")
for file in files:
    print(file)
