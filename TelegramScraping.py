#https://medium.com/game-of-data/telegram-channel-data-extraction-users-information-chats-and-specific-messages-and-data-21bb54710fd3
#https://docs.telethon.dev/en/stable/basic/quick-start.html

from telethon import TelegramClient
from telethon import events
import pandas as pd
import os

api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
group_username = "https://t.me/URDU_PRESSA"

client = TelegramClient('session', api_id, api_hash).start()

async def Me():
    user=[]
    me=await client.get_me()
    user.append({'first name':me.first_name})
    user.append({'last name':me.last_name})
    user.append({'username':me.username})
    user.append({'user id':me.id})
    return user

async def Participants(group_or_chat_link):
    participants = await client.get_participants(group_or_chat_link)
    firstname = []
    lastname = []
    username = []
    if len(participants):
        for x in participants:
            firstname.append(x.first_name)
            lastname.append(x.last_name)
            username.append(x.username)

    data = {'first_name': firstname, 'last_name': lastname, 'user_name': username}
    #print(data)
    userdetails = pd.DataFrame(data)
    return userdetails

async def GetMessage(group_or_chat_link, messege_count,file_name):
    chats = await client.get_messages(group_or_chat_link, messege_count)
    message_id = []
    message = []
    sender = []
    reply_to = []
    time = []
    with open(file_name,'w',encoding='utf8') as file:
        if len(chats):
            for chat in chats:
                message_id.append(chat.id)
                message.append(chat.message)
                # msg = msg + chat.message
                sender.append(chat.from_id)
                reply_to.append(chat.reply_to_msg_id)
                time.append(chat.date)

                file.write("\nid:"+str(chat.id)+"\tdate:"+str(chat.date)+"\tkimdan:"+str(chat.from_id)+"\treply:"+str(chat.reply_to_msg_id)+"\tmsg:"+str(chat.message))
        data = {'message_id': message_id, 'message': message, 'sender_ID': sender, 'reply_to_msg_id': reply_to,
                'time': time}
        df = pd.DataFrame(data)
        return df

async def SentMessage(number,message):
    await client.send_message(number,message)

@client.on(events.NewMessage)
async def AutoSentMessage(event):
    if 'hello' in event.raw_text:
        await event.reply('hi')


with client:
    #print(client.loop.run_until_complete(Me()))
    #print(client.loop.run_until_complete(Participants(group_username)))
    #data=client.loop.run_until_complete(GetMessage(group_username,10000000,'msg.txt'))
    #print(data)
    #client.loop.run_until_complete(SentMessage('+998999669001','dsfdsf'))
    client.start()
    client.run_until_disconnected()