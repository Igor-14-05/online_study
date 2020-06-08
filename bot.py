import telebot
import const
import random
import emodji
import directories
import time
import datetime
from cmath import *

bot = telebot.TeleBot(const.token)

@bot.message_handler(commands=['start'])
def handle_text(message):
    gif_hi = open(const.hi_sticker_place + '/' + "hi.tgs",'rb')
    bot.send_animation(message.from_user.id,gif_hi)
    gif_hi.close()
    time.sleep(1)
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row("Учеба" + emodji.em23)
    user_markup.row("О Боте","Связь с нами")
    user_markup.row("Оставить комментарий")
    bot.send_message(message.from_user.id, "Добро Пожаловать, " + message.from_user.first_name,reply_markup = user_markup)
    time.sleep(1)
    bot.send_message(message.from_user.id,"Меня зовут Online_Study_Bot, рад знакомству.")
    const.kol_chelovek += 1
    const.chel.append(message.from_user.id)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    try:
        if message.text == "Оставить комментарий":
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Форма', url='https://docs.google.com/forms/d/1-JMLI1MtHTVKWxOwzyYnEg5bocmkxzA1vpd_mRBCYk0/prefill')
            markup.add(btn_my_site)
            bot.send_message(message.chat.id, "Заполните форму", reply_markup = markup)
            bot.send_message(message.from_user.id,"Займет буквально пять минут")
            bot.send_message(message.from_user.id,"Заранeе спасибо")

        elif message.text == 'О Боте':
            user = telebot.types.ReplyKeyboardMarkup(True,False)
            user.row("Для чего этот Бот?","Как работать с Ботом?")
            user.row("Сколько человек используют бот?" + emodji.em2)
            user.row("Что, если я хочу дать вам дополнительные материалы?")
            user.row("Назад")
            bot.send_message(message.from_user.id,"Что именно вы хотите узнать о нас?",reply_markup=user)

        elif message.text == "Сколько человек используют бот?" + emodji.em2:
            bot.send_message(message.from_user.id,"Нас " + str(const.kol_chelovek))

        elif message.text == 'Связь с нами':
            user_markup1 = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup1.row("Почта" + emodji.em4)
            user_markup1.row("Юзер телеграмма" + emodji.em24)
            user_markup1.row("Назад")
            bot.send_message(message.from_user.id,"Надеюсь, не будете беспокоить моего основателя просто так",reply_markup=user_markup1)

        elif message.text == "Юзер телеграмма" + emodji.em24:
            bot.send_message(message.from_user.id,"@wolf1405")

        elif message.text == 'Назад':
            user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup.row("Учеба" + emodji.em23)
            user_markup.row("О Боте","Связь с нами")
            user_markup.row("Оставить комментарий")
            bot.send_message(message.from_user.id,"Ок",reply_markup=user_markup)

        elif message.text == "Почта" + emodji.em4:
            bot.send_message(message.from_user.id,"onlinestudybot@gmail.com")

        elif message.text == "Учеба" + emodji.em23:
            user_markup2 = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup2.row("Вступительные тесты в институты")
            user_markup2.row("Тесты и задания" + emodji.em23,"Калькулятор")
            user_markup2.row("Полезные ссылки на YouTube" , "Платформы для самообразования")
            user_markup2.row("Назад")
            bot.send_message(message.from_user.id, "Рад, что ты хочешь учиться", reply_markup = user_markup2)

        elif message.text == "Калькулятор":
            bot.send_message(message.from_user.id,"Пишите пример, но в начале напишите символ @")

        elif message.text[0] == "@":
            vopr = message.text[1:]
            otvet = str(eval(vopr))
            bot.send_message(message.from_user.id,vopr + "=" + otvet)

        elif message.text == "Платформы для самообразования":
            platforms = telebot.types.ReplyKeyboardMarkup(True,False)
            platforms.row("Stepik")
            platforms.row("EDX","Coursera")
            platforms.row("TED","SoloLearn","Lingualeo")
            platforms.row(emodji.em8 + "Назад")
            bot.send_message(message.from_user.id,"Выберите нужную вам платформу. Появится описание и ссылки на их сайт и ссылки на скачивание для IOS и Android",reply_markup=platforms)

        elif message.text == "Stepik":
            stepic = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=org.stepic.droid")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/stepik-best-online-courses/id1064581926")
            site = telebot.types.InlineKeyboardButton(text="Сайт",url="https://welcome.stepik.org/ru")
            stepic.add(ios,android)
            stepic.add(site)
            bot.send_message(message.from_user.id,"Вот",reply_markup=stepic)

        elif message.text == "EDX":
            EDX = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=org.edx.mobile")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/edx-courses-by-harvard-mit/id945480667")
            site = telebot.types.InlineKeyboardButton(text="Сайт",url="https://www.edx.org/")
            EDX.add(ios,android)
            EDX.add(site)
            bot.send_message(message.from_user.id,"Вот",reply_markup=EDX)

        elif message.text == "Coursera":
            Coursera = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=org.coursera.android")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/coursera-learn-new-skills/id736535961")
            site = telebot.types.InlineKeyboardButton(text="Сайт",url="https://www.coursera.org/")
            Coursera.add(ios,android)
            Coursera.add(site)
            bot.send_message(message.from_user.id,"Вот",reply_markup=Coursera)

        elif message.text == "TED":
            TED = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=com.ted.android")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/ted/id376183339")
            site = telebot.types.InlineKeyboardButton(text="Сайт",url="https://www.ted.com/")
            TED.add(ios,android)
            TED.add(site)
            bot.send_message(message.from_user.id,"Вот",reply_markup=TED)

        elif message.text == "SoloLearn":
            SoloLearn = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=com.sololearn")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/sololearn-learn-to-code/id1210079064")
            site = telebot.types.InlineKeyboardButton(text="Сайт",url="https://www.sololearn.com/")
            SoloLearn.add(ios,android)
            SoloLearn.add(site)
            bot.send_message(message.from_user.id,"Вот",reply_markup=SoloLearn)

        elif message.text == "Lingualeo":
            Lingualeo = telebot.types.InlineKeyboardMarkup()
            ios = telebot.types.InlineKeyboardButton(text="Для Android",url="https://play.google.com/store/apps/details?id=com.lingualeo.android")
            android = telebot.types.InlineKeyboardButton(text="Для IOS",url="https://apps.apple.com/uz/app/english-with-lingualeo/id480952151")
            Lingualeo.add(ios,android)
            bot.send_message(message.from_user.id,"Вот",reply_markup=Lingualeo)

        elif message.text == "Тесты и задания" + emodji.em23:
            markup = telebot.types.ReplyKeyboardMarkup(True,False)
            markup.row("Биология" + emodji.em22, "Химия")
            markup.row("Математика полегче", "Математика посложнее")
            markup.row("Информатика" + emodji.em24, "Задачи на программирование")
            markup.row(emodji.em8 + "Назад")
            bot.send_message(message.from_user.id,"Выбери нужный предмет",reply_markup = markup)

        elif message.text == "Биология" + emodji.em22:
            markup = telebot.types.InlineKeyboardMarkup()
            file = random.choice(directories.biologiya)
            btn = telebot.types.InlineKeyboardButton(text="Тест",url=file)
            markup.add(btn)
            bot.send_message(message.from_user.id,"Надеюсь, понравится",reply_markup=markup)

        elif message.text == 'Полезные ссылки на YouTube':
            bot.send_message(message.from_user.id, """\r
             <b>Замечательный канал</b>
             <a href="URL">https://youtu.be/oBWMgI2PWa8</a>""", parse_mode="HTML")

        elif message.text == emodji.em8 + "Назад":
            user_markup2 = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup2.row("Вступительные тесты в институты")
            user_markup2.row("Тесты и задания" + emodji.em23,"Калькулятор")
            user_markup2.row("Полезные ссылки на YouTube" , "Платформы для самообразования")
            user_markup2.row("Назад")
            bot.send_message(message.from_user.id, "Рад, что ты хочешь учиться", reply_markup = user_markup2)

        elif message.text == "Вступительные тесты в институты":
            user_markup3 = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup3.row("МГУ(Узбекистан)","Губкина(Узбекистан)")
            user_markup3.row("Плеханово(Узбекистан)")
            user_markup3.row(emodji.em8 + "Назад")
            bot.send_message(message.from_user.id, "Хороший выбор", reply_markup = user_markup3)

        elif message.text == "Губкина(Узбекистан)":
            file = random.choice(directories.gubkino)
            markup = telebot.types.InlineKeyboardMarkup()
            btn_my_site = telebot.types.InlineKeyboardButton(text='Задание', url=file)
            markup.add(btn_my_site)
            bot.send_message(message.from_user.id,"Ваш, выбранный предмет",reply_markup=markup)

        elif message.text == 'МГУ(Узбекистан)':
            user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup.row("Математика","Информатика")
            user_markup.row("Русский" + emodji.em10,"Биология")
            user_markup.row("Вернуться")
            bot.send_message(message.from_user.id,"Выбери,пожалуста предмет",reply_markup=user_markup)

        elif message.text ==  "Вернуться":
            user_markup3 = telebot.types.ReplyKeyboardMarkup(True,False)
            user_markup3.row("МГУ","Губкина")
            user_markup3.row(emodji.em8 + "Назад")
            bot.send_message(message.from_user.id, "Хороший выбор", reply_markup = user_markup3)

        elif message.text == "Математика":
            math_file = random.choice(directories.math)
            math_markup = telebot.types.InlineKeyboardMarkup()
            math = telebot.types.InlineKeyboardButton(text="Задние",url=math_file)
            math_markup.add(math)
            bot.send_message(message.from_user.id,"Удачи в поступлении",reply_markup=math_markup)

        elif message.text == "Информатика":
            inf_file = random.choice(directories.inf)
            inf_markup = telebot.types.InlineKeyboardMarkup()
            inf = telebot.types.InlineKeyboardButton(text="Задние",url=inf_file)
            inf_markup.add(inf)
            bot.send_message(message.from_user.id,"Удачи в поступлении",reply_markup=inf_markup)

        elif message.text == "Русский" + emodji.em10:
            rus_file = random.choice(directories.rus)
            rus_markup = telebot.types.InlineKeyboardMarkup()
            rus = telebot.types.InlineKeyboardButton(text="Задние",url=rus_file)
            rus_markup.add(rus)
            bot.send_message(message.from_user.id,"Удачи в поступлении",reply_markup=rus_markup)

        elif message.text == "Биология":
            bio_file = random.choice(directories.bio)
            bio_markup = telebot.types.InlineKeyboardMarkup()
            bio = telebot.types.InlineKeyboardButton(text="Задние",url=bio_file)
            bio_markup.add(bio)
            bot.send_message(message.from_user.id,"Удачи в поступлении",reply_markup=bio_markup)
    except:
        bot.send_message(message.from_user.id,"Пожалуйста, попробуйте еще раз, небольшая ошибка")
        bot.send_message(message.from_user.id,"Если она так и будет появляться, то свяжитесь свяжитесь с моим основателем, нажав на кнопку \"Связь с нами\" или набрав эту фразу на клавиатуре  ")

bot.polling(none_stop=False, interval=0)

"""
  directory = 'C:/tt/photo'
        all_files = os.listdir(directory)
        print(all_files)
        for file in all_files:
            img = open(directory + '/' + file, 'rb')
            bot.send_photo(message.from_user.id, img)
            img.close()
"""