#
#author: Bijil Abraham Philip
#

import nltk
import operator

class QuestionRetriever:
	questionsForTags={} #list of questions corresponding to a tag 
	tags={} # tag:inverse of frequency
	questions=[] #list of questions with index as question number

	def __init__(self,questionsForTags,tags,questions):
		self.questionsForTags=questionsForTags
		self.tags=tags
		self.questions=questions

	def retrieveSimilarQuestions(self,question,tagsOfQuestion):
		relevantQues={}
		for tag in tagsOfQuestion:
			curTagQL=self.questionsForTags[tag]  #question list for current tag
			for q in curTagQL:
				if q in relevantQues:
					relevantQues[q]=relevantQues[q]+self.tags[tag]
				else: 
					relevantQues[q]=self.tags[tag]
			
		final_list=[]
		sorted_list=sorted(relevantQues.iteritems(), key=operator.itemgetter(1))
		for s in range(len(sorted_list)-10,len(sorted_list)-1):
			final_list.append(sorted_list[s][0])


		return final_list