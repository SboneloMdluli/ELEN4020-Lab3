import sys
import os
import string
import re

def process(k):	
        cur_ = os.getcwd()
	dir_ = os.path.join(cur_, "outdir")
	fname = os.path.join(dir_,"source_0_split_0_.mtxt")
	f = open(fname, "r")
	text = f.readlines()
	
	for line,i in enumerate(text):
	        if (line > 50) and (not re.search(r'\d', i[0])):
	            text[text.index(i)] = tuple(i.split()) 
	            print(i)
	                   
	        if line== 50 + k:
	             break


if __name__ == '__main__':

     k = 50
     print("First distinct: "+ str(k) + " words")
     
     fil = process(k)
  
