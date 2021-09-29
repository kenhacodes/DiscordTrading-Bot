import discord
import os
import alpaca_trade_api as tradeapi
import requests
import json

#Discord API
DISCORD_URL = 'https://discord.com/api/v8'
USER_ID_URL = '/users/{user.id}'


def get_User():
    #Comprueba si el usuario esta en la base de datos
    #Devuelve los datos del usuario en forma de lista
    #Lo de abajo es un placeholder hasta que la base de datos este terminada
    name = message.author
    idUser = message.author.id
    dinero = 1000
    pendent_orders = []
    historial = []

    user_data = [name, idUser, dinero, pendent_orders, historial]
    return user_data


#List of commands/actions

#Main yellow color app
#dba72e


#Test embedded message ^^
def test_embed():
    return 0


#Start
#The user is put in the mongodb database. If he already is send message telling him so


def start():
    return 0


#List of stocks
#Shows the user a list of all the available stocks
#Tells him if the market is open and when it opens

#List of pendents
#Shows him a list of pendants buys and sells

#WatchList
#Shows him the list of his watchlist

#Profile
#See his money/investments
#Win Ratio
#Status
