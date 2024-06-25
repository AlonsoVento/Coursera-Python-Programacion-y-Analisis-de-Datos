import urllib.request, urllib.parse, urllib.error
import json

# Prompt for a URL
url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_1778266.json'  # Default URL for testing

print('Retrieving', url)

# Read the JSON data from the URL
try:
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    # Parse the JSON datahttp://py4e-data.dr-chuck.net/comments_1778266.json
    js = json.loads(data)

    # Initialize sum and count of comments
    sum_counts = 0
    count = 0

    # Iterate through each comment and sum up the counts
    for comment in js['comments']:
        count += 1
        sum_counts += int(comment['count'])

    # Print out the count of comments and their sum
    print('Count:', count)
    print('Sum:', sum_counts)

except urllib.error.URLError as e:
    print('Failed to retrieve data:', e.reason)
except json.JSONDecodeError as e:
    print('Failed to parse JSON:', e)