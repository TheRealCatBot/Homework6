import json
import requests

SERVICE_URL = "https://www.mes.gov.ge/index.php?lang=geo"
header = {"content-type": "application/json"}

books = {}


response = requests.get("https://www.mes.gov.ge/index.php?lang=geo")
if 200 <= response.status_code < 300:
   print(response.text.count("განათლება"))
   with open("response.json", "wb") as f:
      f.write(response.content)
else:
   print(f"Error occurred. Status code - {response.status_code}")


response = requests.get("https://httpbin.org/image/jpeg")
yes =  response.headers["Content-Type"].split('/')[1]
file = open(f"sample_image.{yes}", "wb")
file.write(response.content)
file.close()

response = requests.get("https://httpbin.org/image/jpeg")
yes = response.headers["Content-Type"].split('/')[1]
file = open(f"sample_image.{yes}", "wb")
file.write(response.content)
file.close()

response = requests.get("https://httpbin.org/image/png")
yes = response.headers["Content-Type"].split('/')[1]
file = open(f"sample_image.{yes}", "wb")
file.write(response.content)
file.close()

response = requests.get("https://httpbin.org/image/svg")
yes = response.headers["Content-Type"].split('/')[1]
file = open(f"sample_image.{yes}", "wb")
file.write(response.content)
file.close()

response = requests.get("https://httpbin.org/image/webp")
yes = response.headers["Content-Type"].split('/')[1]
file = open(f"sample_image.{yes}", "wb")
file.write(response.content)
file.close()

response = requests.get("https://httpbin.org/ip")
t = json.loads(response.text)
with open("my-ip.txt", 'w', encoding='utf-8') as file:
   file.write(t.get('origin'))