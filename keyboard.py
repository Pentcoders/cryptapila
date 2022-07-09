from aiogram import types



menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('💬 Рассылка')
)

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('⏪ Отмена')
)


def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='💬 Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='❎ Удалить', callback_data='ignor')
    )
    return quest
###############################################################################################################################
berkn = types.InlineKeyboardMarkup(row_width=1)
berkn.add(
    types.InlineKeyboardButton(text='[объясни правила]', callback_data='obpr'),
    types.InlineKeyboardButton(text='[игру? ты серьезно?]', callback_data='itc'),
    )

imya = types.InlineKeyboardMarkup(row_width=1)
imya.add(
    types.InlineKeyboardButton(text='[посмотреть баланс]', callback_data='balanc'),
    )

play = types.InlineKeyboardMarkup(row_width=1)
play.add(
    types.InlineKeyboardButton(text='[Играть]', callback_data='playing'),
    )

person = types.InlineKeyboardMarkup(row_width=1)
person.add(
    types.InlineKeyboardButton(text='[фрилансер]', callback_data='naemrab'),
    types.InlineKeyboardButton(text='[наемный рабочий]', callback_data='naemrab'),
    types.InlineKeyboardButton(text='[начинающий в крипте]', callback_data='naemrab'),
    )

age = types.InlineKeyboardMarkup(row_width=1)
age.add(
    types.InlineKeyboardButton(text='[до 18 лет]', callback_data='ages'),
    types.InlineKeyboardButton(text='[18-23 года]', callback_data='ages'),
    types.InlineKeyboardButton(text='[24-30 лет]', callback_data='ages'),
    types.InlineKeyboardButton(text='[более 30 лет]', callback_data='ages'),
    )

vopros1 = types.InlineKeyboardMarkup(row_width=1)
vopros1.add(
    types.InlineKeyboardButton(text='[да]', callback_data='yes'),
    types.InlineKeyboardButton(text='[нет]', callback_data='NOOOOOOOO'),
    )

vopros2 = types.InlineKeyboardMarkup(row_width=1)
vopros2.add(
    types.InlineKeyboardButton(text='[да, с огромными вложениями]', callback_data='dacogr'),
    types.InlineKeyboardButton(text='[нет]', callback_data='novp2'),
    types.InlineKeyboardButton(text='[да, легко]', callback_data='dalegko'),
    )

prosto = types.InlineKeyboardMarkup(row_width=1)
prosto.add(
    types.InlineKeyboardButton(text='[заебал, покупаю]', callback_data='zaebalpokypay'),
    types.InlineKeyboardButton(text='[продолжить]', callback_data='obpr'),
    )

vopros3 = types.InlineKeyboardMarkup(row_width=1)
vopros3.add(
    types.InlineKeyboardButton(text='[1-2 недели]', callback_data='erthew'),
    types.InlineKeyboardButton(text='[от года]', callback_data='thrtefe'),
    types.InlineKeyboardButton(text='[3 месяца]', callback_data='gergfwe'),
    )

vopros4 = types.InlineKeyboardMarkup(row_width=1)
vopros4.add(
    types.InlineKeyboardButton(text='[от 1 000 000 рублей]', callback_data='million'),
    types.InlineKeyboardButton(text='[от 300-500к рублей]', callback_data='million'),
    types.InlineKeyboardButton(text='[до 10к рублей]', callback_data='do10k'),
    )

vopros5 = types.InlineKeyboardMarkup(row_width=1)
vopros5.add(
    types.InlineKeyboardButton(text='[6-8 часов/день]', callback_data='ktrefefmt'),
    types.InlineKeyboardButton(text='[10-12 часов/день]', callback_data='uktyherthn'),
    types.InlineKeyboardButton(text='[до 3 часов/день]', callback_data='YYYYYYYYYYYYYYYYY'),
    )

newlevel = types.InlineKeyboardMarkup(row_width=1)
newlevel.add(
    types.InlineKeyboardButton(text='[открыть доступ]', callback_data='opendostyp'),
    )

prishli = types.InlineKeyboardMarkup(row_width=1)
prishli.add(
    types.InlineKeyboardButton(text='[пришли готовое решение]', callback_data='prishligot'),
    )

esgefrie = types.InlineKeyboardMarkup(row_width=1)
esgefrie.add(
    types.InlineKeyboardButton(text='[сильное коммьюнити]', callback_data='CYKAAAAAAAA'),
    types.InlineKeyboardButton(text='[капитал +1 млн руб.]', callback_data='capital1laym'),
    types.InlineKeyboardButton(text='[базу полезных связей]', callback_data='capital1laym'),
    )


comzaebal = types.InlineKeyboardMarkup(row_width=1)
comzaebal.add(
    types.InlineKeyboardButton(text='[расскажи про коммьюнити]', callback_data='procomyou'),
    types.InlineKeyboardButton(text='[покупаю, заебал]', callback_data='zaebalpokypay'),
    )

chytchet = types.InlineKeyboardMarkup(row_width=1)
chytchet.add(
    types.InlineKeyboardButton(text='[вернуться обратно]', callback_data='PPPPPP'),
    types.InlineKeyboardButton(text='[перейти к оплате]', callback_data='oplata'),
    types.InlineKeyboardButton(text='[задать вопрос в поддержку]', url='https://t.me/pushnila_support'),
    )

obnovit = types.InlineKeyboardMarkup(row_width=1)
obnovit.add(
    types.InlineKeyboardButton(text='[Обновить ссылку]', callback_data='oplata'),
    )

esheblya = types.InlineKeyboardMarkup(row_width=1)
esheblya.add(
    types.InlineKeyboardButton(text='[получить бесплатный урок]', callback_data='polychitfree'),
    types.InlineKeyboardButton(text='[хочу вступить]', callback_data='zaebalpokypay'),
    )

dveknopki = types.InlineKeyboardMarkup(row_width=1)
dveknopki.add(
    types.InlineKeyboardButton(text='[что я получу в итоге?]', callback_data='whatiget'),
    types.InlineKeyboardButton(text='[хочу вступить]', callback_data='zaebalpokypay'),
    )

chetyriknopki = types.InlineKeyboardMarkup(row_width=1)
chetyriknopki.add(
    types.InlineKeyboardButton(text='[NFT и продажа Вайтлистов]', callback_data='CCCCCCC'),
    types.InlineKeyboardButton(text='[NODES]', callback_data='HHHHHHHHHH'),
    types.InlineKeyboardButton(text='[Арбитраж крипты]', callback_data='GGGGGGGG'),
    types.InlineKeyboardButton(text='[Трейдинг/инвестиции]', callback_data='DDDDDDD'),
    )

zadavau = types.InlineKeyboardMarkup(row_width=1)
zadavau.add(
    types.InlineKeyboardButton(text='[еще вопрос]', callback_data='whatiget'),
    types.InlineKeyboardButton(text='[хочу вступить]', callback_data='zaebalpokypay'),
    )