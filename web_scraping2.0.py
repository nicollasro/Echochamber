# encoding: utf-8
# -*- coding: cp1252 -*-.
#!/usr/bin/python

import tweepy
import pandas as pd
from time import time


def web_scrapping(account, file):

	df = pd.DataFrame(columns=['id', 'created_at', 'source','user','full_text'])
	for status in tweepy.Cursor(api.user_timeline, screen_name=account, include_rts=False, lang="pt", tweet_mode="extended").items(batch):
		status = status._json
		#print (status.keys())
		new_entry = []
		new_entry += [status['id'], status['created_at'],status['source'],status['user']['screen_name'], status['full_text']]

		single_tweet_df = pd.DataFrame([new_entry],columns=df.columns)
		df = pd.concat([df, single_tweet_df])
		
	csvFile = open(file, 'w' ,encoding='utf-8')
	df.to_csv(csvFile, mode='w', columns=['id', 'created_at', 'source','user','full_text'], index=False, encoding="utf-8")
	
def check_limits(api):

	limits=api.rate_limit_status()
	for i in limits['resources'].keys():
		for k in limits['resources'][i].keys(): 
			if limits['resources'][i][k]['limit']!=limits['resources'][i][k]['remaining']:
				reset_time=float(limits['resources'][i][k]['reset'])-time()
				remain=int(limits['resources'][i][k]['limit'])-int(limits['resources'][i][k]['remaining'])
				max_limit=limits['resources'][i][k]['limit']
				print('---- Status com Limite Modificado---------')
				print (limits['resources'][i])
				print("Falta "+str(reset_time/60)+' min para o próximo reset')
				print('Capacidade comprometida '+str(int(remain)/int(max_limit)))

if __name__ == "__main__":

	consumer_key = "XXXX"
	consumer_secret = 'XXXX"
	access_key= 'XXXX'
	access_secret = 'XXXX'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	account = '@ '
	file_path =".csv"
	batch=10

	web_scrapping(account, file_path)
	print('Finalizou com sucesso!')
	




