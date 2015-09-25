#! /usr/bin/env python

import urllib, json, sys, urllib2

from pprint import pprint

if sys.argv[1] == 'XBL':
    system = 1
elif sys.argv[1] == 'PSN':
    system = 2
else:
    print """Usage: %s (XBL|PSN) (Username)"""
    sys.exit(1)

playerName = sys.argv[2]

if len(sys.argv) > 3:
    for i in range(3,len(sys.argv)):
        playerName = playerName + '%20' + sys.argv[i]

f = open('api_key', 'r')

api_key = f.read().rstrip()

if len(api_key) == 17:
    print "You must update your bungie.net api_key. Please read the README"
    sys.exit(2)

url3 = "http://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/%s/%s/" % (system, playerName)

req3 = urllib2.Request(url3)
req3.add_header('X-API-Key', api_key)
response3 = urllib2.urlopen(req3)
data3 = json.loads(response3.read())

try:
    playerId = data3['Response'][0]['membershipId']

except:
    print "There was an error, below is hopefully some useful information: "
    print data3['Message']
    pprint(data3)
    sys.exit(3)

url = "http://www.bungie.net/Platform/Destiny/Vanguard/Grimoire/%s/%s/" % (system, playerId)

url2 = "http://www.bungie.net/Platform/Destiny/Vanguard/Grimoire/Definition/"

req3 = urllib2.Request(url3)
req3.add_header('X-API-Key', api_key)
response3 = urllib2.urlopen(req3)
data3 = json.loads(response3.read())

req = urllib2.Request(url)
req.add_header('X-API-Key', api_key)
response = urllib2.urlopen(req)
data = json.loads(response.read())

req2 = urllib2.Request(url2)
req2.add_header('X-API-Key', api_key)
response2 = urllib2.urlopen(req2)
grimoire_data = json.loads(response2.read())

cards = data['Response']['data']['cardCollection']

# Shamelessly stolen list of grimoire cards to check against from http://destinyghosthunter.net/

frags = [ 700750 , 700680 , 700690 , 700700 , 700710 , 700720 , 700730 , 700740 , 700760 , 700770 , 700780 , 700790 , 700800 , 700810 , 700820 , 700830 , 700840 , 700850 , 700860 , 700870 , 700880 , 700890 , 700900 , 700910 , 700920 , 700930 , 700940 , 700950 , 700960 , 700970 , 700980 , 700990 , 701000 , 701010 , 701020 , 701030 , 701040 , 701050 , 701060 , 701070 , 701080 , 701090 , 701100 , 701110 , 701120 , 701130 , 701140 , 701150 , 701160 , 701170 ]

videos = {
    700750 : "https://youtu.be/YSd61cAh06k" ,
    700680 : "https://youtu.be/CRQFolmNqmA" ,
    700690 : "https://youtu.be/G9oo1J6e_jQ" ,
    700700 : "https://youtu.be/-5jNuQfsvt4" ,
    700710 : "https://youtu.be/VUO_KyKDkew" ,
    700720 : "https://youtu.be/k2RjU-Q6yGM" ,
    700730 : "https://youtu.be/bhTOr7MH93U" ,
    700740 : "https://youtu.be/PAOwpMhWVF8" ,
    700760 : "https://youtu.be/BaXODMsNexs" ,
    700770 : "https://youtu.be/SjvpQVCzGk4" ,
    700780 : "https://youtu.be/Lh2bm20my-Y" ,
    700790 : "https://youtu.be/zIZaL1NpXho" ,
    700800 : "https://youtu.be/OygJu-Jo0MA" ,
    700810 : "https://youtu.be/gubApRTD_wY" ,
    700820 : "https://youtu.be/PTAmhkkRlac" ,
    700830 : "https://youtu.be/FKDcFJYO8H8" ,
    700840 : "https://youtu.be/i7PBfkgqo5g" ,
    700850 : "https://youtu.be/LWLhu7LNWGA" ,
    700860 : "https://youtu.be/b_euukXiGq8" ,
    700870 : "https://youtu.be/ZmB3Ur5qhnE" ,
    700880 : "https://youtu.be/Zu2rIVdwGPI" ,
    700890 : "https://youtu.be/oq4A0x4m0BM" ,
    700900 : "https://youtu.be/ca_7fjcYebU" ,
    700910 : "https://youtu.be/M_5FpcLF3eU" ,
    700920 : "https://youtu.be/BqQ3UyMM_n4" ,
    700930 : "https://youtu.be/NVDG4K1IxvY" ,
    700940 : "https://youtu.be/FelSvk4eibc" ,
    700950 : "https://youtu.be/SpXELWBQEzI" ,
    700960 : "https://youtu.be/CMMRnFhQ2_U?t=41s" ,
    700970 : "https://youtu.be/CMMRnFhQ2_U?t=1m1s" ,
    700980 : "https://youtu.be/CMMRnFhQ2_U?t=1m7s" ,
    700990 : "https://youtu.be/CMMRnFhQ2_U?t=3m58s" ,
    701000 : "https://youtu.be/CMMRnFhQ2_U?t=4m12s" ,
    701010 : "https://youtu.be/List6aXiJp0" ,
    701020 : "https://youtu.be/34y2WRWj3wU" ,
    701030 : "https://www.reddit.com/r/DestinyTheGame/comments/3lb4oo/calcified_fragments_sorted_by_location_and_videos/cv6ss9y" ,
    701040 : "https://youtu.be/8jgI4qUCvCg" ,
    701050 : "https://www.youtube.com/watch?v=RypyNAyCMB0" ,
    701060 : "https://youtu.be/ZD33_Ps9u28" ,
    701070 : "https://www.youtube.com/watch?v=T0kV3GgSy5A" ,
    701080 : "https://youtu.be/xBAMdYOU4hk" ,
    701090 : "https://www.youtube.com/watch?v=DTIAP-oeFmE" ,
    701100 : "No information available" ,
    701110 : "No information available" ,
    701120 : "No information available" ,
    701130 : "https://youtu.be/FRGLuSNPObI" ,
    701140 : "https://youtu.be/j7wOMbqK-l0" ,
    701150 : "No information available" ,
    701160 : "https://www.youtube.com/watch?v=l5-YlGso7ug" ,
    701170 : "https://www.youtube.com/watch?v=LwcHJ7T6fq4" 
}

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
    print 'Obtain by: ' + videos[frag]
    print '-------'

print 'Total Fragments Found: ' + str(len(frags_org) - len(frags))