import os
import re
import subprocess

# Get the python_scripts environment variable
python_scripts = os.environ.get("pythons")

# Split the URLs into a list
urls = python_scripts.strip().split('\n')


# Loop through each URL
for url in urls:
    # Replace /tree/branchName or /blob/branchName with /trunk
    svn_url = re.sub(r'/tree/[^/]+|/blob/[^/]+', '/trunk', url)
    
    # Perform the svn export using subprocess
    subprocess.run(["svn", "export", svn_url, steps.get_path.outputs.path])
