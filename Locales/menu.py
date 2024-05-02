ADMIN_COMMANDS = """
<b>Admin Module</b>

<blockquote>Some functions might need the bot to have certain admin rights</blockquote>

<b>──「 Resume/Pause 」──</b>
<b>-></b> /pause or /resume - <i>Pause or Resume stream the ongoing stream</i>

<b>──「 Skip/Loop 」──</b>
<b>-></b> /skip - <i>Skip the ongoing stream</i>
<i>Additional Argument -</i> <code>Number</code> - <i>Skips the given number of tracks</i>
<b>-></b> - /loop <code>Number</code> - <i>Loop the current stream</i>

<b>──「 End/Stop 」──</b>
<b>-></b> /end or /stop - <i>End the ongoing stream and clear all the tracks</i>

<b>──「 Speed 」──</b>
<b>-></b> /speed - <i>Adjust the playback speed of the ongoing stream</i>
<b>-></b> /cspeed - <i>Adjust the playback speed of the ongoing stream in channel</i>
"""
SUDO_COMMANDS = """
<b>Sudo Module</b>

<blockquote>Includes all the admin functions</blockquote>

<b>──「 Broadcast 」──</b>
<b>-></b> /broadcast - <i>Broadcast a message to all the chats</i>
<i>Additional Arguments -</i>
<b>-</b> <code>pin</code> - <i>Pins the broadcasted message</i>
<b>-</b> <code>pinloud</code> - <i>Pins the broadcasted message with notification</i>
<b>-</b> <code>user</code> - <i>Broadcasts the message to users who have started the bot</i>
<b>-</b> <code>assistant</code> - <i>Broadcast your message from the assistant account of the bot</i>
<b>-</b> <code>nobot</code> - <i>Forces the bot to not broadcast the message</i>

<b>──「 Chat Blacklist 」──</b>
<b>-></b> /blacklistchat - <i>Blacklist a chat</i>
<b>-></b> /whitelistchat - <i>Whitelist a chat</i>
<b>-></b> /blacklistedchat - <i>Shows the list of blacklisted chats</i>

<b>──「 Block Users 」──</b>
<b>-></b> /block - <i>Block a user</i>
<b>-></b> /unblock - <i>Unblock a user</i>
<b>-></b> /blockedusers - <i>Shows the list of blocked users</i>

<b>──「 Global Ban 」──</b>
<b>-></b> /gban - <i>Globally ban a user</i>
<b>-></b> /ungban - <i>Globally unban a user</i>
<b>-></b> /gbannedusers - <i>Shows the list of globally banned users</i>

<b>──「 Maintenance 」──</b>
<b>-></b> /logs - <i>Get logs of the bot</i>
<b>-></b> /logger - <i>Enable/disable logging</i>
<b>-></b> /maintenance - <i>Enable/disable maintenance mode</i>
"""

USER_COMMANDS = """
<b>User Module</b>

<blockquote>Includes all the user functions</blockquote>

<b>──「 Play 」──</b>
<b>-></b> /play - <i>Starts streaming the requested track in VC</i>
<b>-></b> /vplay - <i>Streams the requested video track in VC</i>
<b>-></b> /playforce - <i>Stops the ongoing stream and plays the requested track in VC</i>

<b>──「 Channel Play 」──</b>
<b>-></b> /cplay - <i>Plays the requested track in Channel's VC</i>
<b>-></b> /cvplay - <i>Streams the requested video track in Channel's VC</i>
<b>-></b> /cplayforce - <i>Stops the ongoing stream and plays the requested track in Channel's VC</i>
<b>-></b> /channelplay - <i>Connect channel to a group and start playing tracks from the group</i>

<b>──「 Song Download 」──</b>
<b>-></b> /song - <i>Download any track from youtube in mp3/mp4 format</i>

<b>──「 Queue 」──</b>
<b>-></b> /queue - <i>Shows the queue</i>
"""