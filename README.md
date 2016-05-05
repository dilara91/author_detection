# author_detection
Homework 1 for Cmpe 561 in Python

The problem caused by slashes solved. It ran on pythonanywhere correctly. 
Download and put files in the same folder.

To use the program user need to firstly run the train\_test.py script. This will take the dataset as an argument. Dataset should in a format where there are folders for every author and files in them respectively. The path should be given to that folder. In the case of 69yazar you should write the following;

python train\_test.py ./69yazar/raw\_texts

Please make sure to add ./ if the directory is on your path. 
After running this script you can use author\_detection.py. Make sure that you have all the python files in the same folder. You should give the train and the test paths as arguments respectively. If you used the train_test.py script it should be called as follows;

python author\_detection.py ./train ./test

After the program ends we have three result files one for each method; BoW, BoW+Bigram, BoW+Trigram.  You can find results of my run of the program in the repository.

If you want to use only one method, you should comment out the others. For example if you only want to compute the BoW approach, then comment out the methods as explained in the author\_detection.py .
