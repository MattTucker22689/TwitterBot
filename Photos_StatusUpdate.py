#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By: Matt Tucker
# Date: 24 Feb 17
#Description: The following is an example of a Twitter Bot built using Twython that posts random photos

import sys, os, random
from twython import Twython

CONSUMER_KEY = 'Yours Here'
CONSUMER_SECRET = 'Yours Here'
ACCESS_KEY = 'Yours Here'
ACCESS_SECRET = 'Yours Here'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#Chose a random integer 1-10, I did this because I created a collection of 10 images and ittereated their names 1-10.
choice=random.randint(1,10)
#File name is: 'random number'.jpg
name = str(choice) + ".jpg"
#My photos are located /home/pi so I only had to use the file name.... Otherwise, you will need to state location/file
photo = open(name, 'rb')

#For videos change "api.upload_media(media=photo)" to "api.upload_video(media=video, media_type='video/mp4')"
api.update_status(media_ids=[api.upload_media(media=photo)['media_id']])

#BAM PHOTO STATUS!
