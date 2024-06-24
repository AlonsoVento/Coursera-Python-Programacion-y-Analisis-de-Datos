#Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ingresar la URL del archivo HTML
url = input('Enter URL - ')
if not url:
    url = 'http://py4e-data.dr-chuck.net/comments_1778263.html'

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Inicializar la suma
total_sum = 0

# Encontrar todas las etiquetas <span> con clase "comments"
tags = soup.find_all('span', class_='comments')
for tag in tags:
    # Extraer el contenido de texto de la etiqueta <span>, convertirlo a entero y agregarlo a la suma
    total_sum += int(tag.text)

# Mostrar el resultado
print("Sum:", total_sum)