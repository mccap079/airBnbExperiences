import json
from subprocess import call
import os
from time import sleep

username = 'yourInstagramUsername';
pw = 'yourInstagramPassword';

infile = open('output.json', 'r') # r = read
data = json.load(infile)
experiences = data['experiences']

currentDir = os.getcwd()

for i, experience in enumerate(experiences):
	caption = experience['kicker_text'] + ', ' + experience['country']
	filename = currentDir + '/img/' + str(i) + '.jpg'
	city = experience['kicker_text'].split(' * ')[-1]
	rating = u'\U0001F525' * int(experience['star_rating']) #u'\U0001F525' = fire emoji
	caption = 'I experienced: ' + experience['title'] + ' #' + city + ' #' + experience['country'] + ' ' + rating
	print caption

	call(['instapy','-u',username,'-p',pw,'-f',filename,'-t',caption])
	sleep(120) # pause for 2 min between posts

infile.close()