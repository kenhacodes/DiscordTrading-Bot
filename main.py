import discord
import os
import alpaca_trade_api as tradeapi
import requests
import json
from commands import *
import pymongo
import flask

#Conexion a API Alpaca

API_KEY = os.getenv('paperAlpacaKey')
SECRET_KEY = os.getenv('paperAlpacaKeySecret')

#URL's API
BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
PORTFOLIO_URL = '{}/v2/account/portfolio/history'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY}

#Conexion MongoDB

mongodbPassword = os.getenv('mongodbPassword')
# Defines a new client.
client = pymongo.MongoClient(
    "mongodb+srv://kenha:{}@cluster0.46tv4.mongodb.net/DogeTradeBot?retryWrites=true&w=majority"
    .format(mongodbPassword))

# Get the database (database name by default is "test")
db = client.db_name  # OR db = client.test
print(db)

#Conexion a discord
client = discord.Client()

@client.event
async def on_ready():
    print('Woof! {0.user} is on!'.format(client))

#Funciones prueba API Alpaca

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        'symbol': symbol,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

#Devuelve el estado de la cuenta de Alpaca
def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

status = get_account().get('status')
print(status)

#Devuelve las ordenes
def get_orders():
    r = requests.get(ORDERS_URL, headers=HEADERS)
    return json.loads(r.content)

orders = get_orders()

#Imprime las ordenes pendientes
def print_orders():
    print('Pendent orders: ')
    for order in orders:
        r = orders[0].get('symbol') + ' ' + orders[0].get(
            'qty') + ' ' + orders[0].get('side')
        print(r)
        print('..........')


print_orders()

#Admin Permissions
adminid = '377180298066001921'
not_admin = 'You are not an admin'


#Comando de prueba de mensaje
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    if message.author.bot == True:
        return

    #Variables generales para funciones
    name = message.author
    idUser = message.author.id

    #Print los datos del usuario que escribio
    print(get_User(name, idUser))

    if message.content.startswith('%buy'):
        response = create_order('AAPL', 5, 'buy', 'market', 'gtc')
        r = "Stock: {}, Side: {}, Quantity: {}, Time in force: {}, Status: {}".format(
            response["symbol"], response["side"], response["qty"],
            response["time_in_force"], response["status"])
        print(r)
        print("...")
        await message.channel.send(r)

    if message.content.startswith('%sell'):
        response = create_order('AAPL', 1, 'sell', 'market', 'gtc')
        r = "Stock: {}, Side: {}, Quantity: {}, Time in force: {}, Status: {}".format(
            response["symbol"], response["side"], response["qty"],
            response["time_in_force"], response["status"])
        print(r)
        print("...")
        await message.channel.send(r)

    #if message.content.startswith('%'):
    #    comando = commands(message.content)[1:len(message.content)]
    #    await message.channel.send(comando)

    if message.content.startswith('%print_orders'):
        if str(message.author.id) == adminid:
            #Print las ordenes pendientes
            print_orders()
            print('Done!')

            #Respuesta del bot
            await message.channel.send('Done! Woof!')
        else:
            await message.channel.send(not_admin)
            print('{} tried to do an admin command!'.format(message.author))

client.run(os.getenv('token'))