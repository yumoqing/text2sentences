from .version import __version__
from .sentence import Sentence

Punctuation = [
	",",
	".",
	"?"
	"!",
	":",
	";",
	"，",
	"。",
	"？",
	"！",
	"：",
	"；"
]

class TextParser:
	def __init__(self):
		self.in_quote = False
		self.quote = None
		self.start_pos = 0
		
	def parse(self, text):
		sentences = []
		sentext = ''
		for i,c in enumerate(text):
			if c == ' ':
				if sentext != '':
					sentext = f'{sentext} '
				continue

			if c == '\r':
				continue

			if c == '\n':
				if self.in_sentence:
					sentext = f'{sentext} '
				else:
					self.new_paragraph = True
				continue

			if c in ['"', '“']:
				if self.in_quote and self.quote == c:
					sentence = Sentence(sentext, 
									start_pos=self.start_pos,
									dialog=True)
					sentences.append(sentence)
					sentext = ''
				else:
					self.in_quote = True
					self.quote = c
				continue

			if c in Punctuation:
				if sentext != '':
					sentence = Sentence(sentext, 
									start_pos=self.start_pos,
									dialog=self.in_quote)
					sentences.append(sentence)
					sentext = ''
				continue
			if sentext == '':
				self.start_pos = i
			sentext = f'{sentext}{c}'
		if sentext != '':
			sentence = Sentence(sentext, 
							start_pos=self.start_pos,
							dialog=self.in_quote)
			sentences.append(sentence)
			sentext = ''
		return sentences
				
def text2sentence(text):
	tp = TextParser()
	s = tp.parse(text)
	return s

