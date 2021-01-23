import requests
from bs4 import BeautifulSoup
import re,random

def returnrandompage(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, features="html.parser")
    mainContent = soup.find(id='bodyContent')
    links = mainContent.findAll(attrs={'href': re.compile(r"^/wiki/[^:]+$")})
    res = random.choice(links)['href']
    return(res)

# Bot
bot_token = ""
bot_chatID = ""

# Get the first link
f = open("lastlink.txt", "r")
nextlink=f.read()
print("The first link is: " + nextlink)

# Find the next 5 random links
for x in range(5):
    nextlink = returnrandompage(nextlink)
    nextlink = "https://en.wikipedia.org" + nextlink
    print(nextlink)
    sendtext = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + nextlink
    requests.get(sendtext)

# Save the last link
f = open("lastlink.txt", "w")
f.write(nextlink)
f.close()

#https://api.telegram.org/bot<bottoken>/getUpdates
