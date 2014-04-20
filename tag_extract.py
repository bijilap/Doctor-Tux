#
# author: Bijil Abraham Philip
#

import nltk

class TagExtractor:
	tags={} #set of tags
	complex_tags={} #first word of complex tag : complex tag.......complex tag is one having >1 word and seperated by a -
	hyponomy_tags={} #tag: highest level of abstraction/ tag synonym
	complex_tags_replacements={} #first word:complex tag (words seperated by a dash)

	def __init__(self,tags,complex_tags,hyponomy_tags,complex_tags_replacements):
		self.tags=tags
		self.complex_tags=complex_tags
		self.complex_tags_replacements=complex_tags_replacements
		self.hyponomy_tags=hyponomy_tags


	def identifyComplextags(self,question):
		features=nltk.word_tokenize(question)
		for f in features:
			if f in self.complex_tags:
				#print self.complex_tags[f]
				#question=question.replace(self.complex_tags[f],self.complex_tags_replacements[f])
				for ctag in self.complex_tags[f]:
					#print ctag
					question=question.replace(ctag,self.complex_tags_replacements[ctag])

		return question

	def resolveHyponomy(self,question): #convert tags to simplest tags
		features=question.split()
		for f in features:
			if f in self.hyponomy_tags:
				#print self.hyponomy_tags[f]
				question=question.replace(f,self.hyponomy_tags[f])
		return question