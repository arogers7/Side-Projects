from bs4 import BeautifulSoup
import requests

def getSoup(url):
    """This helps to call beautifulSoup, since I'm always using bs's html parser, I made a command to take in a url and do everything I need from beautiful soup."""
    r = requests.get(url)
    return BeautifulSoup(r.content,'html.parser')

def convertMessage(args):
    """converts the arguments given by the user in discord into a string that can be emailed."""
    str = args[0]
    for i in range(1,len(args)):
        str = str + " " + args[i]
    return str

def convertSearch(args):
    """converts the arguments given by discord into a usable url for beautiful soup."""
    str = args[0]
    for i in range(1,len(args)):
        str = str + "+" + args[i]
    return str
