import json
import re
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN, GIT_TOKEN

BOT_TOKEN = TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

YOUR_TOKEN = GIT_TOKEN
OWNER = "DarPru"

USERS = {
    'dar_pru': 'DarPru',
    'Kirusha_molodec': 'Kirusha-Molodec',
    'senchukk': 'senchukk',
    'maxabuts': 'maxarez',
    'nnastian': 'nastiiaan',
    'LezhatPleace': 'CyberAmmo',
    'TaranYevgen': 'TaranYevgen',
    'antimenchik': 'Antimen-Web',
    'tselikovaa': 'tselikova007',
    'callmeyungpluxury': 'yungpluxury',
    'grankin_n': 'Nebarik07',
    'sashenka_kh': 'Ripka7',
    'Vikaseo123': 'vikaseo123',
    'Morgenn': 'angry-red-panda'


}
@dp.message_handler(lambda message: '@allow_my_id_to_github_bot' in message.text)
async def process_start_command(message: types.Message):
    name = message.from_user.username
    if name in USERS:
        USERNAME = USERS[name]
        URLS = list(filter(None, re.split('\n|,| |и', message.text[26:])))
        for url in URLS:
            REPO = url
            ORG = "1sites"
            portals = ["datacolor.com.ua", "artistwizard.co.uk", "stayathome.co.in", "fun88cado.com", "drbet.org.uk",
                       "1vin.com.ua", "1vin.co.ua", "tuev-nord.com.ua", "1vin.org.ua", "vupysknoj.com.ua",
                       "goto1xbet.website", "headlines.com.ua", "1vin.net.ua", "1vin.kiev.ua", "tiger-casino.net"]
            for i in portals:
                if REPO == i:
                    ORG = "1portals"
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
                await message.reply(f'Успех! Пользователь {USERNAME} был успешно добавлен в репозиторий {REPO}')
            else:
                await message.reply(f'Что-то пошло не так! @darpru нужна помощь!')

    else:
        await message.reply(f"Тебя нет в моей базе, @dar_pru это нужно поправить")



@dp.message_handler()
async def defaultHander(message : types.Message):
    await message.answer(f"Извините, это не команда")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
