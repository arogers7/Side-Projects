import helper
args = ['abc','def']
print(helper.convertSearch(args))

"""
##This is what I wrote to convert book of haikus into a format that was more useful to my bot, I was too proud to delete it :)"
rawhaikus = open('haikusraw.txt','r',encoding="utf8").read().splitlines()
haikus = open('haikus.txt','w',encoding="utf8")

haikunum = 0
haikus.write("NEWHAIKU\n")
for line in range(len(rawhaikus)):
    if (len(rawhaikus[line]) > 0 and rawhaikus[line][0] =="—"):
        for index in [6,4,2]:
            haikus.write(rawhaikus[line-index])
            haikus.write("\n")
        haikus.write("\n")
"""
