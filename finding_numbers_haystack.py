import re
import urllib.request

# Descargar y leer el contenido del archivo
url = "http://py4e-data.dr-chuck.net/regex_sum_1778261.txt"
response = urllib.request.urlopen(url)
data = response.read().decode()

# Encontrar todos los números en el archivo usando expresiones regulares
numbers = re.findall(r'[0-9]+', data)

# Convertir los números encontrados de cadenas a enteros
numbers = [int(num) for num in numbers]

# Calcular la suma de los números
total_sum = sum(numbers)

# Imprimir la suma total
print("La suma de los números en el archivo es:", total_sum)
