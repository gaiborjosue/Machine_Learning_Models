import os
import re
import subprocess

# Get the python_scripts environment variable
python_scripts = "https://github.com/gaiborjosue/Machine_Learning_Models/tree/test/NaiveBayes/Email_Similarity\nhttps://github.com/gaiborjosue/Machine_Learning_Models/tree/test/NaiveBayes/Email_Similarity"
# Split the URLs into a list
urls = python_scripts.split('\n')

# Loop through each URL
for url in urls:
    svn_url = re.sub(r'/tree/[^/]+|/blob/[^/]+', '/trunk', url)
    
    # Perform the svn export using subprocess
    print(svn_url)
