
from ftlangdetect import detect

class Sentence:
	def __init__(self, text, start_pos=0, dialog=False):
		self.start_pos = start_pos
		self.text = text
		self.dialog = dialog
		self.language = detect(text)



