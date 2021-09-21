import discord
import os
import alpaca_trade_api as tradeapi
import requests
import json


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
print('Pendent orders: ')
print(orders)

#Comando de prueba de mensaje
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('%hello'):
    response = create_order('AAPL', 100, 'buy', 'market', 'gtc')
    print (response)
    await message.channel.send(response)

client.run(os.getenv('token'))
