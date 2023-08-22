import os
import re

# Get the python_scripts environment variable
python_scripts = os.environ.get("pythons")

# Split the URLs into a list
urls = cleaned_urls.strip().split('\n')

# Initialize a list to hold the generated SVN URLs
svn_urls = []

# Loop through each URL
for url in urls:
    # Replace /tree/branchName or /blob/branchName with /trunk
    svn_url = re.sub(r'/tree/[^/]+|/blob/[^/]+', '/trunk', url)
    svn_url =  re.sub(r'%0D', '', svn_url)
    svn_urls.append(svn_url)

# Print the generated SVN URLs separated by newline
print('\n'.join(svn_urls))
