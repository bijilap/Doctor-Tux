#
# author: Bijil Abraham Philip
#
import csv
import nltk
from ques_retriever import QuestionRetriever
from tag_extract import TagExtractor


class DoctorTux:

	questions=[[]]
	tags={}
	questionsForTags={}
	tagsInQuestions={}
	synonym_tags={}

	def __init__(self,directory):
		#get list of all tags that can be simplified into synonym tags
		stf = open(directory+"tags_synonym.csv", 'r')
		rdr= csv.reader(stf)
		for r in rdr:
			self.synonym_tags[r[0]]=r[1]
		stf.close()

		qf=open(directory+"Questions&Answers.csv",'r')








directory="data/"