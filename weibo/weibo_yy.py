#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
	from weibo import APIError, APIClient
	import webbrowser
	import json

	APP_KEY = '181368435'            # app key
	APP_SECRET = '2109f155c381f1d5d14a711c0fc68680'      # app secret
	CALLBACK_URL = 'www.baidu.com'  # callback url
	CODE = ''

	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	saveData = json.load(open("user_info.json", 'r'))

	if CODE != "": 
		token = client.request_access_token(CODE, CALLBACK_URL)
		saveData['access_token'] = token.access_token
		saveData['token_expired_time'] = token.expires
		json.dump(saveData, open('user_info.json', 'w'))
	elif not saveData.has_key("access_token") or not saveData.has_key("token_expired_time"):
		url = client.get_authorize_url()
		webbrowser.open(url)
		
	client.set_access_token(saveData['access_token'], saveData['token_expired_time'])
	timeline = client.statuses.user_timeline.get()
	
	resp = client.friendships.friends.get(uid=2094298015)
	for user in resp.users:
		print '%d %s' % (user.id, user.name)