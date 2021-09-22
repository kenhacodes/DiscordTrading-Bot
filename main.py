import discord
import os
import alpaca_trade_api as tradeapi
import requests
import json
from commands import *

#Conexion a API Alpaca

API_KEY = os.getenv('paperAlpacaKey')
SECRET_KEY = os.getenv('paperAlpacaKeySecret')
#URL's API
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
PORTFOLIO_URL = '{}/v2/account/portfolio/history'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID':API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}


#Conexion a discord
client = discord.Client()
@client.event 
async def on_ready():
  print('Woof! {0.user} is on!'.format(client))

#Funciones prueba API Alpaca
def get_account():
  r = requests.get(ACCOUNT_URL, headers=HEADERS)
  return json.loads(r.content)

status=get_account().get('status')
print (status)

def create_order(symbol, qty, side, type, time_in_force):
  data = {
    'symbol': symbol,
    'qty': qty,
    'side': side,
    'type': type,
    'time_in_force':time_in_force
  }
  r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
  return json.loads(r.content)

def get_orders():
  r = requests.get(ORDERS_URL, headers=HEADERS)
  return json.loads(r.content)

orders = get_orders()

def print_orders():
  print('Pendent orders: ')
  for order in orders:
    r = orders[0].get('symbol')    
    print(r)
    r = orders[0].get('qty')
    print(r)
    r= orders[0].get('side')
    print(r)
    print('..........')
print_orders()

#Admin Permissions
admin = 'KenHa#5259'
not_admin = 'You are not an admin'

#Comando de prueba de mensaje
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('%hello'):
    response = create_order('AAPL', 100, 'buy', 'market', 'gtc')
    print (response)
    await message.channel.send(response)
  if message.content.startswith('%print_orders'):
    if str(message.author) == admin:
      print_orders()
      print('Done!')
      await message.channel.send('Done! Woof!')
    else:
      await message.channel.send(not_admin)
      print('{} tried to do a admin command!'.format(message.author))

client.run(os.getenv('token'))

kyubi = 'ewdyewdcucu3c3rucu3rcvu3rlcvir3locirvieuvceuvcl ewruvclierulvicuelverlvulurlver.2jvjerl.ovi2eoi oje2jkc32ilcuv2lvolvrvjcr42ocilocil2vcer,corivoijecfk je uerivpie4ec jekf efezrwuiele je e fe ej l€j lej lefl oviwkchewkcerwcjcczxwexhe3c,kxewrclr3cjr3lcjxbwe   cnccr3crk3elcker3kic.'

