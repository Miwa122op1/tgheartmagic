from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import sleep
import emoji, random, function

MAP = {
'HEART': '''
01111011110
11111111111
11111111111
01111111110
00111111100
00011111000
00001110000
00000100000
''',
'MATRIX': '''
01010101010
10101010101
01010101010
10101010101
01010101010
10101010101
01010101010
10101010101
01010101010
10101010101
01010101010
'''}
redemoji='❤️'
emoji = ['💚', '💙', '💜', '🖤', '🤍', '🤎',]
def generate_parade_colored(RARADE_MAP):
    output = ''
    for c in RARADE_MAP:
        if c == '0':
            output += redemoji
        elif c == '1':
            output += random.choice(emoji)
        else:
            output += c
    return output
app = Client(
    "my_account",
    api_id=20530777,
    api_hash="ad85d8b5306bef340ec044ba3bace8b5"
)

time_sleep = 0.300  # cooldown between frames
time_animat = 0.250
messagesend = [
'П ',
'Пр',
'Про',
'Прос',
'Проси',
'Просил',
'Просили',
'Просили п',
'Просили пе',
'Просили пер',
'Просили пере',
'Просили перед',
'Просили переда',
'Просили передат',
'Просили передать',
'Просили передать:',
'Просили передать: %s']

@app.on_message(filters.command("matrix", prefixes="") & filters.me)
def test(_, message):
    sendend = random.choice(emoji) + \
        random.choice(emoji) + \
        random.choice(emoji) + \
       "%s" + \
        random.choice(emoji) + \
        random.choice(emoji) + \
        random.choice(emoji)
    for i in range(0,12):
        send = generate_parade_colored(MAP['MATRIX'])
        message.edit(send)
        sleep(time_sleep)
    sleep(0.500)
    for i in messagesend:
        sending = i
        if sending == 'Просили передать: %s':
            sending = i % message.text.split(" ",maxsplit = 1)[1]
        message.edit(sendend % sending)
        sleep(time_animat)
@app.on_message(filters.command("heart", prefixes="") & filters.me)
def test(_, message):
    sendend = random.choice(emoji) + \
        random.choice(emoji) + \
        random.choice(emoji) + \
       "%s" + \
        random.choice(emoji) + \
        random.choice(emoji) + \
        random.choice(emoji)
    for i in range(0,12):
        send = generate_parade_colored(MAP['HEART'])
        message.edit(send)
        sleep(time_sleep)
    sleep(0.500)
    for i in messagesend:
        sending = i
        if sending == 'Просили передать: %s':
            sending = i % message.text.split(" ",maxsplit = 1)[1]
        message.edit(sendend % sending)
        sleep(time_animat)
@app.on_message(filters.regex("сердечки"))
async def hearting(_,message):
    await function.heart(_,message)
if __name__ == '__main__':
    print('[+] Connect succes')
    app.run()
    