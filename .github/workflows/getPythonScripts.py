import os
import re
import subprocess

# Get the python_scripts environment variable
python_scripts = "https://github.com/neuronets/trained-models/tree/master/DeepCSR/deepcsr/1.0/src\nhttps://github.com/neuronets/trained-models/tree/master/neuronets/ams/0.1.0/weights"

# Split the URLs into a list
urls = python_scripts.strip().split('\n')


# Loop through each URL
for url in urls:
    # Replace /tree/branchName or /blob/branchName with /trunk
    svn_url = re.sub(r'/tree/[^/]+|/blob/[^/]+', '/trunk', url)
    print(url)

