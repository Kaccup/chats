import telebot
from telebot import types
bot = telebot.TeleBot('qwer')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_today = types.KeyboardButton('Рассказ')
    btn_tomorrow = types.KeyboardButton('Анекдот')
    btn_joke = types.KeyboardButton('Шутка')
    btn_badjoke = types.KeyboardButton('Черный юмор')
    keyboard_markup.add(btn_today, btn_tomorrow, btn_joke, btn_badjoke)
    bot.send_message(message.chat.id, 'Выбери:', reply_markup=keyboard_markup)

def inline(message):
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Рассказы",
    callback_data="Рассказы")
    but_2 = types.InlineKeyboardButton(text="Анекдоты",
    callback_data="Анекдоты")
    but_3 = types.InlineKeyboardButton(text="Шутки",
    callback_data="Шутки")
    but_4 = types.InlineKeyboardButton(text="Чёрный юмор",
    callback_data="Чёрный юмор")
    key.add(but_1, but_2, but_3, but_4)
    bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=key)


@bot.callback_query_handler(func=lambda c:True)
def inlin(c):
    if c.data == 'Рассказы':
        bot.send_message(c.message.chat.id, 'Вы выбрали - Рассказы')
        bot.send_message(c.message.chat.id, f'Темы: Новый год, Космос детям, Рыбалка, Любовь')
    if c.data == 'Анекдоты':
        bot.send_message(c.message.chat.id, 'Вы выбрали - Анекдоты')
        bot.send_message(c.message.chat.id, f'Темы: Новый Год, Винни-Пух, Чукча, Про собак')
    if c.data == 'Шутки':
        bot.send_message(c.message.chat.id, 'Вы выбрали - Шутки')
        bot.send_message(c.message.chat.id, f'Темы: Тем, кому за 30')
    if c.data == 'Чёрный юмор':
        bot.send_message(c.message.chat.id, 'Вы выбрали - Чёрный юмор')
        bot.send_message(c.message.chat.id, f'Темы: Тюремный юмор, Про Вовочку')
    if __name__ == "__main__":
        bot.send_message(c.message.chat.id, f'')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я расскажу Анекдот. напиши - /Список")
    elif message.text == "Нормально":
        bot.reply_to(message, f'Я Бот,  {message.from_user.first_name}!')
        bot.send_message(message.from_user.id, "Приятно познакомиться.")
    elif message.text == "пошел вон":
        bot.send_message(message.from_user.id, "Сам пошел вон! 😂")
    elif message.text == "Винни-Пух":
        bot.send_message(message.from_user.id, "Винни Пух с утра подходит к зеркалу и думает:"
                                               " - Здесь я, и там тоже я! В это время раздаётся стук в дверь. "
                                               "Винни спрашивает: - Кто там? - Я! - Круто! Даже там я! 😂")
    elif message.text == "Космос детям":
        bot.send_message(message.from_user.id, "Небо над головой!"
                                               "Выйдем с ребенком вечером на балкон или во двор и "
                                               "посмотрим на небо.Сколько на небе звезд? Тех, что можно увидеть "
                                               "невооруженным взглядом, без телескопа и бинокля, 6000."
                                               " По 3000 на каждое полушарие неба.Чтобы можно было легко найти звезду"
                                               " на небе, небо разделено на 88 участков. Мы их называем созвездиями. "
                                               "Самая яркая звезда созвездия отмечается латинской буквой α . "
                                               "Чем бледнее звезда тем дальше «ее буква» от начала алфавита "
                                               "(есть исключения, так не всегда бывает, но об этом в другой раз)."
                                               "Кроме звезд на небе невооруженным взглядом можно увидеть и планеты."
                                               "В древности, люди отмечали только одно различие между звездами и "
                                               "планетами. Обычные звезды не двигались. А планеты «блуждали» по небу."
                                               " Планета так и переводится - «блуждающая». К планетам мы еще вернемся."
                                               " 👩‍🚀")
        bot.send_message(message.from_user.id, "Население солнечной системы.Мы живем на планете, которая называется "
                                               "Земля. Она не одинока среди звезд. У нее есть своя «семья». Эта «семья»"
                                               " называется солнечная система.Мы все еще смотрим на небо.Солнце -"
                                               " самый большой и массивный объект солнечной системы (98% массы всех"
                                               " тел в "
                                               "солнечной системе - это конечно для детей постарше). Его мы видим"
                                               " каждый день на небе. Солнце звезда, но в отличие от других звезд она"
                                               " находится близко к нам.Луна - самое близкое к нам небесное тело. Чаще"
                                               " мы обращаем на нее внимание ночью. Луна гораздо меньше Солнца, но на"
                                               " небе они выглядят одинаково по размеру. Просто Луна ближе к нам. "
                                               "Совпадение видимых размеров - просто (космическая) случайность.В "
                                               "солнечной системе 8 планет. Меркурий, Венера, Земля, Марс, Юпитер, "
                                               "Сатурн, Уран и Нептун.")
    elif message.text == "Чукча":
        bot.send_message(message.from_user.id, "Чукча приводит сына к врачу:"
                                               " - Доктор, сын не ест ничего: ни колбасы, ни масла, ни яблок."
                                               " - Почему же он не ест? - Нету, однако.")
        bot.send_message(message.from_user.id, "Утро в кондитерской лавке, идёт приём заказов:"
                                               " - Мне тортик в виде книги, дочь поступила в педагогический. "
                                               "- А мне тортик в виде шестерёнки, сын будет учиться на конструктора. "
                                               "- А вам, мужчина, какой тортик?"
                                               " - Так, а что вы посоветуете, мой гинекологом будет? 😂")
    elif message.text == "Новый год":
        bot.send_message(message.from_user.id, "В детстве думал: - Ура, скоро Новый год! Сейчас думаю: "
                                               "- Твою мать, скоро опять Новый год...😂 ")
        bot.send_message(message.from_user.id, "- Как ты встретил Новый год? - Как подарок. "
                                               "- В смысле? - Всю ночь под ёлкой валялся! 😂")
        bot.send_message(message.from_user.id, "Хочу на Новый год: пачку нервов, упаковку терпения, "
                                               "хронического здоровья, неизлечимого счастья"
                                               " и вечно беременного кошелька! 😂")
        bot.send_message(message.from_user.id, "На Новый год тёща подарила мне два билета в театр."
                                               " Жена приболела, дети уехали на горных лыжах кататься..."
                                               " Вот я и думаю, в чем подвох? 😂")
    elif message.text == "Про собак":
        bot.send_message(message.from_user.id, "Семья пришла в ресторан. Поели, отец расплачивается, "
                                               "а мать говорит официанту:"
                                               " - Вы не против, если мы соберём со стола остатки и "
                                               "отнесём их домой собаке? Официант:"
                                               " - Да, конечно, пожалуйста! Дети, радостно, хором: -"
                                               " Ура! Нам купят собаку!😂")
        bot.send_message(message.from_user.id, "Две собаки разговаривают: - Шарик, как ты думаешь, а "
                                               "от голода таблетки есть?"
                                               " - Да, есть, котлеты называются!😂")
        bot.send_message(message.from_user.id, "К компании крутых, отдыхающих на природе, подходит мужичок и говорит:"
                                               " - Ребята, это не ваш бультерьер тут бегал? - Ну, наш, а тебе то что?"
                                               " - Я, конечно, дико извиняюсь, мы тут тоже рядом отдыхаем, "
                                               "и моя собачка случайно убила вашу! - Да ты что? А что у тебя за зверь?"
                                               " - Да маленький такой пуделёк! - Да как же это? - А ваш им подавился..."
                                               "😂 ")

    else:
        bot.send_message(message.from_user.id, "Учитывай правильный регистр.   /Список")


bot.polling(none_stop=True)
