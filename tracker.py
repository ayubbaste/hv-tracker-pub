import os
import json
import requests
from bs4 import BeautifulSoup
from pyrogram import Client


# For Telegram
session_name = "any_name_you_want" # Str. Example: 'tracker_bot'
api_id = your API_ID # Digits. Example: 1112223
api_hash = "your API_HASH" # Str. Example: 'xx11111xxxx111x1111111x1x1xx11x1'
bot_token = "your BOT_TOKEN" # Str. Example: '1111111111:XXX111xXXXXxxExXx1xXXXXXx1xx1x_XxxX'
recipients = [CHAT_IDs] # Digits. Example: [-1112223334445, -2223334445556]

# URL to parse
url = "habr url" # Str.Example: 'https://career.habr.com/vacancies?divisions[]=backend&type=all'

# Here will be messages to send
messages = []

# BeautifulSoup
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
vcards = soup.find_all("div", "vacancy-card")

# Make/open a file with/for parsed vacancy links
try:
    with open('base.txt', "r+") as basefile:
        old_data = json.load(basefile)
        basefile.close()
except:
    with open('base.txt', "w+") as basefile:
        old_data = []
        json.dump(old_data, basefile)
        basefile.close()

# Vacancy data
for vcard in vcards:
    try:
        vdate = vcard.find("div", "vacancy-card__date").text
    except:
        pass

    try:
        vcotitle = vcard.find("div", "vacancy-card__company-title").text
    except:
        pass

    try:
        vtitle = vcard.find("a", "vacancy-card__title-link").text
    except:
        pass

    try:
        vsalary = vcard.find("div", "vacancy-card__salary").text
    except:
        pass

    try:
        skills = vcard.find("div", "vacancy-card__skills").text
    except:
        pass

    try:
        vurl = "https://career.habr.com" + vcard.find("a", "vacancy-card__title-link")["href"]
    except:
        pass

    if vurl not in old_data:
        old_data.append(vurl)

        # Build massages and add them to list
        message = "<i>%s</i>\
            \n<i>Co.</i> %s\
            \n<i>Vac.</i> <a href='%s'>%s</a>\
            \n<i>Sal.</i> %s\
            \n\n<i>Skills:</i>\
            \n<i>%s</i>" % (vdate, vcotitle, vurl, vtitle, vsalary, skills)

        messages.append(message)

# If there is a new vacancies
if len(messages) > 0:
    try:
        app = Client(
            session_name,
            api_id = api_id,
            api_hash = api_hash,
            bot_token = bot_token
        )

        # Send them with telegram
        for message in messages:
            async def main():
                async with app:
                    for recipient in recipients:
                        await app.send_message(recipient, message, parse_mode="html", disable_web_page_preview = True)
            app.run(main())

        # And add links to parsed vacancy links file
        with open('base.txt', "w+") as exportfile:
            json.dump(old_data, exportfile)
            exportfile.close()
    except:
        pass
