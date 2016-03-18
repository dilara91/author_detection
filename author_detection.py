#!/usr/bin/python

import sys
import os
import tokenizer_train
import tokenizer_test
import create_dict
import multinomial_naive_bayes
import bigram
import trigram

def main():
	
	
	tokenizer_train.main(sys.argv[1])
	tokenizer_test.main(sys.argv[2])
	
	#Only BoW approach
	create_dict.create_dict(1)
	multinomial_naive_bayes.main(sys.argv[1],1)
	
	#BoW+Bigram. Comment out this 3 lines if you don't want to compute.
	bigram.bigram()
	create_dict.create_dict(2)
	multinomial_naive_bayes.main(sys.argv[1],2)
	
	#BoW+Trigram. Comment out this 3 lines if you don't want to compute.
	trigram.trigram()
	create_dict.create_dict(3)
	multinomial_naive_bayes.main(sys.argv[1],3)
	
	
















if __name__ == '__main__':
	main()