# -*- coding: utf-8 -*-
"""
Data preprocessing 
importignt the librarires
"""
import twitter as t
import tweepy as tpy
import pandas as pd
import csv
ACCESS_TOKEN="1098034925327003648-r9hguqt1aDW2HgZwktaptvDomn9zhe"
ACCESS_TOKEN_SECRET="1zb50B1gRrbODwBDnB8X1gSgjequn2wb9qU011lQaos57"
CONSUMER_KEY="aRg2d2EiG4E3h5IhRwXrQi9Cd"
CONSUMER_SECRET="uF5rvny06xRKU3FytlCFB7LSw6pxQJAFvP3lKMhs2HxLqLcab3"
auth = tpy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tpy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('crpf_data.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tpy.Cursor(api.search,q="#crpf",count=100,
                           lang="en",
                           since="2019-02-14").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])