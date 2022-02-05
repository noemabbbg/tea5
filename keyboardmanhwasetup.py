from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
btnreturnmenu=InlineKeyboardButton(text='вернуться в меню', callback_data='returnMenu')




clava18=InlineKeyboardMarkup(row_width=5)
buy_pear2 = InlineKeyboardButton(text="убийца героев", callback_data="HeroKiller")
hent1 = InlineKeyboardButton(text="я забыл название но оно работает", callback_data="хент1")
clava18.insert(hent1)

clavaTOP = InlineKeyboardMarkup(row_width=1)
buy_pear3 = InlineKeyboardButton(text="поднятие уровня в одиночку", callback_data="Solo")
buy_pear4 = InlineKeyboardButton(text="Большая жизнь", callback_data="BigLife")
buy_pear11 = InlineKeyboardButton(text="убийца героев", callback_data="HeroKiller")
buy_pear12 = InlineKeyboardButton(text="Элисед", callback_data="Eliced")

SCB=InlineKeyboardButton(text="SuicideBoy", callback_data="SuicideBoy")
box = InlineKeyboardButton(text="Боксер", callback_data="Boxer")
clavaTOP.insert(box)
clavaTOP.insert(SCB)
clavaTOP.insert(buy_pear12)
clavaTOP.insert(btnreturnmenu)