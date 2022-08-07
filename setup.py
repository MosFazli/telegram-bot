import telebot
import csv
import datetime

bot = telebot.TeleBot("5441208078:AAEBrAHziJy8VZC8R1D7tQOZs9EoAXbwkSs")

tempArray = []
membersClass = []

today = datetime.datetime.today()
day = datetime.datetime.today().weekday()

with open("Saturday.csv", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        tempRow = []
        tempRow.append(row[0])
        tempRow.append(row[1])
        tempRow.append(row[2])
        tempRow.append(row[3])
        tempRow.append(row[4])
        tempRow.append(row[5])
        tempRow.append(row[6])
        tempArray.append(tempRow)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(str(message.from_user.id) + " " + message.from_user.full_name + " => " + message.text)
    bot.reply_to(message, "سلام، به بات تلگرامی دستیار دانشجویی دانشگاه صنعتی شاهرود خوش آمدید")


@bot.message_handler(commands=['plan'])
def send_plan(message):
    print(str(message.from_user.id) + " " + message.from_user.full_name + " => " + message.text)

    saturay_plan = []

    if(day == 6):
        for i in tempArray:
            if(i[5] == "يك شنبه"):
                saturay_plan.append(i)

    if (day == 7):
        for i in tempArray:
            if (i[5] == "دو شنبه"):
                saturay_plan.append(i)

    if (day == 1):
        for i in tempArray:
            if (i[5] == "سه شنبه"):
                saturay_plan.append(i)

    if (day == 2):
        for i in tempArray:
            if (i[5] == "چهار شنبه"):
                saturay_plan.append(i)

    if (day == 3):
        for i in tempArray:
            if (i[5] == "پنج شنبه"):
                saturay_plan.append(i)

    if (day == 4):
        for i in tempArray:
            if (i[5] == "جمعه"):
                saturay_plan.append(i)

    if (day == 5):
        for i in tempArray:
            if (i[5] == "شنبه"):
                saturay_plan.append(i)

    tempString = []
    for i in saturay_plan:
        tempString.append(i[2] + " - " + i[3] + " - " + i[5] +  " - " + i[6])
    for i in tempString:
        bot.reply_to(message, i)



@bot.message_handler(commands=['add'])
def add_class(message):
    print(str(message.from_user.id) + " " + message.from_user.full_name + " => " + message.text)
    tempString = message.text.replace("/add ", "")
    tempClass = tempString
    membersClass.append(tempClass)
    bot.reply_to(message, "کلاس جدید برای شما ثبت شد")



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message.from_user.full_name + " => " + message.text)

bot.infinity_polling()