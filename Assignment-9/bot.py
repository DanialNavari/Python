# import library
import random
import telebot
from telebot import types
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime
import gtts
import qrcode

# global variables
computer_number = ''
user_pos = ''
result = ''

# keyboards--------------------------
# game
keyboard_game = types.ReplyKeyboardMarkup(row_width=1)
key1 = types.KeyboardButton("New Game")
key2 = types.KeyboardButton("خروج از بازی")
keyboard_game.add(key1, row_width=1)
keyboard_game.add(key2, row_width=1)

# commands
keyboard_commands = types.ReplyKeyboardMarkup(row_width=3)
key9 = types.KeyboardButton('/start')
key10 = types.KeyboardButton('/game')
key3 = types.KeyboardButton('/age')
key4 = types.KeyboardButton('/voice')
key5 = types.KeyboardButton('/max')
key6 = types.KeyboardButton('/argmax')
key7 = types.KeyboardButton('/qrcode')
key8 = types.KeyboardButton('/help')
keyboard_commands.add(key9, key10, key3, key4, key5, key6, key7, key8)

# return
keyboard_return = types.ReplyKeyboardMarkup(row_width=1)
key11 = types.KeyboardButton('بازگشت')
keyboard_return.add(key11)

# bot api
bot = telebot.TeleBot(
    "6156638689:AAE_LS4FQD-VuLB2qwelFzNH5_BVczKK5EE", parse_mode=None)

# commands
    # start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, message.chat.username +
                     " خوش آمدی", reply_markup=keyboard_commands)
    global user_pos
    user_pos = 0

    # game
@bot.message_handler(commands=['game'])
def game(message):
    bot.send_message(
        message.chat.id, "یک عدد بین 10 تا 40 حدس بزنید", reply_markup=keyboard_game)
    global user_pos
    global computer_number
    computer_number = random.randint(10, 40)
    user_pos = 1

    # age
@bot.message_handler(commands=['age'])
def calAge(message):
    bot.send_message(
        message.chat.id, "تاریخ تولد خود را به صورت 00-00-0000 وارد کنید", reply_markup=keyboard_return)
    global user_pos
    user_pos = 2

    # voice
@bot.message_handler(commands=['voice'])
def translate_voice(message):
    bot.send_message(message.chat.id, 'یک متن انگلیسی ارسال کنید',
                     reply_markup=keyboard_return)
    global user_pos
    user_pos = 3

    # max
@bot.message_handler(commands=['max'])
def translate_voice(message):
    bot.send_message(
        message.chat.id, ' لیستی از اعداد به صورت 1,2,3 وارد کنید', reply_markup=keyboard_return)
    global user_pos
    user_pos = 4

    # argmax
@bot.message_handler(commands=['argmax'])
def translate_voice(message):
    bot.send_message(
        message.chat.id, ' لیستی از اعداد به صورت 1,2,3 وارد کنید', reply_markup=keyboard_return)
    global user_pos
    user_pos = 5

    # help
@bot.message_handler(commands=['help'])
def help_command(message):
    descs = "+	کامند start/ \n با نام کاربر، خوش آمدید چاپ کند. مثلا (sajjad خوش آمدی) "
    descs = descs + \
        "\n\n +	کامند game/ \n بازی حدس عدد اجرا شود. کاربر یک عدد حدس میزند و بات راهنمایی می‌کند (برو بالا، برو پایین، برنده شدی) - در هنگام بازی، یک دکمه new game در پایین بات مشاهده شود."
    descs = descs + \
        "\n\n +	کامند age/ \n تاریخ تولد را به صورت هجری شمسی دریافت نماید و سن را محاسبه نماید. (برای راهنمایی به آدرس اینستاگرامی pylearn@ مراجعه نمایید)"
    descs = descs + "\n\n +	کامند voice/ \n یک جمله به انگلیسی از کاربر دریافت نماید و آن را به صورت voice ارسال نماید."
    descs = descs + "\n\n +	کامند max/ \n یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و بزرگترین مقدار را چاپ نماید."
    descs = descs + "\n\n +	کامند argmax/ \n یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و اندیس بزرگترین مقدار را چاپ نماید."
    descs = descs + "\n\n +	کامند qrcode/ \n یک رشته از کاربر دریافت نماید و qrcode آن را تولید نماید."

    bot.send_message(message.chat.id, descs, reply_markup=keyboard_commands)

    #qrcode
@bot.message_handler(commands=['qrcode'])
def qrcode_maker(message):
    bot.send_message(message.chat.id, 'یک متن وارد کنید',
                     reply_markup=keyboard_return)
    global user_pos
    user_pos = 6

    #user text input and user positions
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global user_pos
    global computer_number
    user_text = message.text

    if user_text == 'New Game':
        bot.send_message(message.chat.id, "یک عدد بین 10 تا 40 حدس بزنید")
        computer_number = random.randint(10, 40)
        user_pos = 1

    elif user_text == 'خروج از بازی':
        user_pos = 0
        bot.send_message(
            message.chat.id, 'یکی از دستورات ربات را انتخاب کنید', reply_markup=keyboard_commands)

    elif user_text == 'بازگشت':
        user_pos = 0
        bot.send_message(
            message.chat.id, 'یکی از دستورات ربات را انتخاب کنید', reply_markup=keyboard_commands)

    elif user_pos == 1:
        user_number = int(message.text)
        if user_number > 0:
            while True:
                # win
                if user_number == computer_number:
                    result = "🎉🎉🎉🎉 Y o u W o n !! 🎉🎉🎉🎉"
                    bot.send_message(message.chat.id, result,
                                     reply_markup=keyboard_game)
                    user_pos = 0
                    break

                # go up
                elif user_number < computer_number:
                    result = "go up"
                    bot.send_message(message.chat.id, result,
                                     reply_markup=keyboard_game)
                    break

                # go down
                elif user_number > computer_number:
                    result = "go down"
                    bot.send_message(message.chat.id, result,
                                     reply_markup=keyboard_game)
                    break

    elif user_pos == 2:
        birthday = (message.text)
        birth = birthday.split('-')
        diffrence = JalaliDatetime.now(
        ) - JalaliDatetime(birth[0], birth[1], birth[2])
        rooz = str(diffrence).split(',')
        x = rooz[0].replace('days', '')
        sen = str(int(int(x) / 365)) + ' سال'
        bot.send_message(message.chat.id, sen)

    elif user_pos == 3:
        translate_sound = gtts.gTTS(message.text, lang='en')
        translate_sound.save('translate.mp3')
        voice = open('translate.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)

    elif user_pos == 4:
        max_num = 0
        adad = str(message.text).split(',')
        for num in adad:
            if int(num) > max_num:
                max_num = int(num)
            else:
                pass
        bot.send_message(
            message.chat.id, 'بزرگترین عدد وارد شده : ' + str(max_num))

    elif user_pos == 5:
        max_num = 0
        max_index = 0
        adad = str(message.text).split(',')
        for id, num in enumerate(adad):
            if int(num) > max_num:
                max_num = int(num)
                max_index = id
            else:
                pass
        bot.send_message(
            message.chat.id, 'اندیس بزرگترین عدد وارد شده : ' + str(max_index))

    elif user_pos == 6:
        img = qrcode.make(message.text)
        img.save("qrcode.png")
        photo = open('qrcode.png', 'rb')
        bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
