import wikipedia
from bs4 import BeautifulSoup

result = wikipedia.page('davidmklklklklklk').html()
soup = BeautifulSoup(result, "html.parser")
# res = soup.find_all("infobox-label")

# print(soup.prettify())
# for info in res:
#     print(info)
# with open("index.html", "w") as index:
#     index.write(str(soup))

info_data = soup.select('.infobox-data')
info_label = soup.select('.infobox-label')
data_dict = {}

for i in range(len(info_label)):
    # if info_label.text.lower() == "occupation":
    #     info_data.select()
    data_dict[info_label[i].text] = info_data[i].text

with open("log.txt", "w") as log:
    log.write(str(data_dict))
