import os
import subprocess
import glob
import sys
from os.path import basename
def myfunction():
	i = 0
	dem = 0
	directory_list = list()
	temp = 'D:/the-complete-react-native-and-redux-course'
	for root, dirs, files in os.walk(temp, topdown=False):
	    for name in dirs:
	        directory_list.append(os.path.join(root, name))

	for dir in directory_list:
		i = i + myfunction2(dir)
	
	for dir in directory_list:
		dem = dem + myfunction3(dir, dem, i)

def myfunction2(dir):
	path = dir + '\\*.mp4'
	i = 0
	files = glob.glob(path)
	if files:
		for file in files:
			i = i + 1
	if i > 0:
		return i
	else:
		return 0

def myfunction3(dir, dem, i):
	path = dir + '\\*.mp4'
	files = glob.glob(path)
	temp2 = 0
	if files:
		for file in files:
			print "Dang xu li file "+ basename(file)
			temp ='python autosub_app.py ' + "\"" +file + "\""
			subprocess.call(temp)
			temp2 = temp2 + 1
			print "Da xu li %d / %d file" %( dem + temp2, i)
			print "************************************************************************************************"
			print "************************************************************************************************"
			print "************************************************************************************************"
			print "************************************************************************************************"
			print "************************************************************************************************"
	
	if temp2 > 0:
		return temp2
	else:
		return 0
			
myfunction()

