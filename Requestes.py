import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

# -----------------------
# 1. Simple GET request
# -----------------------
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(f"Statut HTTP : {response.status_code}")
try:
    print("Réponse JSON :")
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("⚠️ La réponse n'est pas du JSON.")

# -----------------------
# 2. GET request with incorrect reference fixed
# -----------------------
response = requests.get("https://www.example.com")
print(f"Contenu brut de la réponse : {response.content}")

# -----------------------
# 3. POST request with JSON data
# -----------------------
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data)
try:
    print("Réponse JSON après POST :")
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("⚠️ La réponse n'est pas du JSON.")

# -----------------------
# 4. Handling error response (404)
# -----------------------
response = requests.get("https://httpbin.org/status/404")
if response.status_code != 200:
    print(f"Erreur HTTP : {response.status_code}")

# -----------------------
# 5. Timeout example
# -----------------------
url = "https://httpbin.org/delay/10"
try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print(f"Erreur de timeout : {err}")
except requests.exceptions.RequestException as err:
    print(f"Erreur de requête : {err}")

# -----------------------
# 6. Authorization Header
# -----------------------
auth_token = "XXXXXXXX"
headers = {
    "Authorization": f"Bearer {auth_token}"
}
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
try:
    print("Réponse avec en-tête d'authentification :")
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("⚠️ La réponse n'est pas du JSON.")

# -----------------------
# 7. Scraping with BeautifulSoup
# -----------------------
url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text if soup.title else "Pas de titre"
paragraph = soup.find("p").text if soup.find("p") else "Pas de paragraphe"
links = [a["href"] for a in soup.find_all("a") if "href" in a.attrs]
print(f"Titre : {title}\nParagraphe : {paragraph}\nLiens : {links}")

# -----------------------
# 8. urllib POST request
# -----------------------
data = urllib.parse.urlencode({"key": "value"}).encode("utf-8")
req = urllib.request.Request("https://www.example.com", data=data, method="POST")
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode("utf-8")
    print(f"Réponse après POST : {html}")
except urllib.error.URLError as e:
    print(f"Erreur URL : {e}")
