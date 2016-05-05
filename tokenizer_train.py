#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import glob
import re

#takes the path to the author folders and tokenize them. There will be one train
#file for each author.
def main(root):
	for dirname in os.listdir(root):
		if(dirname != root):
			tokenize(root,dirname)
	
				
def tokenize(root,author):
	dirname = os.path.join(root, author)
	token = os.path.join('.', 'tokenized_train')
	if not os.path.exists(token):
		os.makedirs(token)
	thefile = open('tokenized_train/'+author+'.txt', 'w+')
	for filename in glob.glob(dirname+'/*.txt'):
		file = open(filename, 'r')
		text = file.read().lower() #lower every letter
		file.close()
		r = re.compile(r'[\W\d_]', re.U) #support Turkish chars. 
		text = r.sub(" ", text) #replaces every non alphanumeric char with space.
		words = list(text.split()) #splits it according to spaces.
		for item in words:
			if len(item)>2 and len(item)<8:      #trims the words to only have
				thefile.write("%s\n" % item)	 #at most seven letters.
			elif len(item)>7:
				thefile.write("%s\n" % item[:7])
	
if __name__ == '__main__':
	main()
