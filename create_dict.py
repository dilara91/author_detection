#!/usr/bin/python


import sys
import os
import glob
import re


				
def create_dict(mode):
	if mode ==1:
		dirname = os.path.join('.', 'tokenized_train')
		thefile = open('dictionary.txt', 'w+')
	elif mode ==2:
		dirname = os.path.join('.', 'bigram_train')
		thefile = open('bigram_dictionary.txt', 'w+')
	else:
		dirname = os.path.join('.', 'trigram_train')
		thefile = open('trigram_dictionary.txt', 'w+')
	
	text =[]		
	for filename in glob.glob(dirname+'\\*.txt'):
		myfile = open(filename, 'r')
		for line in myfile:
			text.append(line.strip())
		myfile.close()
	
	unique_words = set(text)
	for word in unique_words:
		thefile.write(str(word) + "\n")
	
if __name__ == '__main__':
	create_dict()