class script(object):
    START_TXT = """Hey {}\n\n<b>Welcome to Movie Search Bot</b>

<b>I can provide Movies. A Telegram Auto Filter Bot. Its Easy To Use Me :)

Just Add me to Your Group As Admin, Hit The Help Button For More Info..

โจ ๐๐๐ข๐ง๐ญ๐๐ข๐ง๐๐ ๐๐ฒ :  <a href='https://t.me/PM_Bots'>๐ฃ๐  ๐๐ผ๐๐</a> </b>"""
"""
    HELP_TXT = """Hey {}
Here is the Help of Commands"""
    ABOUT_TXT = """<b>๐ฅฑ My Name : see my name on the top
๐ตโโ Developer : <a href='https://t.me/vadivel_da'>๐๐ฎ๐ฑ๐ถ๐๐ฒ๐น ๐ฑ๐ฎ</a>
๐ Library : ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ
๐ฅ Language : ๐ฟ๐๐๐ท๐พ๐ฝ ๐น
๐ช Data Base : ๐ผ๐พ๐ฝ๐ถ๐พ ๐ณ๐ฑ
๐ Updates : @PM_Bots </b>"""
    SOURCE_TXT = """Vaa Arunachalam ne varuva nu theriyum๐"""
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
    CONNECTION_TXT = """Sorry, Admin can Access This๐"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of MSP x Filter

<b>Commands and Usage:</b>
โข /id - <code>get id of a specified user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ Total Files: <code>{}</code>
โ Total Users: <code>{}</code>
โ Total Chats: <code>{}</code>
โ Used Storage: <code>{}</code> ๐ผ๐๐ฑ
โ Free Storage: <code>{}</code> ๐ผ๐๐ฑ"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
