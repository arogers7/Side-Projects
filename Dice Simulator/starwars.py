import requests
import random

def fact(*args):
    url = 'https://swapi.co/api/{}/{}/'
    try:
        if random.randrange(0,2)==1:
            #this is planets
            #a random planet (of the 59 planets in the API) is chosen
            num = random.randrange(1,59)
            request = requests.get(url.format('planets',num))
            info = request.json()
            option = random.choice(['rotation period','diameter','population'])
            sentence = 'The planet {} has a {} of {}.'.format(info['name'],option,info[option.replace(' ','_')])

        else:
            #this is species
            num = random.randrange(1,37)
            request = requests.get(url.format('species',num))
            info = request.json()
            option = random.choice(['average_height','average_lifespan','language'])
            if option=='average_height':
                sentence = 'The species {} has an average height of {} cm'.format(info['name'],info['average_height'])
            if option=='average_lifespan':
                sentence = 'The species {} has an average lifespan of {} years'.format(info['name'],info['average_lifespan'])
            if option=='language':
                sentence = 'The species {} speaks {}'.format(info['name'],info['language'])

        if info[option] == 'unknown':
            raise
        else:
            return (True,sentence)
    except:
        #all exceptions are caught by the same exception because the fact is not
        #necessary for the sim to work. Since I want the roll results to appear
        #immediately, no more time can be wasted trying to find a valid fact
        return (False,'null')
