import requests
from bs4 import BeautifulSoup

url = 'https://www.steamcardexchange.net/index.php?gamepage-appid-1119980'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('img')

for image in images:
    if 'src' in image.attrs:
        src = image['src']
        if src.startswith('https://cdn.cloudflare.steamstatic.com/steamcommunity/public/images/items/1119980'):
            response = requests.get(src)
            filename = src.split('/')[-1]
            with open(filename, 'wb') as f:
                f.write(response.content)