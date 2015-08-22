import asyncio
from random import randint
import requests
from bs4 import BeautifulSoup
import plugins


def _initialise(bot):
    plugins.register_handler(_handle_me_action)
    plugins.register_user_command(["diceroll", "coinflip", "joke", "tod", "magicball", "bane"])


def _handle_me_action(bot, event, command):
    if event.text.startswith('/me'):
        if event.text.find("roll dice") > -1 or event.text.find("rolls dice") > -1 or event.text.find("rolls a dice") > -1 or event.text.find("rolled a dice") > -1:
            yield from asyncio.sleep(0.2)
            yield from command.run(bot, event, *["diceroll"])
        elif event.text.find("flips a coin") > -1 or event.text.find("flips coin") > -1 or event.text.find("flip coin") > -1 or event.text.find("flipped a coin") > -1:
            yield from asyncio.sleep(0.2)
            yield from command.run(bot, event, *["coinflip"])
        else:
            pass

			
def diceroll(bot, event, *args):
    """roll a dice"""
    yield from bot.coro_send_message(event.conv, _("<i>{} rolled <b>{}</b></i>").format(event.user.full_name, randint(1,6)))
 
def tod(bot, event, *args):
	t = requests.Session()
	url = 'http://www.truthordare.us/random'
	response = t.get(url)
	soup = BeautifulSoup(response.content)
	tod = soup.find("div", {"id": "tdboxtext"}).text
	yield from bot.coro_send_message(event.conv, _(tod))
 
 
def coinflip(bot, event, *args):
    """flip a coin"""
    if randint(1,2) == 1:
        yield from bot.coro_send_message(event.conv, _("<i>{}, coin turned up <b>heads</b></i>").format(event.user.full_name))
    else:
        yield from bot.coro_send_message(event.conv, _("<i>{}, coin turned up <b>tails</b></i>").format(event.user.full_name))
 
 
def magicball(bot, event, *args):
    """shake 8 ball"""
    Shake = randint(1,20)
    if Shake == 1:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Yes</b></i>").format(event.user.full_name))
    elif Shake == 2:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>No</b></i>").format(event.user.full_name))
    elif Shake == 3:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>It is certain</b></i>").format(event.user.full_name))
    elif Shake == 4:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>It is decidedly so</b></i>").format(event.user.full_name))
    elif Shake == 5:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Yes definitely</b></i>").format(event.user.full_name))
    elif Shake == 6:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>You may rely on it</b></i>").format(event.user.full_name))
    elif Shake == 7:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>As I see it, yes</b></i>").format(event.user.full_name))
    elif Shake == 8:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Most likely</b></i>").format(event.user.full_name))
    elif Shake == 9:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Outlook good</b></i>").format(event.user.full_name))
    elif Shake == 10:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Signs point to yes</b></i>").format(event.user.full_name))
    elif Shake == 11:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Reply hazy try again</b></i>").format(event.user.full_name))
    elif Shake == 12:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Ask again later</b></i>").format(event.user.full_name))
    elif Shake == 13:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b><Better not tell you now/b></i>").format(event.user.full_name))
    elif Shake == 14:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Cannot predict now</b></i>").format(event.user.full_name))
    elif Shake == 15:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Concentrate and ask again</b></i>").format(event.user.full_name))
    elif Shake == 16:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Don't count on it</b></i>").format(event.user.full_name))
    elif Shake == 17:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>My reply is no</b></i>").format(event.user.full_name))
    elif Shake == 18:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>My sources say no</b></i>").format(event.user.full_name))
    elif Shake == 19:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Outlook not so good</b></i>").format(event.user.full_name))
    elif Shake == 20:
        yield from bot.coro_send_message(event.conv, _("<i>{},<b>Very doubtful</b></i>").format(event.user.full_name))
		

def joke(bot, event, *args):
	c = requests.Session()
	url = 'http://theoatmeal.com/djtaf/'
	response = c.get(url)
	soup = BeautifulSoup(response.content)
	jokeline = soup.find("h2", {"class": "part1"}).text
	punchline = soup.find("h2", {"class": "part2"}).text
	yield from bot.coro_send_message(event.conv, _(jokeline))
	yield from bot.coro_send_message(event.conv, _(punchline))	
