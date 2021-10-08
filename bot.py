import telebot
import os
import json

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

#ATENÇÃO: NÃO DECLARAR ESTAS VARIAVEIS PUBLICAMENTE! USAR SECRETS

#API KEY da Binance (Gerado dentro do site da mesma)
API_KEY = ''
#API SECRET da Binance (Gerado dentro do site da mesma)
API_SECRET = ''
#KEY do BOT (obitida com o botfather no Telegram)
BOT_KEY = ''
#KEY do grupo onde a mensagem será enviada (obitida em https://api.telegram.org/bot<BOT_KEY>/getUpdates)
GROUP_KEY = ''

#Coletando Variaveis do Ambiente (Criadas em Settings>Secrets)
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

txt_price = "Cotação Crypto Binance:\n\n"

#Pegando todas as cotações e selecionando apenas as necessárias e enviando ao grupo
prices = client.get_all_tickers()
for i in prices:
	moeda = i['symbol'][-3:]
	if(moeda=="BRL"):
		cripto = i['symbol'][:3]
		criptoName = ""
		if(cripto=="BTC"):
			criptoName = "Bitcoin"
			criptoInfo = client.get_ticker(symbol=i['symbol'])
			json_str = json.dumps(criptoInfo)
			criptoInfo = json.loads(json_str)
			txt_price += ('%.2f' % round(float(criptoInfo['criptoInfo']),2)) +" "+ cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
		if(cripto=="ETH"):
			criptoName = "Ethereum"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
		if(cripto=="ADA"):
			criptoName = "Cardano"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
		if(cripto=="XRP"):
			criptoName = "Ripple"
			txt_price += cripto + " (" +criptoName+ ")" +" = R$ "+ ('%.2f' % round(float(i['price']),2)) + "\n"
groups_list = GROUP_KEY.split('#')
for i in range(len(groups_list)):
	bot.send_message(groups_list[i], txt_price)
#bot.polling()
