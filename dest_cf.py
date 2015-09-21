#! /usr/bin/env python

import urllib, json, sys

if len(sys.argv) != 3:
    print """Usage: %s (XBL|PSN) (Username)

NOTE: You may have to enclose your username in quotes if it 
contains spaces or other non-alphanumeric characters"""
    sys.exit(1)

if sys.argv[1] == 'XBL':
    system = 1
else:
    system = 2

playerName = sys.argv[2]

url3 = "http://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/%s/%s/" % (system, playerName)

response3 = urllib.urlopen(url3)

data3 = json.loads(response3.read())

playerId = data3['Response'][0]['membershipId']

url = "http://www.bungie.net/Platform/Destiny/Vanguard/Grimoire/%s/%s/" % (system, playerId)

url2 = "http://www.bungie.net/Platform/Destiny/Vanguard/Grimoire/Definition/"

response = urllib.urlopen(url)

response2 = urllib.urlopen(url2)

data = json.loads(response.read())

grimoire_data = json.loads(response2.read())

cards = data['Response']['data']['cardCollection']

frags = [ 700680, 700690, 700700, 700710, 700720, 700830, 700840, 700850, 700860, 700770, 700780, 700790, 700800, 700810, 700820, 700830, 700840, 700850, 700860, 700870, 700880, 700890, 700900, 700910, 700920, 700930, 700940, 700950, 700960, 700970, 700980, 700990, 701000, 701010, 701020, 701030, 701040, 701050, 701060, 701070, 701080, 701090, 701100, 701110, 701120, 701130, 701140, 701150, 701160, 701170 ]

frags_org = frags[:]

carddb = {}

for card in cards:
    if card['cardId'] in frags:
        frags.remove(card['cardId'])


for theme in grimoire_data['Response']['themeCollection']:
    for page in theme['pageCollection']:
        for card in page['cardCollection']:
            cardId = card['cardId']
            cardName = card['cardName'].encode('utf-8', 'ignore')
            cardDescription = card['cardDescription'].encode('utf-8', 'ignore')
            if cardId in frags_org:
                frag_num = frags_org.index(cardId) + 1
            else:
                frag_num = -1

            carddb[cardId] = [cardName, cardDescription, frag_num]


for frag in frags:
    print '-------'
    print carddb[frag][0]
    print '-------'

print 'Total Fragments Found: ' + str(len(frags_org) - len(frags))