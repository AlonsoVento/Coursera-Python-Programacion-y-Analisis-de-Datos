import socket

def get_http_headers(url):
    # Extract the host and document path from the URL
    host = 'data.pr4e.org'
    document = '/intro-short.txt'

    # Create a socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))

    # Send an HTTP GET request
    cmd = f'GET {document} HTTP/1.0\r\nHost: {host}\r\n\r\n'.encode()
    mysock.send(cmd)

    # Receive the response and print the headers
    response = ''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        response += data.decode()

    mysock.close()

    # Split the response into headers and body
    headers, body = response.split('\r\n\r\n', 1)

    # Print headers
    print(headers)

    return headers, body

# Retrieve and print the headers and body
headers, body = get_http_headers('http://data.pr4e.org/intro-short.txt')

# Print the body (optional)
# print(body)