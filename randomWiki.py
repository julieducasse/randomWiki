import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import re,random

http = httplib2.Http()
# status, response = http.request("https://en.wikipedia.org/wiki/Pinot_noir_passing-off_controversy")

# for link in BeautifulSoup(response, parse_only=SoupStrainer('a'),features="html.parser"):
#         if link.has_attr('href') and re.search("^/wiki/",link['href']):
#             print(link['href'])

# soup = BeautifulSoup(response, parse_only=SoupStrainer('a'),features="html.parser")     
# res= soup.findAll(attrs={'href': re.compile(r"^/wiki/")})

f = open("lastlink.txt", "r")
testlink=f.read()

print("The first link is: " + testlink)
def returnrandompage(page):
    #page argument is the string
    status, response = http.request(page)
    soup = BeautifulSoup(response,features="html.parser") 
    content=soup.find("div",{"class": "mw-parser-output"})    
    res = content.findAll(attrs={'href': re.compile(r"^/wiki/[^:]+$")})
    print(len(res))
    randchoice=random.choice(res) 
    return randchoice['href']

nextlink=testlink
for x in range(5):
    nextlink = returnrandompage(nextlink)
    nextlink = "https://en.wikipedia.org/" + nextlink
    print(nextlink)

f = open("lastlink.txt", "w")
f.write(nextlink)
f.close()
