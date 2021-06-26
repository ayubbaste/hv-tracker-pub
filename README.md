## Career.habr.com new vacancies tracker 
Welcome to the HV-Tracker-Pub wiki!

>It parses new vacancies from https://career.habr.com/ and sends them to your Telegram.

<b>Before you start</b>

- Get Telegram API_ID and API_HASH here: https://my.telegram.org/

- Create telegram bot with BotFather and get Bot Token.

- Use your telegram Bot Token to see all CHAT_IDs and chose that one, where to send new vacancies:

- ```https://api.telegram.org/bot1855xxx:AAE2l9cGEIYzxxxxxxxxxxxxxxxxxxxxx/getUpdates```

<b>Installation</b>

- Install all requirements

```
pip install -r requirements.txt
```

<b>Usage</b>

- Set your variables:

```
session_name = "any_name_you_want" # Str. Example: 'tracker_bot'
api_id = your API_ID # Digits. Example: 1112223
api_hash = "your API_HASH" # Str. Example: 'xx11111xxxx111x1111111x1x1xx11x1'
bot_token = "your BOT_TOKEN" # Str. Example: '1111111111:XXX111xXXXXxxExXx1xXXXXXx1xx1x_XxxX'
recipients = [CHAT_IDs] # Digits. Example: [-1112223334445, -2223334445556]
parse_url= "career.habr url with vacancies" # Str. Example: 'https://career.habr.com/vacancies?divisions[]=backend&divisions[]=administration&qid=3&type=all'
```

- Launch the script
```
python tracker.py
```

Automate the launch of the script with Cron or any other way. Vacanies HV-tracker-pub from career.habr.com
