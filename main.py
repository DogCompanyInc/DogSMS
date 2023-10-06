import config
from twilio.rest import Client

text = 'hello from DogSMS!'
number = config.number
receiver = '+011549728246652(fake)'
banner = '''

  _____               _____ __  __  _____ 
 |  __ \             / ____|  \/  |/ ____|
 | |  | | ___   __ _| (___ | \  / | (___  
 | |  | |/ _ \ / _` |\___ \| |\/| |\___ \ 
 | |__| | (_) | (_| |____) | |  | |____) |
 |_____/ \___/ \__, |_____/|_|  |_|_____/ 
                __/ |                     
               |___/                      
        made by DogCompanyInc
	you can send SMS and use as module :)
'''

def sending_sms(text, receiver):
	try:
		account_sid = config.account_sid
		auth_token = config.auth_token

		client = Client(account_sid, auth_token)

		message = client.messages.create(
			body=text,
			from_=number,
			to=receiver
			)

		return 'Оправка успешная!'
	except Exception as ex:
		return 'Уппс... Ошибка! При отправке сообщения', ex

def main():
	receiver = input('Введите номер получателя: ')
	text = input('Введите текст сообщения: ')
	sending_sms(text=text, receiver=receiver)

if __name__ == '__main__':
	print(banner)
	main()
