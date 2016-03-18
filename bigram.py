#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import glob
import re


#takes tokenized train and test files and creates bigram files for the articles.				
def bigram():
	train = os.path.join('.', 'tokenized_train')
	test = os.path.join('.', 'tokenized_test')
	
	bigram_train = os.path.join('.', 'bigram_train')
	bigram_test = os.path.join('.', 'bigram_test')
	
	if not os.path.exists(bigram_train):
		os.makedirs(bigram_train)
	if not os.path.exists(bigram_test):
		os.makedirs(bigram_test)
	
	
			
	for filename in glob.glob(train+'\\*.txt'):
		text =[]
		author_name = filename.split('\\')[-1].split('.')[0]
		author_file = bigram_train+'\\'+author_name+'.txt'
		thefile = open(author_file, 'w+')
		myfile = open(filename, 'r')
		for line in myfile:
			text.append(line.strip())
		myfile.close()
		for index in range(0,len(text)-1):
			thefile.write(text[index]+' '+text[index+1]+'\n')
		
	
	for filename in glob.glob(test+'\\*.txt'):
		test_text = []
		author_name = filename.split('\\')[-1].split('.')[0]
		author_file = bigram_test+'\\'+author_name+'.txt'
		thefile = open(author_file, 'w+')
		myfile = open(filename, 'r')
		for line in myfile:
			test_text.append(line.strip())
		myfile.close()
		for index in range(0,len(test_text)-1):
			thefile.write(test_text[index]+' '+test_text[index+1]+'\n')
				
		
		
	
	
if __name__ == '__main__':
	bigram()