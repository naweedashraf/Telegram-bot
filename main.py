import telepot, time, os
from feed import getFeed

# telegram bot
token = ''
lastUpdateId = ''

with open('token.txt', 'r') as file:
    token = file.readline()

while True:
    if 'updateId.txt' in os.listdir('./'):
        with open('updateId.txt', 'r') as file:
            lastUpdateId = file.readline()
    else:
        lastUpdateId = '0'

    TelegramBot = telepot.Bot(token)
    contents = TelegramBot.getUpdates(lastUpdateId)
    if len(contents)>0:
        for content in contents:
            msg = content['message']['text']
            id = content['message']['from']['id']
            if msg == '/help':
                TelegramBot.sendMessage(id, "enter \n/sport to get sport news \n/economy to get economic news \n/technology to get economic news")
            elif msg == '/technology':
                TelegramBot.sendMessage(id, getFeed('Technology'), parse_mode='Markdown')
            elif msg == '/sport':
                TelegramBot.sendMessage(id, getFeed('Sports'), parse_mode='Markdown')
            elif msg == '/economy':
                TelegramBot.sendMessage(id, getFeed('Economy'), parse_mode='Markdown')
            else:
                TelegramBot.sendMessage(id, "Incorrect message.\n enter \n/sport to get sport news \n/economy to get economic news \n/technology to get economic news")
    with open('updateId.txt','w') as file:
        if len(contents) > 0 :
            file.write(str(contents[-1]['update_id']+1))
        else:
            file.write(lastUpdateId)
    
    time.sleep(2)