import sys
import os
import string

def sortList(text):
	text.sort(key= lambda x: x[1], reverse=True)
	return text
	
def top_Kquery(text, k):
	return(text[:k])
	
def process():	
        cur_ = os.getcwd()
	dir_ = os.path.join(cur_, "outdir")
	fname = os.path.join(dir_,"source_0_split_0_.mtxt")
	f = open(fname, "r")
	text = f.readlines()
	
	for i in text:
	   text[text.index(i)] = tuple(i.split()) 
	          
        return text

if __name__ == '__main__':

     sorted_txt = sortList(process())
     query = [10,20]
     for k in query:
       print("Top: "+ str(k) + " occuring words")
       for i in top_Kquery(sorted_txt,k):
                print(i)

