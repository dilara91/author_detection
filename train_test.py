#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import random
import shutil

#takes the path to the authors' files and splits them to 60/40 train/test files.

def main():
	
	test_dir = os.path.join('.', 'test')
	train_dir = os.path.join('.', 'train')
	if not os.path.exists(test_dir):
		os.makedirs(test_dir)
	
	if not os.path.exists(train_dir):
		os.makedirs(train_dir)
	
	for dirname, dirnames, filenames in os.walk(sys.argv[1]):
		if(dirname != sys.argv[1]):
			
			train = (len(filenames)*6)/10
			test = len(filenames) - train
		
			author_train = os.path.join(train_dir,dirname.split('\\')[-1])
			author_test = os.path.join(test_dir,dirname.split('\\')[-1])
			
			if not os.path.exists(author_train):
				os.makedirs(author_train)
	
			if not os.path.exists(author_test):
				os.makedirs(author_test)
			
			
			random_files = random.sample(range(1, len(filenames)), train)
			count = 0
			for filename in filenames:
				count = count+1
				cur_file = os.path.join(dirname, filename)
				if count in random_files:
					to_move_file = os.path.join(author_train, filename)
					shutil.copy(cur_file, to_move_file)
					
				else:
					to_move_file = os.path.join(author_test, filename)
					shutil.copy(cur_file, to_move_file)

		









if __name__ == '__main__':
  main()