import json
import re
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
# from config import TOKEN, GIT_TOKEN


'''
pip install requests
pip install aiogram

'''

BOT_TOKEN = TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

YOUR_TOKEN = GIT_TOKEN
ADMIN = "@" # put admin's tg name
ORG = "" # put your organisation mane here

# put the list of users allowed to be added to repo
USERS = {
    'tg_name': 'github_name'

}
@dp.message_handler(lambda message: '@allow_my_id_to_github_bot' in message.text)
async def process_start_command(message: types.Message):
    name = message.from_user.username
    if name in USERS:
        USERNAME = USERS[name]
        URLS = list(filter(None, re.split('\n|,| |и', message.text[26:])))
        print(URLS)
        for url in URLS:
            REPO = url
            URL = f'https://api.github.com/repos/{ORG}/{REPO}/collaborators/{USERNAME}'
            headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {YOUR_TOKEN}",
                "X-GitHub-Api-Version": "2022-11-28"
            }
            data = {
                "permission": "write"
            }
            r = requests.put(url=URL, data=json.dumps(data), headers=headers)
            if r.status_code == 201 or r.status_code == 204:
                await message.reply(f'Success! User {USERNAME} was added to repo {REPO}')
            else:
                await message.reply(f'Something went wrong! {ADMIN} need your help!')

    else:
        await message.reply(f"You are not in my base, {ADMIN} need your help!")



@dp.message_handler()
async def defaultHander(message : types.Message):
    await message.answer(f"Sorry, it's not a command")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
