import requests
from bs4 import BeautifulSoup
import random

# Web sitesinin URL'si
url = 'https://www.neoldu.com/motivasyon-sozleri-motive-edici-sozler-38505h.htm'

# Web sitesine bağlanma
r = requests.get(url)

# BeautifulSoup kullanarak HTML kodunu analiz etme
soup = BeautifulSoup(r.content, 'html.parser')

# Tüm "text_content" sınıfına sahip div elemanlarını bulma
divs = soup.find_all('div', {'class': 'text_content'})

# Her bir div elemanının altındaki p elemanlarını ekrana yazdırma
p_elements = [p for div in divs for p in div.find_all('p')]
if p_elements:
    print(random.choice(p_elements).text)
else:
    print("Hiç p elementi yok.")