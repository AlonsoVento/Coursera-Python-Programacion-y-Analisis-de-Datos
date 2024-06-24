from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for the URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Retrieve and print the initial URL
print('Retrieving:', url)

# Repeat the process for the specified number of times
for i in range(count):
    # Open the URL and parse the HTML using BeautifulSoup
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    
    # Find all anchor tags and get the href attribute of the one at the specified position
    tags = soup('a')
    url = tags[position - 1].get('href', None)
    
    # Print the URL being retrieved
    print('Retrieving:', url)

# Print the last name retrieved from the final URL
print('The answer to the assignment for this execution is:', url.split('_')[-1].split('.')[0])