from pyrogram import Client

#----------------------------------

#api_id и api_hash аккаунта можно получить на my.telegram.org

api_id = 15410703 #только цифры

api_hash = "84e9bd34b07f616ed36f0386dcdf3f68" #должен быть в скобках

take_from = ["Cryptography_2020"] #откуда хотите брать посты? (юзернейм (в кавычках, без @) или айди канала (без кавычек) ); через запятую

send_to = ["cryptoestatenews"] #айди канала (без кавычек) или юзернейм (в кавычках, без @), куда хотите пересылать посты; через запятую

client = Client("getpost", api_id, api_hash) #если хотите сменить аккаунт, смените getpost на любое другое слово или просто удалите .session файл в папке со скриптом

#----------------------------------
client.start()

@client.on_message()
def handle_messages(app, m):
    try:
        if m.chat.username in take_from or m.chat.id in take_from:
            for channel in send_to:
                m.forward(channel, as_copy=True)
    except Exception as e:
        print(e)