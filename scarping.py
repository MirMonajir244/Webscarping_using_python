# pip install bs4
# pip install html5lib
# pip install requests
import requests
import pyttsx3
from bs4 import BeautifulSoup
url = input("Enter your full website link: ")
pyttsx3.speak("You Have Entered a website please wait I am Working on it")

# Get The HTML

req = requests.get(url)
HtmlContent = req.content
# print(HtmlContent)

# Parsing the HtmlContent
soup = BeautifulSoup(HtmlContent, 'html.parser')
# print(soup.prettify) #prettify make the HtmlContent's pretty

# Travarse the Soup
# Get all the paragraph tag
paragraph = soup.find_all('p')
print(paragraph)

print('#'*125)

# get all the anchor link

anchor = soup.find_all('a')
links = set()
for link in anchor:
    if(link.get('href') != '#'):
        textlink = link.get('href')
        links.add(link)
        print(textlink)
