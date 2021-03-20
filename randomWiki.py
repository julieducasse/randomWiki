import requests
from bs4 import BeautifulSoup
import re,random, telegram,time 

not_wanted_words = ["ISBN","ISO","(identifier)"]

def doesContain(link,words):
    match=link.split("https://en.wikipedia.org/wiki/",1)[1]
    for w in words:
        if match.__contains__(w):
        # if match.startswith(w):
            print("it's matching: ",match)
            return True
    return False

def returnrandompage(page):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, features="html.parser")
    mainContent = soup.find(id='mw-content-text')
    links = mainContent.findAll(attrs={'href': re.compile(r"^/wiki/[^:]+$")})
    res = random.choice(links)['href']
    return(res)

# Bot
bot_token = ""
bot_chatID_julie = ""
bot_chatID_arun = ""

bot = telegram.Bot(token=bot_token)



# Get the first link
f = open("lastlink.txt", "r")
nextlink=f.read()
print("The first link is: " + nextlink)

# Find the next 3 random links
for x in range(3):
    nextlink = returnrandompage(nextlink)
    #nextlink ="/wiki/ISBN_(identifier)"
    nextlink = "https://en.wikipedia.org" + nextlink
    print(nextlink)
    while doesContain(nextlink,not_wanted_words):
        nextlink = returnrandompage(nextlink)
        # nextlink ="/wiki/ISBN_(identifier)"
        nextlink = "https://en.wikipedia.org" + nextlink
        print("im loopin, found unwanted link: ",nextlink)
    # print("ive finished while loop or sent message, beurk")
    bot.sendMessage(chat_id=bot_chatID_arun, text=nextlink)  
    bot.sendMessage(chat_id=bot_chatID_julie, text=nextlink)
    #sendtext = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + nextlink
    #requests.get(sendtext)
    time.sleep(1)


# Save the last link
f = open("lastlink.txt", "w") 
f.write(nextlink)
f.close()

#https://api.telegram.org/bot<bottoken>/getUpdates
