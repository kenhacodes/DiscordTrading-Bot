import discord
import os
import alpaca_trade_api as tradeapi
import requests
import json

client = discord.Client()

#Alpaca API conexion

API_KEY = os.getenv('paperAlpacaKey')
SECRET_KEY = os.getenv('paperAlpacaKeySecret')
APCA_API_KEY_ID = API_KEY
APCA_API_SECRET_KEY = SECRET_KEY 
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)

testr = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})

print(testr.content)

#Conexion a discord 
@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#Comando de prueba de mensaje
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('%hello'):
    await message.channel.send('NiceNice')



client.run(os.getenv('token'))
