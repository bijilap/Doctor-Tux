#
# author: Bijil Abraham Philip
#
import csv
import nltk
from ques_retriever import QuestionRetriever
from tag_extract import TagExtractor


class DoctorTux:

	questions=[[]]
	answers=[]
	tags={}
	questionsForTags={}
	tagsInQuestions={}
	synonym_tags={}
	complex_tags={}
	complex_tags_replacements={}

	def __init__(self,directory):
		#get list of all tags that can be simplified into synonym tags
		stf = open(directory+"tags_synonym.csv", 'r') #converting each tag to its hypernym
		rdr= csv.reader(stf)
		for r in rdr:  
			#r[0]=tag  r[1]=tag it should be replaced with
			self.synonym_tags[r[0]]=r[1]
		stf.close()

		tf=open(directory+"tags.csv", 'r') #assign wieght for tag for each tag
		rdr=csv.reader(tf)
		for r in rdr:
			tmp=r[0].split(';') #tmp[0]=tag      tmp[1]=frequency
			self.tags[tmp[0]]=float(1/float(tmp[1]))
		tf.close()

		for tmp in self.tags:
			t=tmp.split('-')
			if len(t)>1:
				t2=tmp.replace('-',' ')
				#print t2
				if t[0] not in self.complex_tags:
					self.complex_tags[t[0]]=[]

				self.complex_tags[t[0]].append(t2)
				#self.complex_tags_replacements[t[0]]=tmp
				self.complex_tags_replacements[t2]=tmp

		qf=open(directory+"Questions&Answers&Tags.csv",'r')
		rdr=csv.reader(qf)
		for r in rdr: #r[0]:question title r[1]=question title r[2]: best answer r[3]: tags
			if r[0][len(r[0])-1] not in ['!','?','.']:
				r[0]=r[0]+'.'
			r[1]=nltk.clean_html(r[1])
			r[2]=nltk.clean_html(r[2])
			r[0]=r[0]+' '+r[1]
			self.questions.append(r[0])
			self.answers.append(r[1])
			n=len(self.questions)-1
			r[3]=r[3].replace('<','')
			r[3]=r[3].replace('>',' ')
			tmplist=r[3].split(' ')
			for t in tmplist:
				if t in self.synonym_tags:
					r[3]=r[3].replace(t,self.synonym_tags[t])

			tmplist=r[3].split(' ')
			tmplist.pop()
			self.tagsInQuestions[n]=tmplist
			for t in tmplist:
				if t not in self.questionsForTags:
					self.questionsForTags[t]=[]
				self.questionsForTags[t].append(n)

		qf.close()
		#print self.questionsForTags
	

	def getClosestQuestionSet(self,question):
		tagEx=TagExtractor(self.tags,self.complex_tags,self.synonym_tags,self.complex_tags_replacements)
		quesRet=QuestionRetriever(self.questionsForTags, self.tags,self.questions)
		question=question.lower()
		question=tagEx.identifyComplextags(question)
		question=tagEx.resolveHyponomy(question)
		tagsInQuestions=tagEx.getTagsFromQuestion(question)
		similarQuestionList=quesRet.retrieveSimilarQuestions(question,tagsInQuestions)
		for sques in similarQuestionList:
			print self.questions[sques]
			print "\n\n#########\t#########\n\n"
		#print question

directory="data/"
dt=DoctorTux(directory)
#dt.getClosestQuestionSet("How do I install Ubuntu Touch on my laptop?")
#dt.getClosestQuestionSet("How do I install Ubuntu 12.04.3 on my HP dv6 laptop?")
#dt.getClosestQuestionSet("I had to make a windows update, this means that you have to restore the windows bootloader, after i did that using installation disc, I wanted to restore or repair my GRUB. How can we restore grub into system with no or minimal boot access?")
#dt.getClosestQuestionSet("How  to install unity on ubuntu server?")
#dt.getClosestQuestionSet("how can I create a user with admin rights in ubuntu using command-line ?")
dt.getClosestQuestionSet("How to install windows ubuntu (wubi) ?")
#dt.getClosestQuestionSet("Is there a SPARC(Sun Microsystem) installation for Ubuntu. I wanted to install this on an old server in my university")
#dt.getClosestQuestionSet("How to recover ubuntu from grub load issues?")