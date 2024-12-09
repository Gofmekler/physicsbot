import random
import telebot
from telebot import types

TOKEN = '7733349619:AAEz3DZBqp3HcZKei1OrhkkhOoPyjBVQOHA'
bot = telebot.TeleBot(TOKEN)

# Список тестовых задач
tasks = {
    'mechanics': [
        {
            "question": "Автомабіль рухаецца з паскарэннем 3 м/с² на працягу 10 секунд. Якую хуткасць ён набярэ за гэты час?",
            "answer": "30 м/с", "hint": "Выкарыстайце формулу v = u + at"},
        {
            "question": "Камень кідаюць вертыкальна ўверх з пачатковай хуткасцю 20 м/с. Якая максімальная вышыня, якую ён дасягне?",
            "answer": "20.4 м", "hint": "Выкарыстайце формулу h = v² / (2g)"}
    ],
    'molecular_physics': [
        {
            "question": "Газ у цыліндры з поршнем мае аб'ём 2 літры пры тэмпературы 300 К. Які будзе аб'ём газу пры тэмпературы 600 К, калі ціск застаецца нязменным?",
            "answer": "4 літры", "hint": "Выкарыстайце закон Шарля"},
        {"question": "Колькі малекул змяшчаецца ў 1 моле ідэальнага газу пры нармальных умовах?",
         "answer": "6.022 × 10²³ малекул", "hint": "Выкарыстайце пастаянную Авогадра"}
    ],
    'electricity_magnetism': [
        {
            "question": "Рэзістор з супрацівам 10 Ом падключаны да крыніцы напружання 5 В. Які ток працякае праз рэзістар?",
            "answer": "0.5 А", "hint": "Выкарыстайце закон Ома"},
        {
            "question": "Магнітнае поле з індукцыяй 0.2 Тл дзейнічае на праваднік даўжынёй 0.5 м, па якім працякае ток 3 А. Якая сіла дзейнічае на праваднік?",
            "answer": "0.3 Н", "hint": "Выкарыстайце формулу F = BIL"}]}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Атрымаць спіс раздзелаў", callback_data='get')
    markup.add(button)
    bot.send_message(message.chat.id,
                     "Вітаю, робат дапаможа ў вывучэнні фізікі з самага пачатку. Цісні кнопку ніжэй, каб атрымаць спіс раздзелаў.",
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "/get":
        send_sections(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    data_to_function = {
        'get': send_sections,
        'get1': send_mechanics,
        'get2': send_molecular_physics,
        'get3': send_electricity_magnetism,
        'next_mechanics': send_mechanics,
        'next_mechanics1': send_mechanics_1,
        'next_mechanics2': send_mechanics_2,
        'next_mechanics3': send_mechanics_3,
        'next_mechanics4': send_mechanics_4,
        'next_mechanics5': send_mechanics_5,
        'next_molecular_physics': send_molecular_physics,
        'next_molecular_physics1': send_molecular_physics_1,
        'next_molecular_physics2': send_molecular_physics_2,
        'next_molecular_physics3': send_molecular_physics_3,
        'next_molecular_physics4': send_molecular_physics_4,
        'next_molecular_physics5': send_molecular_physics_5,
        'next_electricity_magnetism': send_electricity_magnetism,
        'next_electricity_magnetism1': send_electricity_magnetism_1,
        'back_to_sections': lambda msg: send_sections(msg),
        'test_mechanics': lambda msg: send_test(msg, 'mechanics'),
        'test_molecular_physics': lambda msg: send_test(msg, 'molecular_physics'),
        'test_electricity_magnetism': lambda msg: send_test(msg, 'electricity_magnetism'), }
    if call.data.startswith('another_task_'):
        section = call.data.split('_')[-1]
        send_test(call.message, section)
    else:
        function = data_to_function.get(call.data)
    if function:
        function(call.message)

def send_sections(message):
    markup = types.InlineKeyboardMarkup()
    buttons = [ types.InlineKeyboardButton("Механіка", callback_data='get1'),
      types.InlineKeyboardButton("Малекулярная фізіка", callback_data='get2'),
      types.InlineKeyboardButton("Электрычнасць і магнетызм", callback_data='get3') ]
    markup.add(*buttons)
    message_text = "Для пачатковага ўзроўню рэкамендуем пачаць вывучэнне фізікі з азоў механікі. " "Гэты раздзел раскажа аб руху матэрыяльных цел і ўзаемадзеянні паміж імі."
    bot.send_message(message.chat.id, message_text, reply_markup=markup)


def send_mechanics(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics1')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    button_test = types.InlineKeyboardButton("Асноўныя формулы:", callback_data='formula_mechanics_kinematics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #photo = open('D:/Telegram Downloads/photo_2024-11-21_13-34-15.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Вы выбралі Механіку. Механіка - гэта раздзел фізікі, які вывучае рух і ўзаемадзеянне матэрыяльных цел.",
                     reply_markup=markup)


def send_mechanics_1(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics2')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #gif = open('C:/Users/Administrator/Downloads/transmission-925_512.gif', 'rb')
    #bot.send_animation(message.chat.id, gif)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Раздзелы механікі"+" \n1. Кінематыка: Гэты раздзел вывучае рух цел без уліку прычын, якія выклікаюць гэты рух.  Кінематыка апісвае такія параметры, як хуткасць, паскарэнне і шлях.  \nАсноўныя ўраўненні кінематыкі дазваляюць аналізаваць рух аб'ектаў у розных сістэмах адліку."+"\n\n2. Дынаміка: У адрозненне ад кінематыкі, дынаміка разглядае прычыны руху, гэта значыць сілы, якія дзейнічаюць на целы.  Закон Ньютана, які абвяшчае, што сіла роўна здабытку масы на паскарэнне (F = ma), з'яўляецца асноватворным у дынаміцы.  Дынаміка дапамагае растлумачыць, чаму аб'екты рухаюцца так, як яны рухаюцца."+"\n\n3. Статыка: Гэты раздзел механікі вывучае ўмовы раўнавагі цел.  Статыка аналізуе сілы, якія дзейнічаюць на нерухомыя аб'екты, і вызначае ўмовы, пры якіх яны застаюцца ў стане спакою.  Законы статыкі важныя для праектавання будынкаў, мастоў і іншых канструкцый."+" \n\n4. Механіка матэрыялаў: Гэты падраздзел вывучае паводзіны матэрыялаў пад уздзеяннем вонкавых сіл.  Ён ахоплівае тэмы, такія як напруга, дэфармацыя і трываласць матэрыялаў.  Механіка матэрыялаў мае важнае значэнне ў інжынерыі і будаўніцтве."+" \n\n5. Астранамічная механіка: Гэта вобласць механікі вывучае рух нябесных цел і іх узаемадзеянне.  Астранамічная механіка грунтуецца на законах Ньютана і законах Кеплера, якія апісваюць арбіты планет і спадарожнікаў.",reply_markup=markup)


def send_mechanics_2(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics3')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #photo = open('D:/Telegram Downloads/photo_2024-11-21_13-34-15.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Кінематыка: \nКінематыка - гэта раздзел механікі, які вывучае рух цел без уліку прычын, якія выклікаюць гэты рух. Іншамі словамі, мы разглядаем толькі як цела рухаецца, але не чаму яно так рухаецца. \n\nДля гэтага мы выкарыстоўваем велічыні, якія апісваюць рух:\n• Перамяшчэнне (s) - вектар, які злучае пачатковае і канчатковае становішча цела. Ён паказвае напрамак і адлегласць руху.\n• Шлях (l) - скалярная велічыня, якая апісвае даўжыню траекторыі руху цела. \n• Скорасць (v) - вектарная велічыня, якая паказвае хуткасць і напрамак руху цела ў дадзены момант часу.\n• Хуткасць (v) - скалярная велічыня, якая паказвае толькі колькасць руху цела.\n• Паскарэнне (a) - вектарная велічыня, якая паказвае хуткасць змены скорасці цела.\n\nВіды руху:\n• Прамалінейны рух: Рух па прамой лініі.\n• Раўнамерны рух: Рух з пастаяннай хуткасцю.\n• Няраўнамерны рух: Рух з зменнай хуткасцю.\n• Раўнамерна паскараны рух: Рух з пастаянным паскарэннем.",reply_markup=markup)


def send_mechanics_3(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics4')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #photo = open('D:/Telegram Downloads/photo_2024-11-21_13-34-15.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Вы выбралі Механіку. Механіка - гэта раздзел фізікі, які вывучае рух і ўзаемадзеянне матэрыяльных цел.",
                     reply_markup=markup)


def send_mechanics_4(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics5')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #photo = open('D:/Telegram Downloads/photo_2024-11-21_13-34-15.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Вы выбралі Механіку. Механіка - гэта раздзел фізікі, які вывучае рух і ўзаемадзеянне матэрыяльных цел.",
                     reply_markup=markup)


def send_mechanics_5(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    #photo = open('D:/Telegram Downloads/photo_2024-11-21_13-34-15.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Вы выбралі Механіку. Механіка - гэта раздзел фізікі, які вывучае рух і ўзаемадзеянне матэрыяльных цел.",
                     reply_markup=markup)

def send_molecular_physics(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics1')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)

def send_molecular_physics_1(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics2')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)

def send_molecular_physics_2(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics3')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)

def send_molecular_physics_3(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics4')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)

def send_molecular_physics_4(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics5')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)

def send_molecular_physics_5(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_molecular_physics')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_molecular_physics')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Малекулярную фізіку. Малекулярная фізіка вывучае ўласцівасці і паводзіны малекул і атамаў.",
                     reply_markup=markup)


def send_electricity_magnetism(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_electricity_magnetism1')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_electricity_magnetism')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Электрычнасць і магнетызм. Гэты раздзел фізікі вывучае электрычныя і магнітныя з'явы.",
                     reply_markup=markup)

def send_electricity_magnetism_1(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_electricity_magnetism')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_electricity_magnetism')
    markup.add(button_next, button_back, button_test)
    bot.send_message(message.chat.id,
                     "Вы выбралі Электрычнасць і магнетызм. Гэты раздзел фізікі вывучае электрычныя і магнітныя з'явы.",
                     reply_markup=markup)

def send_test(message, section):
    task = random.choice(tasks[section])
    bot.send_message(message.chat.id, task["question"])
    bot.register_next_step_handler(message, lambda msg: check_answer(msg, task["answer"], section, task["hint"]))


def check_answer(message, correct_answer, section, hint):
    markup = types.InlineKeyboardMarkup()
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_another = types.InlineKeyboardButton("Яшчэ адна задача", callback_data=f'another_task_{section}')
    button_hint = types.InlineKeyboardButton("Падказка", callback_data=f'hint_{section}')
    markup.add(button_back, button_another, button_hint)

    if message.text.lower() == correct_answer.lower():
        bot.send_message(message.chat.id, "Правільна!", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f"Няправільна. Правільны адказ: {correct_answer}", reply_markup=markup)


def send_hint(message, section):
    task = next(task for task in tasks[section] if task["question"] in message.text)
    bot.send_message(message.chat.id, f"Падказка: {task['hint']}")


bot.polling()
