import telebot

bot = telebot.TeleBot('6814753197:AAGFpQYrCMDpo1Er25HwFUCoG0wtK-AFa9A')


@bot.message_handler(commands=['home'])
def home1(message):
    bot.send_message(message.chat.id, '[Сайт Лицея](https://sch7kstovo.edusite.ru/p2aa1.html)', parse_mode='Markdown')

@bot.message_handler(commands=['changes'])
def changes1(message):
    bot.send_message(message.chat.id, '[Изменения в расписании](https://sch7kstovo.edusite.ru/p17aa1.html)', parse_mode='Markdown')

@bot.message_handler(commands=['diary'])
def diary1(message):
    bot.send_message(message.chat.id, '[Электронный журнал](https://edu.gounn.ru/?show=home&u=594)', parse_mode='Markdown')

@bot.message_handler(commands=['canteen'])
def canteen1(message):
    bot.send_message(message.chat.id, '[Ежедневное меню в столовой](https://sch7kstovo.edusite.ru/mmagic.html?page=/food/index.html)', parse_mode='Markdown')


bot.infinity_polling()