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
    if call.data == 'get':
        send_sections(call.message)
    elif call.data == 'get1':
        send_mechanics(call.message)
    elif call.data == 'get2':
        send_molecular_physics(call.message)
    elif call.data == 'get3':
        send_electricity_magnetism(call.message)
    elif call.data == 'next_mechanics':
        send_mechanics(call.message)
    elif call.data == 'next_mechanics1':
        send_mechanics_1(call.message)
    elif call.data == 'next_mechanics2':
        send_mechanics_2(call.message)
    elif call.data == 'next_mechanics3':
        send_mechanics_3(call.message)
    elif call.data == 'next_mechanics4':
        send_mechanics_4(call.message)
    elif call.data == 'next_mechanics5':
        send_mechanics_5(call.message)
    elif call.data == 'formula_kinematics':
        send_kinematics_formula(call.message)
    elif call.data == 'formula_statics':
        send_statics_formula(call.message)
    elif call.data == 'formula_dynamics':
        send_dynamics_formula(call.message)
    elif call.data == 'next_molecular_physics':
        send_molecular_physics(call.message)
    elif call.data == 'next_molecular_physics1':
        send_molecular_physics_1(call.message)
    elif call.data == 'next_molecular_physics2':
        send_molecular_physics_2(call.message)
    elif call.data == 'next_molecular_physics3':
        send_molecular_physics_3(call.message)
    elif call.data == 'next_molecular_physics4':
        send_molecular_physics_4(call.message)
    elif call.data == 'next_molecular_physics5':
        send_molecular_physics_5(call.message)
    elif call.data == 'next_electricity_magnetism':
        send_electricity_magnetism(call.message)
    elif call.data == 'next_electricity_magnetism1':
        send_electricity_magnetism_1(call.message)
    elif call.data == 'back_to_sections':
        send_sections(call.message)
    elif call.data == 'test_mechanics':
        send_test(call.message, 'mechanics')
    elif call.data == 'test_molecular_physics':
        send_test(call.message, 'molecular_physics')
    elif call.data == 'test_electricity_magnetism':
        send_test(call.message, 'electricity_magnetism')
    elif call.data.startswith('another_task_'):
        section = call.data.split('_')[-1]
        send_test(call.message, section)


def send_sections(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Механіка", callback_data='get1')
    button2 = types.InlineKeyboardButton("Малекулярная фізіка", callback_data='get2')
    button3 = types.InlineKeyboardButton("Электрычнасць і магнетызм", callback_data='get3')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id,
                     "Для пачатковага ўзроўню рэкамендуем пачаць вывучэнне фізікі з азоў механікі. Гэты раздзел раскажа аб руху матэрыяльных цел і ўзаемадзеянні паміж імі.",
                     reply_markup=markup)


def send_mechanics(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics1')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Вы выбралі Механіку. Механіка - гэта раздзел фізікі, які вывучае рух і ўзаемадзеянне матэрыяльных цел.",
                     reply_markup=markup)


def send_kinematics_formula(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics2')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     """ • V = S/t (хуткасць = перамяшчэнне / час) \n• a = (V2 - V1) / t (паскарэнне = (канчатковая хуткасць - пачатковая хуткасць) / час) \n• s = V0 * t + (a * t^2) / 2 (перамяшчэнне = пачатковая хуткасць * час + (паскарэнне * час^2) / 2) \n• Перамяшчэнне: s = (g * t²) / 2 \n\nРух па акружнасці: \n• Перыяд абароту: T = 2πR/v * T - перыяд абароту (с) * R - радыус акружнасці (м) * v - хуткасць па акружнасці (м/с) \n• Вуглавая хуткасць: ω = 2π/T = v/R * ω - вуглавая хуткасць (рад/с) \n• Цэнтраімклівае паскарэнне: aц = v²/R = ω²R \n• Перамяшчэнне: Δr = r2 - r1 (векторная розніца канчатковага і пачатковага радыус-вектараў) \n• Хуткасць: v = Δr/Δt (вытворная вектара перамяшчэння па часе) \n• Паскарэнне: a = Δv/Δt (вытворная вектара хуткасці па часе) """,
                     reply_markup=markup)


def send_dynamics_formula(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics3')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     """ • Другі закон Ньютана: F = ma, дзе: * F - сумарная сіла, якая дзейнічае на цела * m - маса цела * a - паскаранне цела \n• Вага: P = mg, дзе: * P - вага цела * m - маса цела * g - паскарэнне вольнага падзення (прыблізна 9.8 м/с²) \n• Сіла трэння: Fтр = μN, дзе: * Fтр - сіла трэння * μ - каэфіцыент трэння * N - сіла нармальнай рэакцыі апорнай паверхні \n• Сіла цяжару: Fg = GmM/r², дзе: * Fg - сіла цяжару * G - гравітацыйная пастаянная * M - маса Зямлі (або іншага нябеснага цела) * m - маса цела * r - адлегласць ад цэнтра Зямлі (або іншага нябеснага цела) да цела \n• Закон сувязі паміж масай і вагай: P = mg = GmM/r², дзе: * P - вага цела * m - маса цела * g - паскарэнне вольнага падзення * G - гравітацыйная пастаянная * M - маса Зямлі (або іншага нябеснага цела) * r - адлегласць ад цэнтра Зямлі (або іншага нябеснага цела) да цела """,
                     reply_markup=markup)


def send_statics_formula(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics4')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     """ • Раўнавага: \n\nСтатычная раўнавага - гэта стан цела, калі яго паскарэнне роўна нулю. Гэта азначае, што сумарная сіла, якая дзейнічае на цела, роўная нулю. \n\n• Момент сілы: \nМомент сілы - гэта мера дзеяння сілы на цела, якое выклікае яго кручэнне. * M = F * d, дзе: * M - момент сілы * F - сіла * d - адлегласць ад пункта прыкладання сілы да восі кручэння \n\n• Цэнтр мас: \nЦэнтр мас - гэта кропка, якая прадстаўляе сярэдні пункт масы ўсіх частак цела. \n\n• Умовы раўнавагі: * Сума ўсіх сіл, якія дзейнічаюць на цела, роўная нулю: ΣF = 0. * Сума момантаў усіх сіл адносна любой кропкі роўная нулю: ΣM = 0. \n\n• Трэння: \nТрэння - гэта сіла, якая супрацьдзейнічае руху аднаго цела адносна іншага. * Fтр = μN, дзе: * Fтр - сіла трэння * μ - каэфіцыент трэння * N - сіла нармальнай рэакцыі апорнай паверхні """,
                     reply_markup=markup)


def send_mechanics_1(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics2')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    gif = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, gif)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Раздзелы механікі" + " \n1. Кінематыка: Гэты раздзел вывучае рух цел без уліку прычын, якія выклікаюць гэты рух.  Кінематыка апісвае такія параметры, як хуткасць, паскарэнне і шлях.  \nАсноўныя ўраўненні кінематыкі дазваляюць аналізаваць рух аб'ектаў у розных сістэмах адліку." + "\n\n2. Дынаміка: У адрозненне ад кінематыкі, дынаміка разглядае прычыны руху, гэта значыць сілы, якія дзейнічаюць на целы.  Закон Ньютана, які абвяшчае, што сіла роўна здабытку масы на паскарэнне (F = ma), з'яўляецца асноватворным у дынаміцы.  Дынаміка дапамагае растлумачыць, чаму аб'екты рухаюцца так, як яны рухаюцца." + "\n\n3. Статыка: Гэты раздзел механікі вывучае ўмовы раўнавагі цел.  Статыка аналізуе сілы, якія дзейнічаюць на нерухомыя аб'екты, і вызначае ўмовы, пры якіх яны застаюцца ў стане спакою.  Законы статыкі важныя для праектавання будынкаў, мастоў і іншых канструкцый." + " \n\n4. Механіка матэрыялаў: Гэты падраздзел вывучае паводзіны матэрыялаў пад уздзеяннем вонкавых сіл.  Ён ахоплівае тэмы, такія як напруга, дэфармацыя і трываласць матэрыялаў.  Механіка матэрыялаў мае важнае значэнне ў інжынерыі і будаўніцтве." + " \n\n5. Астранамічная механіка: Гэта вобласць механікі вывучае рух нябесных цел і іх узаемадзеянне.  Астранамічная механіка грунтуецца на законах Ньютана і законах Кеплера, якія апісваюць арбіты планет і спадарожнікаў.",
                     reply_markup=markup)


def send_mechanics_2(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics3')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    button_formula_kinematics = types.InlineKeyboardButton("Асноўныя формулы", callback_data='formula_kinematics')
    markup.add(button_next, button_back, button_test, button_formula_kinematics)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     "Кінематыка: \nКінематыка - гэта раздзел механікі, які вывучае рух цел без уліку прычын, якія выклікаюць гэты рух. Іншамі словамі, мы разглядаем толькі як цела рухаецца, але не чаму яно так рухаецца. \n\nДля гэтага мы выкарыстоўваем велічыні, якія апісваюць рух:\n• Перамяшчэнне (s) - вектар, які злучае пачатковае і канчатковае становішча цела. Ён паказвае напрамак і адлегласць руху.\n• Шлях (l) - скалярная велічыня, якая апісвае даўжыню траекторыі руху цела. \n• Скорасць (v) - вектарная велічыня, якая паказвае хуткасць і напрамак руху цела ў дадзены момант часу.\n• Хуткасць (v) - скалярная велічыня, якая паказвае толькі колькасць руху цела.\n• Паскарэнне (a) - вектарная велічыня, якая паказвае хуткасць змены скорасці цела.\n\nВіды руху:\n• Прамалінейны рух: Рух па прамой лініі.\n• Раўнамерны рух: Рух з пастаяннай хуткасцю.\n• Няраўнамерны рух: Рух з зменнай хуткасцю.\n• Раўнамерна паскараны рух: Рух з пастаянным паскарэннем.",
                     reply_markup=markup)


def send_mechanics_3(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics4')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    button_formula_dynamics = types.InlineKeyboardButton("Асноўныя формулы", callback_data='formula_dynamics')
    markup.add(button_next, button_back, button_test, button_formula_dynamics)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     """ Дынаміка - гэта раздзел механікі, які вывучае рух цел пад дзеяннем сіл. Асноўны закон дынамікі - гэта другі закон Ньютана, які сцвярджае, што паскаранне цела прапарцыйна сумарнай сіле, якая дзейнічае на яго, і напраўлена ў бок дзеяння сілы. """,
                     reply_markup=markup)


def send_mechanics_4(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics5')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    button_formula_statics = types.InlineKeyboardButton("Асноўныя формулы", callback_data='formula_statics')
    markup.add(button_next, button_back, button_test, button_formula_statics)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id,
                     """ Статыка - гэта раздзел механікі, які вывучае ўмовы раўнавагі цел, гэта значыць сітуацыю, калі цела знаходзіцца ў спакоі або рухаецца з пастаяннай хуткасцю. Асноўным законам статыкі з'яўляецца першы закон Ньютана, які сцвярджае, што цела знаходзіцца ў стане спакою або рухаецца з пастаяннай хуткасцю, калі сумарная сіла, якая дзейнічае на яго, роўная нулю. Статыка шырока выкарыстоўваецца ў розных галінах навукі і тэхнікі: • Будаўніцтва: Разлік напружанняў і дэфармацый у канструкцыях, а таксама вызначэнне ўстойлівасці будынкаў. • Механіка: Праектаванне механізмаў, якія рухаюцца з пастаяннай хуткасцю, а таксама вывучэнне ўстойлівасці механізмаў. • Авіяцыя: Распрацоўка самалётаў і верталётаў, улічваючы ўмовы раўнавагі ў палёце. • Машынабудаванне: Праектаванне машын, вызначаючы раўнавагу ўсіх рухомых частак. """,
                     reply_markup=markup)


def send_mechanics_5(message):
    markup = types.InlineKeyboardMarkup()
    button_next = types.InlineKeyboardButton("Працягнуць", callback_data='next_mechanics')
    button_back = types.InlineKeyboardButton("Вярнуцца да раздзелаў", callback_data='back_to_sections')
    button_test = types.InlineKeyboardButton("Тэставае заданне", callback_data='test_mechanics')
    markup.add(button_next, button_back, button_test)

    # Отправляем фото
    photo = open('/Users/a11/Downloads/photo_2024-11-28 11.25.55.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo)

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
