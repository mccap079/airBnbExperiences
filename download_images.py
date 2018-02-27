import json
import urllib, urlparse
import os

workingDir = os.getcwd()

infile = open('output.json', 'r') # r = read
data = json.load(infile)
experinces = data['experiences']

for i, experience in enumerate(experinces):
	picture = experience["picture"]
	filename = workingDir + "/img/" + str(i) + ".jpg"
	urllib.urlretrieve(picture, filename)

infile.close()