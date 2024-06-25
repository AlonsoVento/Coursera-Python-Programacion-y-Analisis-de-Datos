import json
import ssl
import urllib.request, urllib.parse, urllib.error

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Service URL
serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

# Get location from user
address_wanted = input("Enter location: ")

# Setting the GET parameters on the URL
parameters = {"q": address_wanted}
paramsurl = urllib.parse.urlencode(parameters)

# Generating the complete URL
queryurl = serviceurl.strip() + paramsurl.strip()
print("Retrieving", queryurl)

# Obtaining and reading the data
try:
    data_read = urllib.request.urlopen(queryurl, context=ctx).read()
    data = data_read.decode()
    print("Retrieved", len(data), "characters")
    
    # Debug: print the retrieved data
    print("Retrieved data:", data)
    
    # Parsing the data and looking for the field we want
    jsondata = json.loads(data)
    
    # Debug: print the JSON structure
    print("JSON structure:", json.dumps(jsondata, indent=4))
    
    if 'plus_code' in jsondata and 'global_code' in jsondata['plus_code']:
        plus_code = jsondata['plus_code']['global_code']
        print("Plus code", plus_code)
    else:
        print("Plus code not found in JSON data")
except Exception as e:
    print("Error:", e)