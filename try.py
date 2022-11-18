import requests
from bs4 import BeautifulSoup
import re
import sys

print(sys.argv)


page = requests.get(f"https://www.google.com/search?q=donald+trump")
soup = BeautifulSoup(page.content, "html.parser")



# with open("index.html", "w") as index:
#     index.write(str(soup))

