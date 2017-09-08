#This program reads the tf-model generated by main.py and then calculates tf-idf and saves it to file.
#now, when the query is fired, the model is read and the similarity is measured
from os import listdir
import os.path
from operator import itemgetter
import string
import sys
from math import log10
def buildTfIdfModelFromTfModel():
	tf_vector_model = eval(open("./input/tf_modelDemo", "r").read())
	idf = {}
	tf_idf = {}
	num = 0
	#build idf
	for term in tf_vector_model:
		for element in tf_vector_model[term]:
			if 0 not in element: #term exists in the document
				num += 1
		idf[term] = log10((len(tf_vector_model[term])*1.0)/(num*1.0))
		num = 0
	#save this idf for processing the query too.
	idf_file = open("./input/idf_file", "w")
	idf_file.write(str(idf))
	idf_file.close()
	#build tf-idf
	for term in tf_vector_model:
		for element in tf_vector_model[term]:
			try:
				tf_idf[term].append([element[0], element[1] * idf[term]])
			except Exception as e:
				tf_idf[term] = []
				tf_idf[term].append([element[0], element[1] * idf[term]])
	return tf_idf

def build_tfidf_of_query(query):
	idf = eval(open("./input/idf_file", "r").read())
	print idf
	tf_idf_of_query = {}
	for word in query.split():
		if word in idf:
			pass
			
def innerProduct(query, document_dict): #here onwards, the similarity checks are in operation. query is the string to be searched and document_dict is tf-idf measure
	pass

def MinkawaskiDistance(query, document_dict, p):
	pass

def EucladianDistance(query, document_dict):
	pass

def ManhattanDistance(query, document_dict):
	pass

def CosineSimilarity(query, document_dict):
	pass

def preProcess(): #this file returnes the tf-idf if it already exists, else returns -1 suggesting invocation buildTfIdfModelFromTfModel
	if os.path.exist/'):
		return buildTfIdfModelFromTfModel()
	print "please create the tf-model using main.py script."
	return -1
	
def main():
	print "Enter the query: ",
	query = str(raw_input())
	#find Tf-IDF of the query
	#now show result of every similarity measure technique.
	tf_idf = {}
	tf_idf = preProcess()
	if(tf_idf == -1):
		return 1
	print tf_idf
	innerProduct(query, tf_idf)
	#MinkawaskiDistance(qury, tf-idf)
	EucladianDistance(query, tf_idf)
	ManhattanDistance(query, tf_idf)
	CosineSimilarity(query, tf_idf)
if __name__ == '__main__':
	main()