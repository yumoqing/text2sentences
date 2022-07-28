
from ftlangdetect import detect

class Sentence:
	def __init__(self, text, start_pos=0, 
						dialog=False, 
						semi_sentence=False, 
						new_paragraph=True):
		self.start_pos = start_pos
		self.text = text
		self.dialog = dialog
		self.semi_sentence=semi_sentence
		self.new_paragraph = new_paragraph
		self.language = detect(text)
		self.lang = self.language['lang']

	def set_lang(self, lang):
		if self.language['score'] < 0.5:
			self.lang = lang

