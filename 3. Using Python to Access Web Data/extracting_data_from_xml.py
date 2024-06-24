import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL for the data file
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1778265.xml'  # default URL for actual data

# Retrieve the XML data from the URL
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

# Parse the XML data
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

# Find all <count> elements using XPath
counts = tree.findall('.//count')

# Calculate the sum of all <count> values
sum_counts = 0
for count in counts:
    sum_counts += int(count.text)

# Print the count of <count> elements and the sum of <count> values
print('Count:', len(counts))
print('Sum:', sum_counts)
