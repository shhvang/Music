from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from Core import app
from IO.utils import help_pannel
from IO.utils.database import get_lang
from IO.utils.decorators.language import LanguageStart, languageCB
from IO.utils.inline.menu import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMAGE, SUPPORT_CHAT
from Locales import get_string, menu


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(client: app, update: Union[types.Message, types.CallbackQuery]):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format("https://t.me/IOSupportChat"), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMAGE,
            caption=_["help_1"].format("https://t.me/IOSupportChat"),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "admin":
        await CallbackQuery.edit_message_text(menu.ADMIN_COMMANDS, reply_markup=keyboard)
    elif cb == "sudo":
        await CallbackQuery.edit_message_text(menu.SUDO_COMMANDS, reply_markup=keyboard)
    elif cb == "user":
        await CallbackQuery.edit_message_text(menu.USER_COMMANDS, reply_markup=keyboard)