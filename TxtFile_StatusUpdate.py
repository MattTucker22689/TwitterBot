#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By: Matt Tucker
# Date: 16 Feb 17
#Description: The following is an example of a Twitter Bot built using Twython that takes lines at random from a .txt file and posts them to Twitter

import sys 
import random
from twython import Twython

CONSUMER_KEY = 'Yours Here'
CONSUMER_SECRET = 'Yours Here'
ACCESS_KEY = 'Yours Here'
ACCESS_SECRET = 'Yours Here'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

#This opens a file called "Links.txt" that is located in /home/pi/ and lets the computer know to execute the code that follows on the file
with open('Links.txt', 'r') as f:
    #This takes in the .txt file line by line
    lines = f.readlines()
    #The chooses a line a random
    choice = random.randrange(len(lines))
    #This prints the chosen line as a way of checking the code for bugs
    print(lines[choice])
    #This sends the line to Twitter to update your status
    api.update_status(status=lines[choice])
    #This closes the file
    f.close()
