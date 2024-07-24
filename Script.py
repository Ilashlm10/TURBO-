class script(object):
    START_TXT = """Hey there! I'm your advanced auto filter bot 🤖\nFast and efficient at your service! ⚡️\nLet's keep this chat clean and enjoyable 🚀\nFeel free to ask for help anytime! 🙌"""
    HELP_TXT = """<b>Hᴇʏ {}
Hᴇʀᴇ Is Tʜᴇ Hᴇʟᴘ Fᴏʀ Mʏ Cᴏᴍᴍᴀɴᴅs.</b>"""
    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ: {}
✯ Cʀᴇᴀᴛᴏʀ: <a href='https://t.me/creatorbeatz'>Jᴏᴇʟ Kᴜʀɪᴀɴ Bɪᴊᴜ</a>
✯ Lɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>
✯ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/download/releases/3.0/'>Pʏᴛʜᴏɴ 3</a>
✯ DᴀᴛᴀBᴀsᴇ: <a href='https://www.mongodb.com/'>MᴏɴɢᴏDB</a>
✯ Bᴏᴛ Sᴇʀᴠᴇʀ: <a href='https://app.koyeb.com/'>Kᴏʏᴇʙ</a>
✯ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: v2.7.1 [ Sᴛᴀʙʟᴇ ]</b>"""

    SOURCE_TXT = """ • <h1><u>Thanks To</u></h1>\n • Thanks To Dan For His Awesome [Library](https://github.com/pyrogram/pyrogram)\n • Thanks To Mahesh For His Awesome [Media-Search-bot](https://github.com/Mahesh0253/Media-Search-bot)\n • Thanks To [Trojanz](https://github.com/trojanzhex) for Their Awesome [Unlimited Filter Bot](https://github.com/TroJanzHEX/Unlimited-Filter-Bot) And [AutoFilterBoT](https://github.com/trojanzhex/auto-filter-bot)\n • Thanks To All Everyone In This Journey\n• Thanks To [EvamariaTG](https://raw.githubusercontent.com/EvamariaTG) for their awesome [EvaMaria Bot](https://raw.githubusercontent.com/EvamariaTG/EvaMaria)\n • Thanks To Me 😂\n• <h1><u>Main Editors</u></h1>\n
 • <a href='tg://user?id=1951205538'>༒ᶜʳᵃᶻʸᴮᴼˢˢ卂乃卄丨丂卄乇Ҝ༒</a>
 • <a href='tg://user?id=1177577143'>Jᴏᴇʟ ᠰ TɢX</a> """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/mflinkzbot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of this bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """➥ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴜsᴇʀs</b>: <i>{}</i>
➥ <b>ᴛᴏᴛᴀʟ ᴄʜᴀᴛs</b>: <i>{}</i>
➥ <b>ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> 
➥ <b>ғʀᴇᴇ sᴛᴏʀᴀɢᴇ</b>: <i>{}</i> """
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    CUSTOM_FILE_CAPTION = """<b>📂Fɪʟᴇɴᴀᴍᴇ : <code>{file_name}</code>

╔═════•✧❅✦❅✧•═════╗
▣ <a href=https://t.me/cinemaworld_123>​𝙲𝙸𝙽𝙴𝙼𝙰 𝚆𝙾𝚁𝙻𝙳</a>
▣ <a href=t.me/cinemaworld_update>𝙲𝙸𝙽𝙴𝙼𝙰 𝚆𝙾𝚁𝙻𝙳 𝚄𝙿𝙳𝙰𝚃𝙴𝚂​</a>
╚═════•✧❅✦❅✧•═════╝</b>"""
    CREDIT_INFO = """
      <b>⍟───[ Cʀᴇᴅɪᴛꜱ ]───⍟</b>   
𝖳𝗁𝖺𝗇𝗄 𝖳𝗈 : <a href=https://github.com/EvamariaTG>Eᴠᴀ ᴍᴀʀɪᴀ​</a>
𝖢𝗈𝖽𝖾𝖽 𝖡𝗒 : <a href=https://t.me/movieman_22>тнє мαη</a>
𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝖽 𝖡𝗒 : <a href=https://t.me/Leomessi_10_19>ʟᴇᴏ ᴍᴇꜱꜱɪ</a>
𝖥𝖾𝖺𝗍𝗎𝗋𝖾 𝖠𝖽𝖽𝖾𝖽 𝖡𝗒 : <a href=t.me/CINEMAWORLD_UPDATE>𝙲𝙸𝙽𝙴𝙼𝙰 𝚆𝙾𝚁𝙻𝙳</a>

       <b>⍟───[ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇꜱ]───⍟</b>
𝗌𝗈𝗎𝗋𝖼𝖾 𝖼𝗈𝖽𝖾 : <a href=https://t.me/movieman_22>тнє мαη 😶‍🌫️</a>
𝖥𝗈𝗋𝗄𝖾𝖽 𝖿𝗋𝗈𝗆 : <a href=https://t.me/Leomessi_10_19>Asᴋ ʜɪᴍ 💻</a>

       <b>⍟───[Mᴀɪɴʟʏ Eᴅɪᴛᴛᴇᴅ]───⍟</b>
𝖬𝖺𝗂𝗇𝗅𝗒 𝖤𝖽𝗂𝗍𝗍𝖾𝖽 𝖡𝗒 : <a href=https://t.me/movieman_22>тнє мαη</a>
𝖲𝗉𝖾𝖼𝗂𝖺𝗅 𝖳𝗁𝖺𝗇𝗄𝗌 𝖳𝗈 : <a href=https://t.me/Leomessi_10_19>ʟᴇᴏ ᴍᴇꜱꜱɪ</a>"""   
    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
• ꜰᴜʟʟ ɴᴀᴍᴇ : ʟᴇᴏ ᴍᴇꜱꜱɪ
• ᴜꜱᴇʀɴᴀᴍᴇ : @Leomessi_10_19 
• ᴘᴇʀᴍᴀɴᴇɴᴛ ᴅᴍ ʟɪɴᴋ : <a href='t.me/Leomessi_10_19'>ʟᴇᴏ ᴍᴇꜱꜱɪ</a></b>"""
    ALL_FILTERS = """
<b>Hᴇʏ {}, Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
    GROUP_INFO = """
<b>⍟ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs Mᴏᴅᴜʟᴇ ⍟</b>
🎬 Cᴏᴍᴘʟᴇᴛᴇ Mᴏᴠɪᴇ Rᴇǫᴜᴇsᴛɪɴɢ Gʀᴏᴜᴘ.
🚦 Aʟʟ Lᴀɴɢᴜᴀɢᴇs Mᴏᴠɪᴇs & Sᴇʀɪᴇs.
🗣️ Bᴏᴛ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ.
📢 Bᴏᴛ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ."""
    
