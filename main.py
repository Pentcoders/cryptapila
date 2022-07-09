import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, admin
import keyboard as kb
import functions as func
import sqlite3
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import Throttled
import datetime
import time as cagat
import datetime
from datetime import datetime, date, time

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
connection = sqlite3.connect('data.db')
q = connection.cursor()

class st(StatesGroup):
	item = State()
	item2 = State()
	item3 = State()
	item4 = State()

class mal(StatesGroup):
	bit = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('Добро пожаловать.', reply_markup=kb.menu)
		else:
			await bot.send_video(message.chat.id, open('img/startgif.mp4', 'rb'))
			local_time = '1'
			cagat.sleep(int(local_time))
			await bot.send_photo(message.chat.id, open('img/first.jpg', 'rb'), caption='Ну наконец-то ты проснулся. Я уж думал ты не очнёшься')
			local_time = '2'
			cagat.sleep(int(local_time))
			await message.answer('Ты в моей игре\n\nЭто моя личная МЕТА вселенная. Здесь все играют🎮 по моим правилам. И ты будешь тоже...')
			local_time = '3'
			cagat.sleep(int(local_time))
			await message.answer('''
Меня зовут Крипто Пила

Я трейдер. И спекулянт. Умею покупать дешево и продавать дорого 🤑

Ты здесь, чтобы увидеть другую реальность. Ту реальность, где можно начать по-настоящему управлять своей жизнью и этим непредсказуемым миром
				''')
			local_time = '4'
			cagat.sleep(int(local_time))
			await bot.send_photo(message.chat.id, open('img/two.jpg', 'rb'), caption='Сейчас мы с тобой сыграем🎮  в игру, в которой только ты будешь управлять сюжетом\n\nТы можешь вырваться из этой игры, разбогатеть💰 и вытащить себя из этой неудобной и несладкой реальности\n\nИли продолжить зависеть от нестабильности мира и быть марионеткой в чужих руках', reply_markup=kb.berkn)

@dp.message_handler(content_types=['text'], text='⏪ Назад')
async def handledr(message: types.Message, state: FSMContext):
	await message.answer('Добро пожаловать, Ублюдок.', reply_markup=kb.menu)

@dp.message_handler(content_types=['text'], text='бомба')
async def handledr(message: types.Message, state: FSMContext):
	await bot.send_photo(message.chat.id, open('img/loading.jpg', 'rb'))

@dp.message_handler(content_types=['text'], text='💬 Рассылка')
async def hangdler(message: types.Message, state: FSMContext):
	func.join(chat_id=message.chat.id)
	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
	result = q.fetchone()
	if result[0] == 0:
		if message.chat.id == admin:
			await message.answer('Введите текст для рассылки.\n\nДля отмены нажми блять на кнопку ниже', reply_markup=kb.back)
			await st.item.set()

#@dp.message_handler(content_types=['text'])
#async def h(message: types.Message, state: FSMContext):
#	func.join(chat_id=message.chat.id)
#	q.execute(f"SELECT block FROM users WHERE user_id = {message.chat.id}")
#	result = q.fetchone()
#	if result[0] == 0:
#		if message.chat.id == admin:
#			pass
#		else:
#			await message.answer('Сообщение Улител.')
#			await bot.send_message(admin, f"<b>Получен новый вопрос!</b>\n<b>От:</b> {message.from_user.mention}\nID: {message.chat.id}\n<b>Сообщение:</b> {message.text}", reply_markup=kb.fun(message.chat.id), parse_mode='HTML')


@dp.callback_query_handler(lambda call: True) # Inline часть
async def cal(call, state: FSMContext):
	if 'ans' in call.data:
		a = call.data.index('-ans')
		ids = call.data[:a]
		await call.message.answer('Введите ответ @slivmenss:', reply_markup=kb.back)
		await st.item2.set() # админ отвечает пользователю
		await state.update_data(uid=ids)
	elif 'ignor' in call.data:
		await call.answer('Удалено')
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await state.finish()
	elif 'obpr' in call.data:
		await call.message.answer('Мне нравится твой настрой🤝. Кстати, как тебя зовут?')
		await mal.bit.set()
	elif 'balanc' in call.data:
		await call.message.answer('Баланс сейчас:\n🪙 0.00 ПилаCOIN')
		local_time = '1'
		cagat.sleep(int(local_time))
		await call.message.answer('Чтобы их заработать, тебе нужно правильно🧠 отвечать на мои вопросы. Всего их будет 5\n\nНа каждый я даю ровно ⏳30 секунд и не больше. Не уложился - проиграл. Поэтому тебе нужно оставаться в чате и думать очень быстро')
		local_time = '2'
		cagat.sleep(int(local_time))
		await call.message.answer('Если сможешь заработать 🪙 5.000 ПилаCOIN, то получишь доступ к знаниям о том, как с полного нуля в крипте ты можешь поднимать💵 свои первые 10 000$\n\nС ПОЛНОГО НУЛЯ\n\nДаже если все твои познания в крипте заканчиваются на: “ну, я знаю, что есть биток и есть эфир, и их можно продавать”, то эта информация будет для тебя ценнее, чем последний стакан воды🚰 посреди Сахары')
		local_time = '3'
		cagat.sleep(int(local_time))
		await call.message.answer('🎮 Нажми кнопку ИГРАТЬ только тогда, когда будешь готов', reply_markup=kb.play)
	elif 'playing' in call.data:
		chat_id = call.message.chat.id
		await bot.send_animation(chat_id, open('img/ber.gif', 'rb'))
		await bot.send_animation(chat_id, open('img/ike.gif', 'rb'))
		await bot.send_photo(chat_id, open('img/error.jpg', 'rb'), caption='ERROR выбор персонажа\n\nПри загрузке игры обнаружилась ошибка')
		await call.message.answer('Чтобы приступить к игре, выбери персонажа🚶, который наиболее похож на тебя:', reply_markup=kb.person)
	elif 'naemrab' in call.data:
		await call.message.answer('Выбери возраст:', reply_markup=kb.age)
	elif 'ages' in call.data:
		await call.message.answer('loading 100%')
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/loading.jpg', 'rb'), caption='✅Загрузка игрового пространства...')
		local_time = '1'
		cagat.sleep(int(local_time))
		await call.message.answer('Окей, давай разомнёмся🧠 Начнём с самого простого')
		await bot.send_photo(chat_id, open('img/qusten1.jpg', 'rb'), caption='Вопрос 1: Как ты думаешь, реально ли зарабатывать💰 на крипте?', reply_markup=kb.vopros1)
	elif 'yes' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/da1.jpg', 'rb'), caption='Отличное начало🤝 Держи пруфы\n\nто, что обведено кругом - это прибыль в $, если что')
		local_time = '1'
		cagat.sleep(int(local_time))
		await bot.send_photo(chat_id, open('img/da2.jpg', 'rb'), caption='Держи 🪙1.000 ПилaCOIN на баланс\n\nМой баланс: 🪙1.000 ПилaCOIN')
		local_time = '1'
		cagat.sleep(int(local_time))
		await bot.send_photo(chat_id, open('img/qusten2.jpg', 'rb'), caption='Поехали ко второму вопросу⏳')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Реально ли заработать на крипте с нуля 💵10к$?', reply_markup=kb.vopros2)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'NOOOOOOOO' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'))
		await bot.send_photo(chat_id, open('img/da1.jpg', 'rb'), caption='Если там зарабатывать нельзя, то как ты объяснишь такие результаты?\n\nто, что обведено кругом - это прибыль в $, если что')
		local_time = '1'
		cagat.sleep(int(local_time))
		await call.message.answer('В любом случае, это была разминка🤝 Дальше - сложнее.\n\nДержи 🪙1.000 ПилaCOIN на баланс')
		await bot.send_photo(chat_id, open('img/qusten2.jpg', 'rb'), caption='Поехали ко второму вопросу⏳')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Реально ли заработать на крипте с нуля 💵10к$?', reply_markup=kb.vopros2)
	elif 'itc' in call.data:
		await call.message.answer('Смотри, расклад такой: я готов поделиться с тобой способом, из которого ты узнаешь как с полного нуля в крипте ты можешь забрать💵 свои первые 100.000 рублей\n\nС ПОЛНОГО НУЛЯ\n\nДаже если все твои познания в крипте заканчиваются на: “ну, я знаю, что есть биток и есть эфир, и их можно продавать”, то эта информация будет для тебя ценнее, чем последний стакан🚰 воды посреди Сахары')
		await call.message.answer('Если ты хочешь продолжать оставаться на обочине и смотреть как очередной Вася🚶 со двора просто берет и поднимает какие-то бешеные проценты по сделкам, пока ты думаешь: «Да как он заработал пол мульта😡, не отрывая жопу от стула? Такого просто не может быть!», то просто выйди из чата\n\nЕсли нет, жми👇 продолжить. И мы приступим к делу', reply_markup=kb.prosto)
	elif 'dalegko' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/dalegko.jpg', 'rb'), caption='ДА!\n\nВзять, например, амбассадорские программы. Там нужно пиарить👾 криптовалютные проекты: постить контент и придумывать мемы. За это тебе могут заплатить 3-5-10к $')
		await call.message.answer('Хочешь пример?\n\nДалеко ходить не надо - достаточно взять известный🌐 проект MoonBeam\n\nТам выдавали награду от 10к до 25к$ участникам, в зависимости от их активности. Такие проекты - не исключение из правил, сейчас это сплошь и рядом')
		await call.message.answer('Поступление +1.000 ПилaCOIN\n\nМой баланс: 🪙2.000 ПилaCOIN')
		##########################3#######################
		await bot.send_photo(chat_id, open('img/qusten3.jpg', 'rb'), caption='Переходим к третьему вопросу\n\nИ сейчас тебе нужно поднапрячься🧠 и подумать. Напоминаю, у тебя 30 секунд⏳ в запасе')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько нужно учиться, чтобы поднимать на крипте 💵хотя бы 100к в месяц?', reply_markup=kb.vopros3)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'dacogr' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Да, но вероятнее всего новичок в крипте с большими вложениями в одночасье может обосраться🤝 и всё потерять\n\nЕсть более простые способы поднимать 10к $, будучи нулём в крипте. Попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Реально ли заработать на крипте с нуля 💵10к$?', reply_markup=kb.vopros2)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'novp2' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Я уже представляю твои глаза👀 по 5 копеек, когда я расскажу тебе про то, как люди без риска и вложений делают по 3-10к $\n\nДоброе утро, это будущее! И оно уже настало. Попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Реально ли заработать на крипте с нуля 💵10к$?', reply_markup=kb.vopros2)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'erthew' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Это тебе инфоцыгане🤖 сказали?\n\nВероятность того, что ты начнёшь делать стабильно 100к в месяц, будучи полным нулём в крипте, меньше, чем совесть инфоцыгана, который сказал тебе это. Хорошие результаты требуют времени. Попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько нужно учиться, чтобы поднимать на крипте 💵хотя бы 100к в месяц?', reply_markup=kb.vopros3)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'thrtefe' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='У меня для тебя отличные🤝 новости: ты неправ!\n\nЕсли ты отпишешься от всех крипто-инфоцыган и будешь потреблять только качественный📈 контент по криптовалюте, то сможешь делать первые 100к в разы быстрее. И целого года не потребуется - вот тебе подсказка. Попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько нужно учиться, чтобы поднимать на крипте 💵хотя бы 100к в месяц?', reply_markup=kb.vopros3)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'gergfwe' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/vp3.jpg', 'rb'), caption='''
Да👌, ты прав, примерно столько потребуется времени

Но ты можешь быстрее. Сейчас объясню почему: давай мы возьмём обычного человека, у которого 8-часовой рабочий день и 2-3 часа в день остаются свободны

Ему хватит месяца📆, чтобы изучить весь рынок и выбрать то направление, в котором ему будет интересно развиваться. И еще 1 месяца хватит, чтобы получить первые💵 результаты

Кстати, хочешь секрет открою? Инфоцыгане🤖 тебе такого не скажут

“Стабильности” в крипте не существует. Это тебе не завод, где начальник стабильно платит зарплату. Всё зависит от рынка. И от твоих навыков. Скажу тебе честно: бывает месяц, когда появляется куча возможностей💰 и можно поднять тонну бабла, а в следующий месяц такого может и не быть

И вообще, надо стремиться🎯 к тому, чтобы делать 100к $ в месяц, а не 10к :)
			''')
		await call.message.answer('Поступление +1.000 ПилaCOIN\n\nМой баланс: 🪙3.000 ПилaCOIN')
		await bot.send_photo(chat_id, open('img/qusten4.jpg', 'rb'), caption='Сложность вопросов увеличивается, чуешь?\n\nВопрос 4')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='С какой суммы💵 можно начать торговать? Твои 30 секунд пошли', reply_markup=kb.vopros4)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'million' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Воу-воу, потише😳. Новичку такая сумма сразу не потребуется\n\nСначала человек должен лично на маленьких суммах убедиться, что у него получается заработать на трейдинге. А только потом увеличивать сумму депозита, риски и, соответственно, прибыль. Короче, попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='С какой суммы💵 можно начать торговать? Твои 30 секунд пошли', reply_markup=kb.vopros4)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'do10k' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/do10kk.jpg', 'rb'), caption='''
Вот удивление, да?

Оказывается, чтобы стартовать в крипте, не нужно сразу вываливать миллион💲 золотых и играть на всё. Новичку необходимо начинать с небольших сумм. Я вообще не рекомендую торговать на началах больше, чем на 100$

Человек должен сначала лично убедиться на маленьких суммах, что у него получается заработать на трейдинге. А только потом увеличивать сумму депозита, риски и, соответственно, прибыль.
			''')
		await call.message.answer('Поступление +1.000 ПилaCOIN\n\nМой баланс: 🪙4.000 ПилaCOIN')
		await bot.send_photo(chat_id, open('img/qusten5.jpg', 'rb'), caption='Заключительный вопрос. Напрягись🧠')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько в среднем часов (в месяц) нужно уделять крипте? ⏳30 секунд...', reply_markup=kb.vopros5)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'uktyherthn' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Мы чё с тобой, на заводе🏭? Попробуй угадать ещё раз')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько в среднем часов (в месяц) нужно уделять крипте? ⏳30 секунд...', reply_markup=kb.vopros5)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'ktrefefmt' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/nep.png', 'rb'), caption='Да, и строго с понедельника по пятницу с 09:00 до 17:00🤝\n\nЭто тебе не офис, чтобы там 6-8 часов сидеть. Конечно, есть такие направления, как скальпинг, где можно хоть 24 часа сидеть у монитора. Но это скорее исключение из правил. Попробуй угадать ещё раз♻️')
		await bot.send_animation(chat_id, open('img/30cek.gif', 'rb'), caption='Сколько в среднем часов (в месяц) нужно уделять крипте? ⏳30 секунд...', reply_markup=kb.vopros5)
		await bot.delete_message(call.message.chat.id, call.message.message_id)
	elif 'YYYYYYYYYYYYYYYYY' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/verno.jpg', 'rb'), caption='Верно!\n\nВ среднем именно так.\n\nВсё зависит от направления, которое ты выберешь. Можно и целыми сутками🕓 быть в рынке, и заниматься всем подряд. Вопрос только в том, насколько эффективно это будет')
		await call.message.answer('+1.000 ПилaCOIN\n\nМой баланс: 🪙5.000 ПилaCOIN')
		await call.message.answer('✅5.000 из 5.000 ПилaCOIN - Ok')
		await bot.send_photo(chat_id, open('img/newlvl.jpg', 'rb'), caption='Открыт🔓 новый уровень.\n\nХочешь потратить 🪙5.000 ПилaCOIN, чтобы открыть доступ незамедлительно?', reply_markup=kb.newlevel)
	elif 'opendostyp' in call.data:
		chat_id = call.message.chat.id
		await call.message.answer('Поздравляю🎉! Ты перешёл на уровень 2')
		await bot.send_video_note(chat_id, open('img/video.mp4', 'rb'))
		await call.message.answer('Если хочешь начать разбираться🧠 в криптовалютах и научиться зарабатывать на них в текущей реальности от 100.000р, тогда жми кнопку и забирай готовое решение, которое я подготовил специально для тебя 👇🏻', reply_markup=kb.prishli)
	elif 'prishligot' in call.data:
		await call.message.answer('''
Перед тем, как я раскрою все карты, я расскажу тебе кое-что важное. Послушай

Мой опыт в качестве наставника показал мне, что самый сильный рост💰 ученики получают тогда, когда имеют на руках проверенный пошаговый план, базу с годной информацией, поддержку наставника и... еще один👾 ингредиент. Сможешь догадаться о чем я?
''', reply_markup=kb.esgefrie)
	elif 'CYKAAAAAAAA' in call.data:
		chat_id = call.message.chat.id
		await call.message.answer('Да, быстрее всего люди растут в любой теме тогда, когда окружены заряженным коммьюнити, которое двигается🏃 в одном направлении. Когда я понял это, то придумал крутую альтернативу тупым курсам по крипте и однотипным приваткам, на которых инфоцыгане🤷 делают миллионы, а студенты - сливают депозиты')
		await bot.send_photo(chat_id, open('img/comyou.jpg', 'rb'), caption='''
Я решил проверить свою гипотезу. Собрал своих студентов и объединил🤝 их в одно сильное комьюнити. Регулярно выдавал им полезный контент, делился самыми актуальными новостями про то, как заработать💵 на крипте здесь и сейчас, ограждал от скама и фейков

И... ребята начали реально расти в деньгах
''', reply_markup=kb.comzaebal)
	elif 'procomyou' in call.data:
		await call.message.answer('''
Видео обзор площадки доступен к просмотру 🔥

Смотри обзор 👇🏻
https://youtu.be/InBNmQm5JYk
			''')
		local_time = '5'
		cagat.sleep(int(local_time))
		await call.message.answer('Хочешь получить первый урок по заработку на криптовалюте из этой базы знаний бесплатно?\n\nНажми кнопку👇 и я сразу вышлю тебе доступ', reply_markup=kb.esheblya)
		


	elif 'capital1laym' in call.data:
		chat_id = call.message.chat.id
		await call.message.answer('Неа, быстрее всего люди растут в любой теме тогда, когда окружены заряженным коммьюнити, которое двигается🏃 в одном направлении. Когда я понял это, то придумал крутую альтернативу тупым курсам по крипте и однотипным приваткам, на которых инфоцыгане🤷 делают миллионы, а студенты - сливают депозиты')
		await bot.send_photo(chat_id, open('img/comyou.jpg', 'rb'), caption='''
Я решил проверить свою гипотезу. Собрал своих студентов и объединил🤝 их в одно сильное комьюнити. Регулярно выдавал им полезный контент, делился самыми актуальными новостями про то, как заработать💵 на крипте здесь и сейчас, ограждал от скама и фейков

И... ребята начали реально расти в деньгах
''', reply_markup=kb.comzaebal)



	elif 'zaebalpokypay' in call.data:
		await call.message.answer('Сударь🤝, мое уважение!\n\nПеред тем, как скину ссылку на оплату, давай я расскажу, что произойдет после этого')
		await call.message.answer('''
Оплата происходит через сервис Юкасса
Подписка стоит 10 000₽

– Переходи по ссылке
– Нажми на кнопку "Оплатить"
– Зайди в диалог с ботом и вступай в канал ☺️

После оплаты ты попадёшь в закрытый канал комьюнити. Там ты получишь доступ к обучающей платформе

Если ты находишься в России, используй карту Visa или Mastercard. Если ты сейчас заграницей - используй карту, выпущенную не в России. Кстати☝️, не забудь выключить VPN, иначе оплата не пройдет

Ты ничего не понял, у тебя возникла проблема или остались вопросы по оплате? Тогда смело обращайся🤝 в нашу поддержку. Мои ребята оперативно помогут тебе
''', reply_markup=kb.chytchet)


	elif 'PPPPPP' in call.data:
		chat_id = call.message.chat.id
		await bot.send_photo(chat_id, open('img/comyou.jpg', 'rb'), caption='''
Я решил проверить свою гипотезу. Собрал своих студентов и объединил🤝 их в одно сильное комьюнити. Регулярно выдавал им полезный контент, делился самыми актуальными новостями про то, как заработать💵 на крипте здесь и сейчас, ограждал от скама и фейков

И... ребята начали реально расти в деньгах
''', reply_markup=kb.comzaebal)
	elif 'oplata' in call.data:
		await call.message.answer('''
Держи ссылочку на оплату. И до встречи на канале!

Если ссылка перестала действовать, нажми кнопку "Обновить ссылку"

Твоя ссылка на оплату 👇🏻
https://sblnk.ru/48367566
''', reply_markup=kb.obnovit)
	elif 'polychitfree' in call.data:
		chat_id = call.message.chat.id
		
		await bot.send_photo(chat_id, open('img/pocle.jpg', 'rb'), caption='''
Урок ждет тебя по этой ссылке 👇🏻

https://t.me/max_pushkin77/144

Нажав её, тебя перекинет на мой телеграм 💸 канал. Там в закреплённом сообщении я поместил видео-урок. Только не забудь☝️ подписаться, чтобы не потерять материалы!
			''')	
		await call.message.answer('Возвращайся сюда, когда посмотришь урок🤝', reply_markup=kb.dveknopki)		
	elif 'whatiget' in call.data:
		await call.message.answer('''
Вот список👉 направлений, в которых ты начнешь зарабатывать первые деньги на крипте. Нажми на кнопку и я расскажу подробнее о каждом
''', reply_markup=kb.chetyriknopki)
	elif 'CCCCCCC' in call.data:
		await call.message.answer('''
WL (white list) - это ограниченный список людей, которые гарантировано получат NFT/доступ к бете приложения проекта.

То есть говоря совсем простым языком, WL - это возможность купить себе NFT быстрее, чем большинство пользователей.

Если выбить WL в хороших проектах, то продать его можно от 50$ до 5 000$ 🤑

Люди готовы платить такие💵 деньги, потому что понимают, что с помощью WL они заработают ещё больше! А нам это выгодно, потому что мы можем на этом заработать, не вкладывая ни копейки.

Мы дадим тебе готовый алгоритм, как находить такие проекты, как получать этот WL и где его можно продать
			''')
		await call.message.answer('Есть ещё вопросы?👇', reply_markup=kb.zadavau)
	elif 'HHHHHHHHHH' in call.data:
		await call.message.answer('''
Заработок на нодах - это, по сути, заработок без вложений. Для простоты понимания: ноды - это ранние майнеры. Представь, что ты вернулся в 2014 год и тебе бесплатно раздают биткоин. Вот это то же самое. Этот вид заработка подойдет тем, кто имеют хотя бы минимальные технические знания

Самый жирный кейс💵 был у нодраннеров SOLANA. С 1 ноды ранние участники смогли заработать от 100.000$

В среднем 1 хороший проект дает 3.000$-5.000$ (Последний кейс NYM)
Мы научим тебя как ставить и вести эти ноды. А опытные участники коммьюнити окажут тебе🤝 поддержку по любым вопросам. Так же у тебя будет доступ к тем проектам, в которых участвую лично я с командой
			''')
		await call.message.answer('Есть ещё вопросы?👇', reply_markup=kb.zadavau)
	elif 'GGGGGGGG' in call.data:
		await call.message.answer('''
Тут мы зарабатываем💰 на разнице купли-продажи

Просто пример: ты приходишь в один банк и покупаешь 10 USDT по 83 рубля. Затем идешь в другой банк и продаешь🤑 их за 87 рублей. Разница в продаже - твоя прибыль. В день можно делать 2-5 таких кругов

Скажу сразу: я не дам тебе готовую связку, где ты заработаешь🙅 дохулиард рублей. Я выдам тебе базу знаний, с которой ты сможешь зарабатывать каждый день вне зависимости от рынка стабильно 10-15% в месяц. Если научишься немного напрягать мозги в этом направлении, то сам научишься находить эти топовые связки, не привязываясь ни к кому. Моя задача научить тебя думать🧠, а не повторять

[P.S.: топовые связки и личное наставничество в этой нише стоит от 1 млн. руб]
			''')
		await call.message.answer('Есть ещё вопросы?👇', reply_markup=kb.zadavau)
	elif 'DDDDDDD' in call.data:
		await call.message.answer('''
Погружаться в это направление стоит, когда ты обрастешь💵 жирком и будешь понимать, как устроен рынок. И когда накопишь свой первый капитал для инвестирования. Такой подход поможет тебе не про%бать сразу все заработанное

Здесь я научу тебя разбираться в стратегиях📈 торговли, чтобы ты составил свою собственную, и торговал по ней. Ты узнаешь как вести агрессивную торговлю на фьючерсах и среднесрочные спотовые стратегии

Результат💰 будет зависеть от твоего капитала и упорства в обучении и практике.
Здесь нет потолка в заработке
			''')
		await call.message.answer('Есть ещё вопросы?👇', reply_markup=kb.zadavau)

@dp.message_handler(state=st.item2)
async def proc(message: types.Message, state: FSMContext):
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		await message.answer('Сообщение отправлено.', reply_markup=kb.menu)
		data = await state.get_data()
		id = data.get("uid")
		await state.finish()
		await bot.send_message(id, 'Вам поступил ответ от администратора:\n\nТекст: {}'.format(message.text))


@dp.message_handler(state=st.item)
async def process_name(message: types.Message, state: FSMContext):
	q.execute(f'SELECT user_id FROM users')
	row = q.fetchall()
	connection.commit()
	text = message.text
	if message.text == '⏪ Отмена':
		await message.answer('Отмена! Возвращаю назад.', reply_markup=kb.menu)
		await state.finish()
	else:
		info = row
		await message.answer('Рассылка начата!', reply_markup=kb.menu)
		for i in range(len(info)):
			try:
				await bot.send_message(info[i][0], str(text))
			except:
				pass
		await message.answer('Рассылка завершена!', reply_markup=kb.menu)
		await state.finish()

@dp.message_handler(state=mal.bit)
async def h(message: types.Message, state: FSMContext):
	await message.answer(f'Хорошо, {message.text}. Сейчас я расскажу тебе правила игры. Твоя задача - заработать 5.000 🪙 ПилаCOIN.', reply_markup=kb.imya)
	await state.finish()
if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)