# Twitter_Bot
An academic Twitter bot meant to help spread research. The purpose of this bot is to take links in a .txt file and release them at regular intervals.

Disclaimer: The following is meant as an academic excerise. It is only meant to show the reader how to build Twitter bots, and some of their functionalitis. How the reader applies it, is a matter all of their own. I do not condone the misuse of technologies in any format.

The following tutorial will be written with the assumption that the user is executing this code on a Raspberry Pi.
We will be using Python and Twython, and is done entirely on the Pi. I personally prefer accessing my Pi remotely using a combination of SSH and VNC methods. If you are unsure how to, or what that even is... I suggest checking out these videos:

https://youtu.be/-v88m-HYeys

https://youtu.be/PYunvpwSwGY

Alexander Baran-Harper, does a GREAT job at showing other's how to use their Pi.

1.) After you wire your "Pi" and have it connected to your wifi network, open Terminal and type in the following command:
                            
                            sudo apt-get update
                            
After you press enter, the Pi will run thru and update the packages. This process can take SEVERAL mins.
Now, once that process is done... type:
                            
                            sudo apt-get upgrade
                            
This will upgrade the packages.
As a note, it is generally a good idea to resize your SD. To do so, type:

                            sudo raspi-config

You will be greeted by a menu which you can navigate using your arrow keys and the enter button. Navigate to the menu item, "Expand Filesystem" and click entered. You will see a rush of text and then a menu pop back up. Go ahead an click enter. Then press navigate to "Finnish." Now you should be asked if you'd like to reboot the Pi, click "Ok."

2.)Keeping in with the previous step we are going to be typing a few more thing into Terminal to get our bot running. The next thing that we want/need to do is type in each of the following, after the previous command is done,

                           sudo apt-get install python-setuptools

                           sudo easy_install pip
                           
                           sudo pip install twython

To briefly explain, all this is really doing is installing the API and libraries needed so that our bot can commuinicate with Twitter.

Disclaimer: Ok, so you might run into a problem here. Don't panic. This is likely just becuase versions are out of date or some other analagous reason. If you do run into trouble, Google it(Twython)! I'm sure there is an answer out there somewhere. Just to get you started here are two links I found with a quick Google search:

https://devcereal.com/how-to-build-raspberry-pi-twitter-bot-python/

http://raspi.tv/2013/how-to-create-a-twitter-app-on-the-raspberry-pi-with-python-tweepy-part-1#app   (This example uses the Tweepy API- might not hurt to go ahead and grab Tweepy and check out the library. To do so type: sudo pip install tweepy)

3.)Now let's take a moment to set up our bot's Twitter page.(I'll let you figure that one out :P )

4.)Cool, so you have the libraries and you have your bot's Twitter page ready. Now we have to go to
https://apps.twitter.com/app/new
This part is actually alot easier than it feels. So, quickly populate the fields accordingly.
When you're done check the box and click the button at the bottom. Sweet, we're almost to the fun part... the code. But, we have to get some info really quick. 

After you clicked the button, you'll be greeted by a screen with a bunch of words saying stuff that makes almost no sense to you probably. It's koasher, I didn't understand it my first time either, but that's ok. Because all we need to do is navigate to the tab that says: 

"Keys and Access Tokens"

Now, scroll down and click,

"Create Access Tokes"

Cool. Almost there. Now, there are four stings of charcters that we need to copy and store somewhere.... A .txt blank file will do. The strings we need to copy are the long lines of geberish that comes after the following(do try to keep them organised, it'll help):

Consumer Key (API Key)

Consumer Secret (API Secret)

Access Token

Access Token Secret

Alright, keep that file open! Maybe even save it! You will NEED those in a min.

5.)NOW THE CODE! So, the way I like to do things is by opening up Python 2. If you would like, you could certainly use "nano" to create the text based .py file in Terminal. I just happen to like the feel of coding using IDLE(Python's native compiler).

Since I will be posting some of my own personal code, here I will only tell you that you want start your code with:

                           #!/usr/bin/env python
                           import "insert the libraries you plan on using"
                           from twython import Twython

                           CONSUMER_KEY = 'your consumer key goes here'
                           CONSUMER_SECRET = 'your consumer secret goes here'
                           ACCESS_KEY = 'your access token goes here'
                           ACCESS_SECRET = 'your access secret goes here' 
                           
                           api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
                           
                           "Enter you code"
                           
And that ladies and gent's concludes the basics of what you need to know to get things up and going. Again, I'm posting copy of my own code up, and will be adding comments to it to help you further along. 

A note, for the Tweepy API start with the following:
  
                         import tweepy  
                         import "W/E Libs you want to use"
                         
                         consumer_key = 'your consumer key goes here'  
                         consumer_secret = 'your consumer secret goes here'  
                         access_token = 'your access token goes here'  
                         access_token_secret = 'your access secret goes here'  
                         
                         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
                         
                         auth.set_access_token(access_token, access_token_secret)  
                         
                         api = tweepy.API(auth)
                         
                         "Enter you code"
                         

Also, here are links to both Twython's and Tweepy's library:

https://media.readthedocs.org/pdf/twython/latest/twython.pdf

http://tweepy.readthedocs.io/en/v3.5.0/



From here you will no doubt want to know how to run your code. To bad go home... Just kidding. To run your code simply open Terminal and type:
                     
                           python "name".py
                           
If you want to make your code run at regular intervals, then type in the following command:

                          crontab -e
                          
Now, you should be greeted with a bunch of explanations and nice little commentary on how crontab work. I'm going to do that in like a line here. Basially what you are going to type is:

                          * * * * * /usr/bin/python /home/pi/"LOCATION"/"TwitterBot".py

Now, what do those * mean? Basically it breaks down like this:

1st - Min

2nd - Hr(24-clock)

3rd - Day of the Month

4th - Month

5th - Day of the Week

So, let's say you wanted to run your code at 1:30pm every day, then you'd type:

                          30 13 * * * /usr/bin/python /home/pi/"LOCATION"/"TwitterBot".py

3:45am the first day of every month AND 1:30pm every day? Type this:

                          45 3 1 * * /usr/bin/python /home/pi/"LOCATION"/"TwitterBot".py
                          30 13 * * * /usr/bin/python /home/pi/"LOCATION"/"TwitterBot".py

And now you're done! Your code will run when ever you set it to. Happy Twitter botting!
