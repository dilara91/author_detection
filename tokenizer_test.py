#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import glob
import re

#takes the path to the author folders and tokenize them. There will be one test
#file for each file in test folder.

def main(root):
	for dirname in os.listdir(root):
		if(dirname != root):
			tokenize_test(root,dirname)
	
				
def tokenize_test(root,author):
	dirname = os.path.join(root, author)
	token = os.path.join('.', 'tokenized_test')
	if not os.path.exists(token):
		os.makedirs(token)
	
	for filename in glob.glob(dirname+'/*.txt'):
		file = open(filename, 'r')
		text = file.read().lower() #lower every letter
		file.close()
		test_filename = filename.split('/')[-2]+'_'+filename.split('/')[-1]
		thefile = open('tokenized_test/'+test_filename, 'w+') #author names are used for naming files so that it is known.
		r = re.compile(r'[\W\d_]', re.U) #support Turkish chars. 
		text = r.sub(" ", text)   #replaces every non alphanumeric char with space.
		words = list(text.split())   #splits it according to spaces.
		for item in words:
			if len(item)>2 and len(item)<8:
				thefile.write("%s\n" % item)   #trims the words to only have
			elif len(item)>7:                  #at most seven letters.
				thefile.write("%s\n" % item[:7])
	
if __name__ == '__main__':
	main()
