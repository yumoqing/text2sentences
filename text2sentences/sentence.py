
# from ftlangdetect import detect
from langdetect import detect_lang

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
		# self.language = detect(text)
		# self.lang = self.language['lang']
		x = self.detect_lang(text)
		l = None
		for k,v in x.items():
			if l is None:
				l = {
						'lang':k,
						'score':v
					}
				continue
			if v > l['score']:
				l = {
						'lang':k,
						'score':v
					}
		self.language = l
		self.lang = l['lang']

	def set_lang(self, lang):
		if self.language['score'] < 0.5:
			self.lang = lang

