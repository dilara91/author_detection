#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import glob
import re


#takes tokenized train and test files and creates trigram files for the articles.				
				
def trigram():
	train = os.path.join('.', 'tokenized_train')
	test = os.path.join('.', 'tokenized_test')
	
	trigram_train = os.path.join('.', 'trigram_train')
	trigram_test = os.path.join('.', 'trigram_test')
	
	if not os.path.exists(trigram_train):
		os.makedirs(trigram_train)
	if not os.path.exists(trigram_test):
		os.makedirs(trigram_test)
	
	
			
	for filename in glob.glob(train+'\\*.txt'):
		text =[]
		author_name = filename.split('\\')[-1].split('.')[0]
		author_file = trigram_train+'\\'+author_name+'.txt'
		thefile = open(author_file, 'w+')
		myfile = open(filename, 'r')
		for line in myfile:
			text.append(line.strip())
		myfile.close()
		for index in range(0,len(text)-2):
			thefile.write(text[index]+' '+text[index+1]+' '+text[index+2]+'\n')
	
	
	for filename in glob.glob(test+'\\*.txt'):
		test_text = []
		author_name = filename.split('\\')[-1].split('.')[0]
		author_file = trigram_test+'\\'+author_name+'.txt'
		thefile = open(author_file, 'w+')
		myfile = open(filename, 'r')
		for line in myfile:
			test_text.append(line.strip())
		myfile.close()
		for index in range(0,len(test_text)-2):
			thefile.write(test_text[index]+' '+test_text[index+1]+' '+test_text[index+2]+'\n')
		
			
		
		
	
	
if __name__ == '__main__':
	trigram()