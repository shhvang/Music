from pyrogram import Client, filters
from Core import app
from config import OWNER_ID

# Define the function to handle the @admins mention
@app.on_message(filters.group & filters.text & filters.regex(r"@admins"))
def mention_admins(client, message):
    # Get the list of admins in the group
    admins = client.get_chat_members(message.chat.id, filter="administrators")

    # Create a mention text or hyperlink for each admin
    mentions = [f"[{admin.user.first_name}](tg://user?id={admin.user.id})" for admin in admins]

    # Join the mentions with a comma separator
    mention_text = ", ".join(mentions)

    # Send the mention text as a message to the effective chat
    client.send_message(message.chat.id, mention_text)

# Define the function to handle the /air command
@app.on_message(filters.private & filters.command("air"))
def air_message(client, message):
    # Check if the user is the bot owner
    if message.from_user.id == OWNER_ID:
        # Get the chat_id and message from the command
        command_parts = message.text.split(" ", 2)
        if len(command_parts) >= 3:
            chat_id = int(command_parts[1])
            content = command_parts[2]
            # Forward or copy the message/content to the chat_id
            if message.reply_to_message:
                client.forward_messages(chat_id, message.chat.id, message.reply_to_message.message_id)
            else:
                client.send_message(chat_id, content)
        else:
            client.send_message(message.chat.id, "Invalid command syntax. Please use /air chat_id message or reply to a message with /air chat_id")
    else:
        client.send_message(message.chat.id, "You are not authorized to use this command.")