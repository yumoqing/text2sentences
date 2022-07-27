
from ftlangdetect import detect

class Sentence:
	def __init__(self, text, start_pos=0, dialog=False, new_paragraph=True):
		self.start_pos = start_pos
		self.text = text
		self.dialog = dialog
		self.new_paragraph = new_paragraph
		self.language = detect(text).get('lang')



