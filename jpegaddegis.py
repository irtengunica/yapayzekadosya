import os.path
import glob
import shutil

source = "B270619_V1_K1" # Replace these variables with the appropriate data
dest = "B270619_V1_K1/txt"
command = "My command"

# Find the files that need to be copied
files = glob.glob(os.path.join(source))

# Copy the files to the destination
for file in files:
     shutil.copy(os.path.join(source), dest)

print("aaaa")
