#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
import webbrowser

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'ue5t443M3wblQMHotxuJVzC3T'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'vAEEtvxS3DoqmKLvZu2Ub6mrDSuVympaOnQgsTLYZ5SiqE2HUD'#keep the quotes, replace this with your consumer secret key
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

try:
    redirect_url = auth.get_authorization_url() 
except tweepy.TweepError:
    print('Error! Failed to get request token.')

webbrowser.open(redirect_url)
pin = input()
token = auth.get_access_token(verifier=pin)

auth.set_access_token(token[0], token[1])

api = tweepy.API(auth)


print('Insert the name to star following')
nombre = input()



seguidos = 0
while seguidos<10000:
	friendsFrom = api.friends_ids(nombre)
	for id in friendsFrom:
		api.create_friendship(id)
		seguidos = seguidos + 1
		print('Nuevo usuario seguido', seguidos)
	nombre = friendsFrom[0]


#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(status=line)
#    time.sleep(900)#Tweet every 15 minutes





