#
#author: Bijil Abraham Philip
#

import nltk

class QuestionRetriever:
	questionsForTags={[]}
	tags={}

	__init__(self,questionsForTags,tags):
		self.questionsForTags=questionsForTags
		self.tags=tags