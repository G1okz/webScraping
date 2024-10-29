import requests
from bs4 import BeautifulSoup

"""
Práctica Web Scraping de una página web de noticias.
Muestra el título, contenido y una lista de elementos de la página.

@author: Miguel Reyna
"""

URL = 'https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Extract the title of the article
title = soup.find('title').get_text()

# Extract the content of the article
content = soup.find('div', class_='article-content').find_all('p')

# Remove last two lines
for p in content:
    for em in p.find_all('em'):
        em.decompose()

# Join the text from all <p> tags into a single string
content_trimmed = '\n'.join([p.get_text() for p in content])

# Get all <li> tags that contain the following attribute:
# class="masthead-nav-topics-item"
contentli = soup.find_all('li', class_='masthead-nav-topics-item')

print("Title: " + title)
print("Content: ")
print(content_trimmed)
print("Content list: ")
print(contentli)
