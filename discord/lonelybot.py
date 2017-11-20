import discord
import asyncio
import random
from discord.ext.commands import Bot
import helper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

lonely = Bot(command_prefix="^")

@lonely.event
async def on_ready():
	print("client logged in")

@lonely.command()
async def waifu(*args):
	if (len(args) == 0):
		search = "holo"
	else:
		search = helper.convertSearch(args)

	message = "Here's a waifu, you weeby fuck: "

	soup = helper.getSoup("http://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags={}&ms=1".format(search))

	urls = []
	for link in soup.find_all('img'):
	    urls.append(link.parent.get('href'))

	if (len(urls) == 0):
		return await lonely.say("No results. Your waifu is shit.")

	soup = helper.getSoup('http://danbooru.donmai.us/' + random.choice(urls))
	for link in soup.find_all('img'):
	    return await lonely.say(message + 'http://danbooru.donmai.us' + str(link.get('src')))

@lonely.command()
async def judge(*args):
	return await lonely.say("ಠ_ಠ ")
@lonely.command()
async def shrug(*args):
	return await lonely.say("¯\_(ツ)_/¯ ")
@lonely.command()
async def fite(*args):
	return await lonely.say("(ง'̀-'́)ง")
@lonely.command()
async def lobster(*args):
	return await lonely.say("(/) (°,,°) (/)")
@lonely.command()
async def angry(*args):
	return await lonely.say("{(>_<)}")

@lonely.command()
async def gim(*args):
	"""Google image searches the arguments given. If none are given, defaults to nice jewish boys."""
	if (len(args) != 0):
		search = helper.convertSearch(args)
	else:
		search = "nice+jewish+boys"
	soup = helper.getSoup("https://www.google.com/search?tbm=isch&q={}".format(search))
	urllist = []
	for link in soup.find_all('img'):
		urllist.append(link.get('src'))
	return await lonely.say(str(random.choice(urllist)))

@lonely.command()
async def hello(*args):
	return await lonely.say("Hello world")

@lonely.command()
async def cheer(*args):
	"""Sends cheesey pick up lines to cheer you up."""
	phrases = ["Are you a magician? Because whenever I look at you, everyone else disappears!","Did you sit in a pile of sugar? Cause you have a pretty sweet ass.","Do you know what my shirt is made of? Boyfriend material.","Are you a camera? Because every time I look at you, I smile.","Do you have a Band-Aid? Because I just scraped my knee falling for you.","Do you work at Starbucks? Because I like you a latte.","If you were a vegetable you'd be a cute-cumber.","If you stood in front of a mirror and held up 11 roses, you would see 12 of the most beautiful things in the world.","If nothing lasts forever, will you be my nothing?","If you were a fruit, you would be a fineapple. And if you were a vegetable, I would visit you every day in hospital"]
	if (len(args) == 2 and args[0] == "me" and args[1] == "up"):
		return await lonely.say(random.choice(phrases))
	else:
		return await lonely.say("you made a typo you cabbage")

@lonely.command()
async def commands(*args):
	"""Sends a list of commands written so far."""
	return await lonely.say("""^waifu: search for your waifu\n^judge/shrug/lenny/angry: sends an text emoji\n^gim: google image search\n^cheer me up: sends a cheesy pick up link\n^feedback: if you'd like to see another function, or you found a bug, please use the feedback function to let me know\n^navy: sends the navy seal copypasta with no args, sends the weeb version with the weeb arg\n^haiku: sends a randomized haiku""")

@lonely.command()
async def hug(*args):
	"""Sends a picture of Kaneki asking for a hug."""
	return await lonely.say(" (> ^-^)>\nhttps://i.pinimg.com/originals/d3/d1/5b/d3d15bcd6e858a053af9e2ce28173fa1.jpg")

@lonely.command()
async def navy(*args):
	"""This sends the entire navy seal copypasta, or the weeb varient."""
	if (len(args) == 1 or args[0] == "weeb"):
		message = open('textfiles/weebcopy.txt','r',encoding="utf8").read()
	elif (len(args) == 2 and args[0] == "surprise" and args[1] == "me"):
		num = random.randrange(2)
		if (num == 0):
			message = open('textfiles/weebcopy.txt','r',encoding="utf8").read()
		else:
			message = open('textfiles/navyseal.txt','r',encoding="utf8").read()
	else:
		message = open('textfiles/navyseal.txt','r',encoding="utf8").read()

	return await lonely.say(message)

@lonely.command()
async def favoritemovie(*args):
	"""Sends the entire script of the Bee Movie."""
	charLimit = 2000
	script = open('textfiles/beemoviescript.txt','r',encoding="utf8").read().splitlines()
	printableString = ""
	for line in script:
		if (len(printableString)+len(line) < charLimit):
			printableString += "\n"+line
		else:
			await lonely.say(printableString)
			printableString = ""
	return await lonely.say(printableString)

@lonely.command()
async def haiku(*args):
	"""Sends a random haiku."""
	haikus = open('textfiles/haikus.txt','r',encoding="utf8").read().splitlines()
	startindex = random.randrange(len(haikus))
	startindex = startindex - startindex % 4
	finalstring = ""
	for i in range(0,3):
		finalstring += haikus[startindex+i] +"\n"
	return await lonely.say(finalstring)

@lonely.command()
async def feedback(*args):
	"""Auto emails feedback to my personal email account."""
	if (len(args)):
		emailBody = helper.convertMessage(args)
		address = "lonelybot1000@gmail.com"
		email = MIMEMultipart()
		email['Subject'] = "Lonely Bot Feedback"
		email['From'] = address

		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(address,'insecureaccount')
		email.attach(MIMEText(emailBody,'plain'))
		server.sendmail(address,"arogers7@buffalo.edu",emailBody)
		server.quit()
		return await lonely.say("Thank you for the feedback! You're a good noodle <3")
	else:
		return await lonely.say("Why would you send nothing as feedback. That doesn't make me feel very special.")

lonely.run("MzQ1MDI0NjYzMzE2ODU2ODMy.DG1dag.7XJi3Gc6TW4_mVCg4a1wuet9Isc")
