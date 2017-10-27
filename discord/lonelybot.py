import discord
import asyncio
import requests
import random
import time as t
from bs4 import BeautifulSoup
from discord.ext.commands import Bot
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#client = discord.Client()
lonely = Bot(command_prefix="^")

def getSoup(url):
#since I'm always using bs's html parser, I made a command to take in a url and do everything I need from beautiful soup
	r = requests.get(url)
	return BeautifulSoup(r.content,'html.parser')

def convertMessage(args):
	str = args[0]
	for i in range(1,len(args)):
		str = str + " " + args[i]
	return str


def convertSearch(args):
#convers the arguments into a string from an array
	str = args[0]
	for i in range(1,len(args)):
		str = str + "+" + args[i]
	return str

@lonely.event
async def on_ready():
	print("client logged in")

@lonely.command()
async def waifu(*args):
#sends pictures of cute anime girls
	if (len(args) == 0):
		search = "holo"
	else:
		search = convertSearch(args)

	message = "Here's a waifu, you weeby fuck: "

	soup = getSoup("http://danbooru.donmai.us/posts?utf8=%E2%9C%93&tags={}&ms=1".format(search))

	urls = []
	for link in soup.find_all('img'):
	    urls.append(link.parent.get('href'))

	if (len(urls) == 0):
		return await lonely.say("No results. Your waifu is shit.")

	soup = getSoup('http://danbooru.donmai.us/' + random.choice(urls))
	for link in soup.find_all('img'):
	    return await lonely.say(message + 'http://danbooru.donmai.us' + str(link.get('src')))

@lonely.command()
async def judge(*args):
#sometimes you just need someone to know that you're judging them for their choices, but you don't have the eyes of judgment on your clipboard
	return await lonely.say("ಠ_ಠ ")
@lonely.command()
async def shrug(*args):
	return await lonely.say("¯\_(ツ)_/¯ ")
@lonely.command()
async def lenny(*args):
	return await lonely.say("(° ͜ʖ°)")
@lonely.command()
async def lobster(*args):
	return await lonely.say("(/) (°,,°) (/)")
@lonely.command()
async def angry(*args):
	return await lonely.say("{(>_<)}")

@lonely.command()
async def gim(*args):
#google image search
	if (len(args) != 0):
		search = convertSearch(args)
	else:
		search = "star+of+david"
	soup = getSoup("https://www.google.com/search?tbm=isch&q={}".format(search))
	urllist = []
	for link in soup.find_all('img'):
		urllist.append(link.get('src'))
	return await lonely.say(str(random.choice(urllist)))

@lonely.command()
async def hello(*args):
	return await lonely.say("Hello world")


@lonely.command()
async def cheer(*args):
	phrases = ["Are you a magician? Because whenever I look at you, everyone else disappears!","Did you sit in a pile of sugar? Cause you have a pretty sweet ass.","Do you know what my shirt is made of? Boyfriend material.","Are you a camera? Because every time I look at you, I smile.","Do you have a Band-Aid? Because I just scraped my knee falling for you.","Do you work at Starbucks? Because I like you a latte.","If you were a vegetable you'd be a cute-cumber.","If you stood in front of a mirror and held up 11 roses, you would see 12 of the most beautiful things in the world.","If nothing lasts forever, will you be my nothing?","If you were a fruit, you would be a fineapple. And if you were a vegetable, I would visit you every day in hospital"]
	if (len(args) == 2 and args[0] == "me" and args[1] == "up"):
		return await lonely.say(random.choice(phrases))
	else:
		return await lonely.say("you made a typo you cabbage")

@lonely.command()
async def commands(*args):
		return await lonely.say("""^waifu: search for your waifu\n^judge/shrug/lenny/angry: sends an text emoji\n^gim: google image search\n^cheer me up: sends a cheesy pick up link\n^feedback: if you'd like to see another function, or you found a bug, please use the feedback function to let me know\n^whatdidyousay: sends the navy seal copypasta\n^favoritemovie: sends the entirity of the bee movie script""")

@lonely.command()
async def whatdidyou(*args):
#says the navy seal copypasta
	message = open('navyseal.txt','r',encoding="utf8").read()
	return await lonely.say(message)

@lonely.command()
async def favoritemovie(*args):
#crashes bot, only sends first message
	charLimit = 2000
	timestop = 4
	script = open('beemoviescript.txt','r',encoding="utf8").read().splitlines()

	printableString = ""
	for line in script:
		if (len(printableString)+len(line) < charLimit):
			printableString += "\n"+line
		else:
			await lonely.say(printableString)
			#t.sleep(timestop)
			print(printableString)
			printableString = ""
	return await lonely.say(printableString)



@lonely.command()
async def feedback(*args):
	if (len(args)):
		emailBody = convertMessage(args)
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

@lonely.command()
async def tvtropes(*args):
	#this line loads the search with the properly formatted args, not functional
	soup = getSoup("http://tvtropes.org/pmwiki/search_result.php?q={}&cx=partner-pub-6610802604051523%3Aamzitfn8e7v&cof=FORID%3A10&ie=ISO-8859-1&siteurl=&ref=&ss=".format(convertSearch(args)))

lonely.run("MzQ1MDI0NjYzMzE2ODU2ODMy.DG1dag.7XJi3Gc6TW4_mVCg4a1wuet9Isc")
