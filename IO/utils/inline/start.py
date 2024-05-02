from pyrogram.types import InlineKeyboardButton

import config
from Core import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Recruit Me", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="Recruit Me", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="Modules", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="Developer", user_id=config.OWNER_ID),
        ]
    ]
    return buttons
