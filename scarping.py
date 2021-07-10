#pip install bs4
#pip install html5lib
#pip install requests
import requests
from bs4 import BeautifulSoup
url = "https://ums.lpu.in/"

#Get The HTML

req = requests.get(url)
HtmlContent = req.content
print(HtmlContent)