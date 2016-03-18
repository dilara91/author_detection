#!/usr/bin/python

#Dilara Kekulluoglu 2014700171

import sys
import os
import re
import math

#gets a root which is where the train files are. This is for having the counts for each class.
#mode can be 1,2 or 3 and they indicate which method we use for classifying. BoW, BoW+bigram etc.
def main(root,mode):
	class_count = train_count(root)	#how many instances each class have in train files.
	total_class_count = sum(class_count.itervalues()) #total number of files in train files.
	print 'total class count '+str(total_class_count)
	dictionary = []
	if mode == 1:    #BoW approach
		myfile = open('dictionary.txt', 'r')
	elif mode == 2:  #BoW+bigram approach
		myfile = open('bigram_dictionary.txt', 'r')
	else:            #BoW+trigram approach
		myfile = open('trigram_dictionary.txt', 'r')
	
	for line in myfile:
		dictionary.append(line.strip())
	myfile.close()
	
	word_count = len(dictionary)    #total word count in the dictionary
	print 'word count '+str(word_count)    
	
	authors_list = []	
	for dirname in os.listdir(root):
		authors_list.append(dirname)
	
	author_tokens = [[] for i in range(len(authors_list))]
	for author_name in authors_list:
			if mode == 1:
				author_file = open('.\\tokenized_train\\'+author_name+'.txt', 'r')
			elif mode== 2:
				author_file = open('.\\bigram_train\\'+author_name+'.txt', 'r')
			else:
				author_file = open('.\\trigram_train\\'+author_name+'.txt', 'r')
			a_index = authors_list.index(author_name)
			
			for line in author_file:
				author_tokens[a_index].append(line.strip())
			author_file.close()
	
	actual_class = []
	predicted_class = []
	if mode == 1:
		for filename in os.listdir('.\\tokenized_test'):
			filepath = os.path.join('.\\tokenized_test', filename)
			words = []
			myfile = open(filepath, 'r')
			for line in myfile:
				words.append(line.strip())
			myfile.close()
			actual_class.append(filename.split('_')[0]) #what is the actual class?
			probability={}
			for author_name in authors_list:
				a_index = authors_list.index(author_name)
				probability[author_name]=likelihood(words,author_name,author_tokens[a_index],class_count,total_class_count,word_count,mode)
			predicted_class.append(max(probability.iterkeys(), key=(lambda key: probability[key])))	
			#what is the predicted class? 
			#predicted class is found by taking the maximum likelihood that is calculated. 
			#every class is measured by the naive bayes and the one with the maximum likelihood
			#is selected as the predicted class.
	elif mode == 2:
		for filename in os.listdir('.\\bigram_test'):
			filepath = os.path.join('.\\bigram_test', filename)
			words = []
			myfile = open(filepath, 'r')
			for line in myfile:
				words.append(line.strip())
			myfile.close()
			actual_class.append(filename.split('_')[0])
			probability={}
			for author_name in authors_list:
				a_index = authors_list.index(author_name)
				probability[author_name]=likelihood(words,author_name,author_tokens[a_index],class_count,total_class_count,word_count,mode)
			predicted_class.append(max(probability.iterkeys(), key=(lambda key: probability[key])))	
	else:
		for filename in os.listdir('.\\trigram_test'):
			filepath = os.path.join('.\\trigram_test', filename)
			words = []
			myfile = open(filepath, 'r')
			for line in myfile:
				words.append(line.strip())
			myfile.close()
			actual_class.append(filename.split('_')[0])
			probability={}
			for author_name in authors_list:
				a_index = authors_list.index(author_name)
				probability[author_name]=likelihood(words,author_name,author_tokens[a_index],class_count,total_class_count,word_count,mode)
			predicted_class.append(max(probability.iterkeys(), key=(lambda key: probability[key])))	
	
	
	#this is the confusion matrix. 69 x 69
	contingency = [[0 for x in range(len(class_count))] for x in range(len(class_count))] 
	
	
	if mode==1:
		result_file = open('result.txt','w+')
	elif mode==2:
		result_file = open('result_bigram.txt','w+')
	else:
		result_file = open('result_trigram.txt','w+')
	
	for actual, predicted in zip(actual_class, predicted_class):
		actual_index = authors_list.index(actual)
		predicted_index = authors_list.index(predicted)
		contingency[actual_index][predicted_index] = contingency[actual_index][predicted_index] + 1
		#fill the confusion matrix according to the actual and predicted classes.
		#normally dictionaries are not ordered so we used a list to keep the indexes of the authors
		#in the confusion matrix.
	
	for author in authors_list:
		i = authors_list.index(author)
		result_file.write(str(contingency[i]))
		result_file.write('\n')
	
	macro_averaged_precision = 0
	macro_averaged_recall = 0
	
	total_tp = 0  #tp --> true positive
	total_fp = 0  #fp --> false positive
	total_fn = 0  #fn --> false negative
	
	for author in authors_list:
		index_a = authors_list.index(author)
		tp = contingency[index_a][index_a]
		fp = predicted_class.count(author)-tp
		fn = sum(contingency[index_a]) - tp
		total_tp = total_tp + tp
		total_fp = total_fp +fp
		total_fn = total_fn + fn
		if tp + fp != 0:
			precision = float(tp) / (tp + fp)
		else:					#when the classifier does not assign a class to 
			precision = 1		#any file we have zero division so we take it as 1.
		if tp+fn != 0:
			recall = float(tp) / (tp + fn)
		else:
			recall = 0			#same with the case that there are no files in the train set for that class. This is not a problem we face with this dataset. 
		result_file.write(author+' precision : '+str(precision)+' recall : '+str(recall)+'\n')
		macro_averaged_precision =  macro_averaged_precision + precision
		macro_averaged_recall = macro_averaged_recall + recall
	
	result_file.write('\n')
	macro_averaged_precision = float(macro_averaged_precision) / len(authors_list)
	macro_averaged_recall = float(macro_averaged_recall) / len(authors_list)
	macro_f1_measure = 2*macro_averaged_precision*macro_averaged_recall / (macro_averaged_precision + macro_averaged_recall)
	result_file.write('macro averaged precision '+str(macro_averaged_precision)+'\n')
	result_file.write('macro averaged recall '+str(macro_averaged_recall)+'\n')
	result_file.write('macro f1 measure '+str(macro_f1_measure)+'\n\n')
	
	micro_averaged_precision = float(total_tp) / (total_tp + total_fp)
	micro_averaged_recall = float(total_tp) / (total_tp + total_fn)
	micro_f1_measure = 2*micro_averaged_precision*micro_averaged_recall / (micro_averaged_precision + micro_averaged_recall)
	result_file.write('micro averaged precision '+str(micro_averaged_precision)+'\n')
	result_file.write('micro averaged recall '+str(micro_averaged_recall)+'\n')
	result_file.write('micro f1 measure '+str(micro_f1_measure)+'\n')
	
	



#takes the possible author name and calculates the probability of that author
#being the author of this given filename.
def likelihood(words,author_name,train_words,class_count,total_class_count,word_count,mode):
	
	
	
	
	p_c = math.log(float(class_count[author_name]) / total_class_count)
	#class likelihood. The more samples we have in the train data, the more it increases.
	p_wc = 0       
	
	for w in words:
		freq = train_words.count(w) + 1
		div = float(freq) / (len(train_words)+word_count)
		p_wc = p_wc + math.log(div)  #logarithmic conversion is used since these are very 
									 #little numbers to multiply.
	
	return p_c + p_wc





#takes the root to train files and counts the files that each author has.
def train_count(root):
	class_count ={}	
	for dirname in os.listdir(root):
		if(dirname != root):
			author = os.path.join(root, dirname)
			class_count[dirname] = len(os.listdir(author))
	return class_count









if __name__ == '__main__':
  main()