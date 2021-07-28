import telebot
import os

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

API_KEY = ''
API_SECRET = ''
BOT_KEY = ''
GROUP_KEY = ''

if os.environ.get('API_KEY', '') != '':
	API_KEY = os.environ['API_KEY']
if os.environ.get('API_SECRET', '') != '':
	API_SECRET = os.environ['API_SECRET']
if os.environ.get('BOT_KEY', '') != '':
	BOT_KEY = os.environ['BOT_KEY']
if os.environ.get('GROUP_KEY', '') != '':
	GROUP_KEY = os.environ['GROUP_KEY']

api_key = API_KEY
api_secret = API_SECRET
bot = telebot.TeleBot(BOT_KEY)
client = Client(api_key, api_secret)

txt_price = ""
prices = client.get_all_tickers()
for i in prices:
	moeda = i['symbol'][-3:]
	if(moeda=="BRL"):
		cripto = i['symbol'][:3]
		criptoName = ""
		if(cripto=="BTC"):
			criptoName = "Bitcoin"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
		if(cripto=="ETH"):
			criptoName = "Ethereum"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
		if(cripto=="ADA"):
			criptoName = "Cardano"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
bot.send_message(GROUP_KEY, txt_price)

#bot.polling()
