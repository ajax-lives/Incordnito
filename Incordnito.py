# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: Incordnito.py
# Bytecode version: 3.6rc1 (3379)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import requests
from discord_webhook import *
from guizero import *
from cryptography.fernet import Fernet
from discord.ext import commands
import threading
import tkinter as tk
import discord
import time
import os.path
from os import path
import zipfile

def doNothing():
    return

def sleepy():
    app.destroy()

def cogDL():
    cogURL = 'https://raw.githubusercontent.com/Munchacho/Incordnito/master/cog.png'
    getCOG = requests.get(cogURL)
    downloadCOG = open('bin/cog.png', 'wb')
    downloadCOG.write(getCOG.content)

def bgDL():
    bgURL = 'https://raw.githubusercontent.com/Munchacho/Incordnito/master/background.png'
    getBG = requests.get(bgURL)
    downloadBG = open('bin/background.png', 'wb')
    downloadBG.write(getBG.content)
version = 1.3
print(version)
url = 'https://pastebin.com/raw/2nqKTEjj'
VersionServer = requests.request('GET', url).text
VersionServer = float(VersionServer)
print(VersionServer)
if path.exists('bin/'):
    doNothing()
else:
    os.mkdir('bin/')
try:
    whLink = open('bin/link.txt', 'r')
    Link = whLink.read()
except:
    linkFile = open('bin/link.txt', 'w+')
    linkFile.write('PUT YOUR CHANNEL WEBHOOK LINK IN THIS TEXT FILE!')
    linkFile.close()
app = App(title=f'Incordnito V{version}0', bg=(34, 34, 34))
app.full_screen = False
settings = Window(app, title='Settings', width=340, height=50)
settings.bg = (34, 34, 34)
settings.hide()
settings.full_screen = False
missingContent = Window(app, title='Missing Files', width=500, height=25)
missingContent.bg = (34, 34, 34)
missingContent.hide()
missingContent.full_screen = False
missingText = Text(missingContent, color='white', text='Your missing files have been downloaded, please restart Incordnito.')
firstRun = Window(app, title='Instructions', width=750, height=25)
firstRun.bg = (34, 34, 34)
firstRun.hide()
firstRun.full_screen = False
firstRunText = Text(firstRun, color='white', text="This is your first time running Incordnito, please read 'instructions.txt' if need be!  Enjoy!")
firstRunText.text_color = 'white'

def getInstructions():
    inURL = 'https://raw.githubusercontent.com/Munchacho/Incordnito/master/Instructions.txt'
    getIN = requests.get(inURL)
    downloadIN = open('Instructions.txt', 'wb')
    downloadIN.write(getIN.content)
if path.exists('bin/runCount.txt'):
    doNothing()
else:
    firstRun.show()
    getInstructions()

def die():
    app.destroy()
if version < VersionServer:
    urlDL = f'https://github.com/Munchacho/Incordnito/releases/download/{VersionServer}0/Incordnito.exe'
    download = requests.request('GET', urlDL)
    pp = open(f'Incordnito-{VersionServer}.exe', 'wb').write(download.content)
    UpdateAvailable = Window(app, title='Update Available!', width=600, height=75)
    UpdateAvailable.bg = (34, 34, 34)
    UpdateText = Text(UpdateAvailable, color='white', text='There is a new update for Incordnito!')
    UpdateText2 = Text(UpdateAvailable, color='white', text=f"It is labeled 'Incordnito-{VersionServer}0.exe' inside your Incordnito folder!")
    UpdateText3 = Text(UpdateAvailable, color='white', text='This program will close in 10 seconds, please use the newest version.')
    UpdateText3.tk.after(10000, die)
try:
    picture = tk.PhotoImage(file='bin/background.png')
    background_label = tk.Label(image=picture)
    background_label.place(relwidth=1, relheight=1)
except:
    bgDL()
    app.hide()
    missingContent.show()
    missingContent.after(5000, sleepy)
keyBox = TextBox(settings, width=55)
keyBox.text_color = 'white'

def genKey():
    key = Fernet.generate_key()
    key = key.decode()
    keyFile = open('bin/key.txt', 'w+')
    keyFile.write(key)
    keyFile.read()
    keyBox.append(key)
    keyFile.close()

def OpenSettings():
    settings.show()
if path.exists('bin/nickname.txt'):
    doNothing()
else:
    nickFile = open('bin/nickname.txt', 'w+')
    nickFile.write('Default Nickname')
    nickFile.close()
try:
    Settings = PushButton(app, height=24, width=24, text='Settings', command=OpenSettings, align='bottom', image='bin/cog.png')
    Settings.text_color = 'white'
except:
    cogDL()
    app.hide()
    missingContent.show()
    missingContent.after(5000, sleepy)
keyGen = PushButton(settings, width='fill', height=1, text='Generate Key', command=genKey)
keyGen.text_color = 'white'
keyFileOpen = open('bin/key.txt', 'r')
key = keyFileOpen.read()
keyBox.value = key
jeff = key
nameTextFile = open('bin/nickname.txt', 'r')
nickname = nameTextFile.read()
nameTextFile.close()
chatBox = TextBox(app, height=25, width=55, multiline=True)
chatBox.bg = (44, 44, 44)
chatBox.text_color = (255, 255, 255)
chatBox.value = ''
space3 = Text(app, height=1)
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_message(message):
    msg = message.content
    msg2decry = bytes(msg, 'utf-8')
    f = Fernet(jeff)
    token = f.decrypt(msg2decry)
    token = token.decode('utf-8')
    token = token.replace('\n', '')
    chatBox.append(token)
    chatBox.tk.see('end')
    sendBox.value = ''
    await bot.process_commands(message)
sendBox = TextBox(app, multiline=True)
sendBox.width = 55
sendBox.bg = (44, 44, 44)
sendBox.text_color = (255, 255, 255)
sendBox.focus()
value = sendBox.value
pp = True
if '\n' in value:
    sendBox.height += 1

def focusPls():
    nigerian = True
    while nigerian == True:
        if settings.visible == False:
            sendBox.focus()
            time.sleep(0.1)

def hook(event):
    f = Fernet(bytes(jeff, 'utf-8'))
    msg = f'<{nickname}0> ' + sendBox.value
    msg = msg.replace('\n', '')
    msg = bytes(msg, 'utf-8')
    gold = f.encrypt(msg)
    decode = gold.decode()
    webhook = DiscordWebhook(url=Link, content=decode)
    response = webhook.execute()
    sendBox.value = ''
sendBox.tk.bind('<Return>', hook)

def runBot():
    bot.run('')

def doThread(event):
    chatThread = threading.Thread(target=runBot)
    chatThread.daemon = True
    chatThread.start()
doThread(event)

def stayFocused(event):
    focusThread = threading.Thread(target=focusPls)
    focusThread.daemon = True
    focusThread.start()
stayFocused(event)
App.display(app)