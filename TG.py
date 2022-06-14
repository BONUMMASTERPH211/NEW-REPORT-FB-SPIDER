import telegram.ext



class Bot:
	def __init__(self, token, update):
		self.token = token
		self.update = update

	def start(self, update, context):
		update.message.reply_text("Hi, code by f34rl3ss")


def main():
	print("> Bot is Running...")
	token = "5531497971:AAFA6yzpCUpcpC_TomxWFTzqmA6FD6AP4Qg"
	
	updater = telegram.ext.Updater(token, use_context=True)
	disp = updater.dispatcher

	TG = Bot(token, updater)
	disp.add_handler(telegram.ext.CommandHandler("start", TG.start))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()
