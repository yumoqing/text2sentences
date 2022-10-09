
from appPublic.uniqueID import getID
from .detectlang import detect_lang

class Sentence:
	def __init__(self, text, start_pos=0, 
						dialog=False, 
						semi_sentence=False, 
						new_paragraph=True,
						lang=None):
		self.sentence_id = getID()
		self.start_pos = start_pos
		self.text = text
		self.dialog = dialog
		self.semi_sentence=semi_sentence
		self.new_paragraph = new_paragraph
		if lang:
			self.language = {
				'score' : 1,
				'lang' : lang
			}
		self.lang = lang
		self.article_id = None

	def langdetect(self):
		if self.lang is None:
			self.language = detect_lang(self.text)
			self.lang = self.language['lang']

	def set_article_id(self, id):
		self.article_id = id

	def set_lang(self, lang):
		if self.language['score'] < 0.5:
			self.lang = lang

	def to_dict(self):
		return {
			'sentence_id':self.sentence_id,
			'start_pos':self.start_pos,
			'dialog':self.dialog,
			'semi_sentence':self.semi_sentence,
			'new_paragraph':self.new_paragraph,
			'lang':self.lang,
			'language':self.language,
			'article_id':self.article_id,
			'text':self.text
		}

def sentence(dic):
	s = Sentence(dic['text'])
	s.sentence_id = dic['sentence_id']
	s.start_pos = dic['start_pos']
	s.dialog = dic['dialog']
	s.semi_sentence = dic['semi_sentence']
	s.new_paragraph = dic['new_paragraph']
	s.language = dic['language']
	s.article_id = dic['article_id']
	s.lang = dic['lang']
