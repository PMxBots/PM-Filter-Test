class script(object):
    START_TXT = """Hey {}\n\n<b>Welcome to Movie Search Bot</b>

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..

✨ 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 :  <a href='https://t.me/PM_Bots'>𝗣𝗠 𝗕𝗼𝘁𝘀</a> </b>"""
"""
    HELP_TXT = """Hey {}
Here is the Help of Commands"""
    ABOUT_TXT = """<b>🥱 My Name : see my name on the top
🕵‍♂ Developer : <a href='https://t.me/vadivel_da'>𝘃𝗮𝗱𝗶𝘃𝗲𝗹 𝗱𝗮</a>
📚 Library : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
🖥 Language : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
🎪 Data Base : 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
🔋 Updates : @PM_Bots </b>"""
    SOURCE_TXT = """Vaa Arunachalam ne varuva nu theriyum😎"""
    MANUELFILTER_TXT = """For Help contact @PMxPGVbot"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Movie Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Movie Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/PM_Moviebot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Sorry, Admin can Access This😒"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of MSP x Filter

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code> 𝙼𝚒𝙱
★ Free Storage: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
