#You need to install modules using pip depending on your version
#check pip version using command in terminal: pip --version

#Loadable modules:
#pip install telebot
#pip install BeautifulSoup4
#pip install requests
#pipn install lxml

import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup as bs
import lxml

import locale

#for_heroku
locale.setlocale(locale.LC_ALL, 'de_De')

bot = telebot.TeleBot('Paste your key API here')

#You can change variable hraders, how you want.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}



class currency_rate():
    class euro_usd_rub():
        def euro_rub():
            url_currency_euro_to_rub = 'https://www.investing.com/currencies/eur-rub'
            pages_currency_euro_to_rub = requests.get(url_currency_euro_to_rub, headers = headers)
            soup_currency_euro_to_ru = bs(pages_currency_euro_to_rub.text, 'lxml')
        
            vars_euro_rub= soup_currency_euro_to_ru.find_all('span', class_= 'text-2xl')
        
            for var_euro_rub in vars_euro_rub:   
                return var_euro_rub.text
            

        def usd_rub():
            url_currency_usd_to_rub = 'https://ru.investing.com/currencies/usd-rub'
            pages_currency_usd_to_rub = requests.get(url_currency_usd_to_rub, headers = headers)
            soup_currency_usd_to_rub = bs(pages_currency_usd_to_rub.text, 'lxml')
        
            vars_usd_rub = soup_currency_usd_to_rub.find_all('span', class_= 'text-2xl')
        
            for var_usd_rub in vars_usd_rub:   
                return var_usd_rub.text

    class euro_usd_uah():
        def euro_uah():
            url_currency_euro_to_uah = 'https://www.investing.com/currencies/eur-uah'
            pages_currency_euro_to_uah = requests.get(url_currency_euro_to_uah, headers = headers)
            soup_currency_euro_to_uah = bs(pages_currency_euro_to_uah.text, 'lxml')
        
            vars_euro_uah = soup_currency_euro_to_uah.find_all('span', class_= 'text-2xl')
        
            for var_euro_uah in vars_euro_uah:   
                return var_euro_uah.text

        def usd_uah():
            url_currency_usd_to_uah = 'https://ru.investing.com/currencies/usd-uah'
            pages_currency_usd_to_uah = requests.get(url_currency_usd_to_uah, headers = headers)
            soup_currency_usd_to_uah = bs(pages_currency_usd_to_uah.text, 'lxml')
        
            vars_usd_uah = soup_currency_usd_to_uah.find_all('span', class_= 'text-2xl')
        
            for var_usd_uah in vars_usd_uah:   
                return var_usd_uah.text
            
    class euro_usd_byn():
        def euro_byn():
            url_currency_euro_to_byn = 'https://www.investing.com/currencies/eur-byn'
            pages_currency_euro_to_byn = requests.get(url_currency_euro_to_byn, headers = headers)
            soup_currency_euro_to_byn = bs(pages_currency_euro_to_byn.text, 'lxml')
        
            vars_euro_byn = soup_currency_euro_to_byn.find_all('span', class_= 'text-2xl')
        
            for var_euro_byn in vars_euro_byn: 
                return var_euro_byn.text

        def usd_byn():
            url_currency_usd_to_byn = 'https://ru.investing.com/currencies/usd-byn'
            pages_currency_usd_to_byn = requests.get(url_currency_usd_to_byn, headers = headers)
            soup_currency_usd_to_byn = bs(pages_currency_usd_to_byn.text, 'lxml')
            
            vars_usd_byn = soup_currency_usd_to_byn.find_all('span', class_= 'text-2xl')
        
            for var_usd_byn in vars_usd_byn: 
                return var_usd_byn.text

    class euro_usd_kzt():
        def euro_kzt():
            url_currency_euro_to_kzt = 'https://www.investing.com/currencies/eur-kzt'
            pages_currency_euro_to_kzt = requests.get(url_currency_euro_to_kzt, headers = headers)
            soup_currency_euro_to_kzt = bs(pages_currency_euro_to_kzt.text, 'lxml')
        
            vars_euro_kzt = soup_currency_euro_to_kzt.find_all('span', class_= 'text-2xl')
            
            for var_euro_kzt in vars_euro_kzt: 
                return var_euro_kzt.text

        def usd_kzt():
            url_currency_usd_to_kzt = 'https://ru.investing.com/currencies/usd-kzt'
            pages_currency_usd_to_kzt = requests.get(url_currency_usd_to_kzt, headers = headers)
            soup_currency_usd_to_kzt = bs(pages_currency_usd_to_kzt.text, 'lxml')
        
            vars_usd_kzt = soup_currency_usd_to_kzt.find_all('span', class_= 'text-2xl')
            
            for var_usd_kzt in vars_usd_kzt: 
                return var_usd_kzt.text

'''    
class currency_converter():
    class euro_usd_rub():
        def euro_rub():
            result = get_number() * currency_rate.euro_usd_rub.euro_rub()
            return result
        
        def rub_euro():
            result = currency_rate.euro_usd_rub.euro_rub() / get_number()
            return result
'''            

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(True)
    currency_rate_button = types.KeyboardButton('Currency rate')
    currency_converter_button = types.KeyboardButton('Сurrency converter')
    
    markup.add(currency_rate_button, currency_converter_button)
    
    bot.send_message(message.chat.id, 'Hello, {0.first_name}! Select what you want from list.'.format(message.from_user), reply_markup= markup)



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':


#buttons_currency_rate
        if message.text == 'Currency rate':
            markup = types.ReplyKeyboardMarkup(True)
            euro_button = types.KeyboardButton('RUB')
            usd_button = types.KeyboardButton('UAH')
            byn_button = types.KeyboardButton('BYN')
            kzt_button = types.KeyboardButton('KZT')
            back_home = types.KeyboardButton('BACK_home')
        
            markup.add(euro_button, usd_button, byn_button, kzt_button, back_home)

            bot.send_message(message.chat.id, 'Currency rate', reply_markup= markup)


#buttons_currecnty_rate_sub_menu
        elif message.text == 'RUB':
            markup = types.ReplyKeyboardMarkup(True)
            euro_rub_button = types.KeyboardButton('EURO-RUB')
            usd_rub_button = types.KeyboardButton('USD-RUB')
            button_back =  types.KeyboardButton('BACK')
            
            markup.add(euro_rub_button, usd_rub_button, button_back)

            bot.send_message(message.chat.id, 'Сurrency rate RUB', reply_markup= markup)
            
        elif message.text == 'UAH':
            markup = types.ReplyKeyboardMarkup(True)
            euro_uah_button = types.KeyboardButton('EURO-UAH')
            usd_uah_button = types.KeyboardButton('USD-UAH')
            button_back =  types.KeyboardButton('BACK')
            
            markup.add(euro_uah_button, usd_uah_button, button_back)

            bot.send_message(message.chat.id, 'Сurrency rate UAH', reply_markup= markup)

        elif message.text == 'BYN':
            markup = types.ReplyKeyboardMarkup(True)
            euro_byn_button = types.KeyboardButton('EURO-BYN')
            usd_byn_button = types.KeyboardButton('USD-BYN')
            button_back =  types.KeyboardButton('BACK')
            
            markup.add(euro_byn_button, usd_byn_button, button_back)

            bot.send_message(message.chat.id, 'Сurrency rate BYN', reply_markup= markup)  

        elif message.text == 'KZT':
            markup = types.ReplyKeyboardMarkup(True)
            euro_kzt_button = types.KeyboardButton('EURO-KZT')
            usd_kzt_button = types.KeyboardButton('USD-KZT')
            button_back =  types.KeyboardButton('BACK')
            
            markup.add(euro_kzt_button, usd_kzt_button, button_back)

            bot.send_message(message.chat.id, 'Сurrency rate KZT', reply_markup= markup)


#buttons_back_currency_rate
        elif message.text == 'BACK':
            markup = types.ReplyKeyboardMarkup(True)
            euro_button = types.KeyboardButton('RUB')
            usd_button = types.KeyboardButton('UAH')
            byn_button = types.KeyboardButton('BYN')
            kzt_button = types.KeyboardButton('KZT')
            back_home = types.KeyboardButton('BACK_home')
            
            markup.add(euro_button, usd_button, byn_button, kzt_button, back_home)

            bot.send_message(message.chat.id, 'BACK', reply_markup= markup)


#buttons_back_home             
        elif message.text == 'BACK_home':
            markup = types.ReplyKeyboardMarkup(True)
            currency_rate_button = types.KeyboardButton('Currency rate')
            currency_converter_button = types.KeyboardButton('Сurrency converter')

            markup.add(currency_rate_button, currency_converter_button)

            bot.send_message(message.chat.id, 'BACK_home'.format(message.from_user), reply_markup= markup)      


#execution_buttons_currency_rate 
        elif message.text == 'EURO-RUB':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_rub.euro_rub()))
        elif message.text == 'USD-RUB':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_rub.usd_rub()))       
        elif message.text == 'EURO-UAH':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_uah.euro_uah())) 
        elif message.text == 'USD-UAH':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_uah.usd_uah())) 
        elif message.text == 'EURO-BYN':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_byn.euro_byn())) 
        elif message.text == 'USD-BYN':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_byn.usd_byn()))   
        elif message.text == 'EURO-KZT':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_kzt.euro_kzt())) 
        elif message.text == 'USD-KZT':
            bot.send_message(message.chat.id, str(currency_rate.euro_usd_kzt.usd_kzt()))        


#buttons_currency_converter 
        elif message.text == 'Сurrency converter':
            markup = types.ReplyKeyboardMarkup(True)
            rub_button_converter = types.KeyboardButton('RUB_converter')
            uah_button_converter = types.KeyboardButton('UAH_converter')
            byn_button_converter = types.KeyboardButton('BYN_converter')
            kzt_button_converter = types.KeyboardButton('KZT_converter')
            back_home = types.KeyboardButton('BACK_home')
            markup.add(rub_button_converter, uah_button_converter, byn_button_converter, kzt_button_converter, back_home)

            bot.send_message(message.chat.id, 'Currency converter', reply_markup= markup)


#buttons_rub_converter            
        elif message.text == 'RUB_converter':
            markup = types.ReplyKeyboardMarkup(True)
            euro_rub_button_converter = types.KeyboardButton('EURO-RUB_converter')
            rub_euro_button_converter = types.KeyboardButton('RUB-EURO_converter')
            usd_rub_button_converter = types.KeyboardButton('USD-RUB_converter')
            rub_usd_button_converter = types.KeyboardButton('RUB-USD_converter')
            back_converter = types.KeyboardButton('BACK_converter')
        
            markup.add(euro_rub_button_converter, rub_euro_button_converter, usd_rub_button_converter, rub_usd_button_converter, back_converter)
        
            bot.send_message(message.chat.id, 'Currency converter RUB', reply_markup= markup)


#buttons_uah_converter                
        elif message.text == 'UAH_converter':
            markup = types.ReplyKeyboardMarkup(True)
            euro_uah_button_converter = types.KeyboardButton('EURO-UAH_converter')
            uah_euro_button_converter = types.KeyboardButton('UAH-EURO_converter')
            usd_uah_button_converter = types.KeyboardButton('USD-UAH_converter')
            uah_usd_button_converter = types.KeyboardButton('UAH-USD_converter')
            back_converter = types.KeyboardButton('BACK_converter')
        
            markup.add(euro_uah_button_converter, uah_euro_button_converter, usd_uah_button_converter, uah_usd_button_converter, back_converter)
        
            bot.send_message(message.chat.id, 'Currency converter UAH', reply_markup= markup)
            
            
#buttons_byn_converter            
        elif message.text == 'BYN_converter':
            markup = types.ReplyKeyboardMarkup(True)
            euro_byn_button_converter = types.KeyboardButton('EURO-BYN_converter')
            byn_euro_button_converter = types.KeyboardButton('BYN-EURO_converter')
            usd_byn_button_converter = types.KeyboardButton('USD-BYN_converter')
            byn_usd_button_converter = types.KeyboardButton('BYN-USD_converter')
            back_converter = types.KeyboardButton('BACK_converter')
        
            markup.add(euro_byn_button_converter, byn_euro_button_converter, usd_byn_button_converter, byn_usd_button_converter, back_converter)
        
            bot.send_message(message.chat.id, 'Currency converter UAH', reply_markup= markup)


#buttons_kzt_converter            
        elif message.text == 'KZT_converter':
            markup = types.ReplyKeyboardMarkup(True)
            euro_kzt_button_converter = types.KeyboardButton('EURO-KZT_converter')
            kzt_euro_button_converter = types.KeyboardButton('KZT-EURO_converter')
            usd_kzt_button_converter = types.KeyboardButton('USD-KZT_converter')
            kzt_usd_button_converter = types.KeyboardButton('KZT-USD_converter')
            back_converter = types.KeyboardButton('BACK_converter')
        
            markup.add(euro_kzt_button_converter, kzt_euro_button_converter, usd_kzt_button_converter, kzt_usd_button_converter, back_converter)
        
            bot.send_message(message.chat.id, 'Currency converter UAH', reply_markup= markup)


#button_back_converter
        elif message.text == 'BACK_converter':
            markup = types.ReplyKeyboardMarkup(True)
            rub_button_converter = types.KeyboardButton('RUB_converter')
            uah_button_converter = types.KeyboardButton('UAH_converter')
            byn_button_converter = types.KeyboardButton('BYN_converter')
            kzt_button_converter = types.KeyboardButton('KZT_converter')
            back_home = types.KeyboardButton('BACK_home')
            markup.add(rub_button_converter, uah_button_converter, byn_button_converter, kzt_button_converter, back_home)

            bot.send_message(message.chat.id, 'BACK_converter', reply_markup= markup)            


#RUB_converter 
        elif message.text == 'EURO-RUB_converter':
            bot.send_message(message.chat.id, "Currency converter EURO-RUB. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_euro_rub);
             
        elif message.text == 'RUB-EURO_converter':
            bot.send_message(message.chat.id, "Currency converter RUB-EURO. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_rub_euro);

        elif message.text == 'USD-RUB_converter':
            bot.send_message(message.chat.id, "Currency converter USD-RUB. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_usd_rub);
             
        elif message.text == 'RUB-USD_converter':
            bot.send_message(message.chat.id, "Currency converter RUB-USD. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_rub_usd);
        
        
#UAH_converter         
        elif message.text == 'EURO-UAH_converter':
            bot.send_message(message.chat.id, "Currency converter EURO-UAH. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_euro_uah);
             
        elif message.text == 'UAH-EURO_converter':
            bot.send_message(message.chat.id, "Currency converter UAH-EURO. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_uah_euro);

        elif message.text == 'USD-UAH_converter':
            bot.send_message(message.chat.id, "Currency converter USD-UAH. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_usd_uah);
             
        elif message.text == 'UAH-USD_converter':
            bot.send_message(message.chat.id, "Currency converter UAH-USD. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_uah_usd);
            
        
#BYN_converter                 
        elif message.text == 'EURO-BYN_converter':
            bot.send_message(message.chat.id, "Currency converter EURO-BYN. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_euro_byn);
             
        elif message.text == 'BYN-EURO_converter':
            bot.send_message(message.chat.id, "Currency converter BYN-EURO. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_byn_euro);

        elif message.text == 'USD-BYN_converter':
            bot.send_message(message.chat.id, "Currency converter USD-BYN. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_usd_byn);
             
        elif message.text == 'BYN-USD_converter':
            bot.send_message(message.chat.id, "Currency converter BYN-USD. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_byn_usd);
         
         
#KZT_converter             
        elif message.text == 'EURO-KZT_converter':
            bot.send_message(message.chat.id, "Currency converter EURO-KZT. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_euro_kzt);
             
        elif message.text == 'KZT-EURO_converter':
            bot.send_message(message.chat.id, "Currency converter KZT-EURO. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_kzt_euro);

        elif message.text == 'USD-KZT_converter':
            bot.send_message(message.chat.id, "Currency converter USD-KZT. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_usd_kzt);
             
        elif message.text == 'KZT-USD_converter':
            bot.send_message(message.chat.id, "Currency converter KZT-USD. Enter a digit.");
            bot.register_next_step_handler(message, get_number_conv_kzt_usd);
     


#def_converter_rub
def get_number_conv_euro_rub(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = float(entered_number) * float(currency_rate.euro_usd_rub.euro_rub()); 
            b = round(result, 1)
            bot.send_message(message.from_user.id, "EURO is RUB: {enter_number} is {res}".format(enter_number = a, res = b));
 
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_euro_rub)

                
def get_number_conv_rub_euro(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number / float(currency_rate.euro_usd_rub.euro_rub());
            b = round(result, 1)
            bot.send_message(message.chat.id, "RUB is EURO: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_rub_euro)
               
def get_number_conv_usd_rub(message):   
    if message.text == int or float:
        try: 
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number * locale.atof(currency_rate.euro_usd_rub.usd_rub());
            b = round(result, 1)
            bot.send_message(message.chat.id, "USD is RUB: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_usd_rub)
    
def get_number_conv_rub_usd(message):   
    if message.text == int or float:
        try: 
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number / locale.atof(currency_rate.euro_usd_rub.usd_rub());
            b = round(result, 1)
            bot.send_message(message.chat.id, "RUB is USD: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_rub_usd)
                
       
#def_converter_uah               
def get_number_conv_euro_uah(message):   
    if message.text == int or float:
        try:
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number * float(currency_rate.euro_usd_uah.euro_uah());
            b = round(result, 1)
            bot.send_message(message.chat.id, "EURO is UAH: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_euro_uah)
    
def get_number_conv_uah_euro(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number / float(currency_rate.euro_usd_uah.euro_uah());
            b = round(result, 1)
            bot.send_message(message.chat.id, "UAH is EURO: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_uah_euro)
                      
def get_number_conv_usd_uah(message):   
    if message.text == int or float:
        try: 
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number * locale.atof(currency_rate.euro_usd_uah.usd_uah());
            b = round(result, 1)
            bot.send_message(message.chat.id, "USD is UAH: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_usd_uah)
    
def get_number_conv_uah_usd(message):   
    if message.text == int or float:
        try:
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number / locale.atof(currency_rate.euro_usd_uah.usd_uah());
            b = round(result, 1)
            bot.send_message(message.chat.id, "UAH is USD: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_uah_usd)               

#def_converter_byn
def get_number_conv_euro_byn(message):   
    if message.text == int or float:
        try:
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number * float(currency_rate.euro_usd_byn.euro_byn());
            b = round(result, 1)
            bot.send_message(message.chat.id, "EURO is BYN: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_euro_byn)
    
def get_number_conv_byn_euro(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number / float(currency_rate.euro_usd_byn.euro_byn());
            b = round(result, 1)
            bot.send_message(message.chat.id, "BYN is EURO: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_byn_euro)
                     
def get_number_conv_usd_byn(message):   
    if message.text == int or float:
        try:
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number * locale.atof(currency_rate.euro_usd_byn.usd_byn());
            b = round(result, 1)
            bot.send_message(message.chat.id, "USD is BYN: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_usd_byn)
    
def get_number_conv_byn_usd(message):   
    if message.text == int or float:
        try:
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number / locale.atof(currency_rate.euro_usd_byn.usd_byn());
            b = round(result, 1)
            bot.send_message(message.chat.id, "BYN is USD: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_byn_usd)
    

#def_converter_kzt
def get_number_conv_euro_kzt(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number * float(currency_rate.euro_usd_kzt.euro_kzt());
            b = round(result, 1)
            bot.send_message(message.chat.id, "EURO is KZT: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_euro_kzt)
    
def get_number_conv_kzt_euro(message):   
    if message.text == int or float:
        try: 
            entered_number = float(message.text)
            a = round(entered_number, 1)
            result = entered_number / float(currency_rate.euro_usd_kzt.euro_kzt());
            b = round(result, 1)
            bot.send_message(message.chat.id, "KZT is EURO: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_kzt_euro)
                      
def get_number_conv_usd_kzt(message):   
    if message.text == int or float:
        try: 
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number * locale.atof(currency_rate.euro_usd_kzt.usd_kzt());
            b = round(result, 1)
            bot.send_message(message.chat.id, "USD is KZT: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_usd_kzt)
    
def get_number_conv_kzt_usd(message):   
    if message.text == int or float:
        try:
            entered_number = locale.atof(message.text)
            a = round(entered_number, 1)
            result = entered_number / locale.atof(currency_rate.euro_usd_kzt.usd_kzt());
            b = round(result, 1)
            bot.send_message(message.chat.id, "KZT is USD: {enter_number} is {res}".format(enter_number = a, res = b));
        except Exception:
            bot.send_message(message.chat.id, 'You entered not digit! Try attempt again.')
            bot.register_next_step_handler(message, get_number_conv_kzt_usd)
                   
                
bot.polling(none_stop=True, interval=0)
    


