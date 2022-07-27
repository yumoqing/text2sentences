from .version import __version__
from .sentence import Sentence
sc_punctuation = [
	",",
	".",
	"?"
	"!",
	":",
	";",
]
big_punctuation = [
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
		self.new_paragraph = True
		
	def parse(self, text):
		sentences = []
		sentext = ''
		for i, c in enumerate(text):
			if c in [' ', '　']:
				if sentext != '':
					sentext = f'{sentext} '
				continue

			if c == '\r':
				continue

			if c == '\n':
				if sentext != '':
					sentence = Sentence(sentext, 
									start_pos=self.start_pos,
									dialog=True,
									new_paragraph=self.new_paragraph)
					sentences.append(sentence)
					sentext = ''
				self.new_paragraph = True
				continue

			if c in ['"', '“', '”']:
				if sentext != '':
					sentence = Sentence(sentext, 
									start_pos=self.start_pos,
									dialog=True,
									new_paragraph=self.new_paragraph)
					sentences.append(sentence)
					self.new_paragraph = False
				sentext = ''
				if self.in_quote:
					self.in_quote = False
				else:
					self.in_quote = True
				continue

			if c in sc_punctuation and text[i+1] in [' ', '\r', '\n'] \
							or c in big_punctuation:
				if sentext != '':
					sentence = Sentence(sentext, 
									start_pos=self.start_pos,
									dialog=self.in_quote,
									new_paragraph=self.new_paragraph)
					self.new_paragraph = False
					sentences.append(sentence)
					sentext = ''
				continue
			if sentext == '':
				self.start_pos = i
			sentext = f'{sentext}{c}'
		if sentext != '':
			sentence = Sentence(sentext, 
							start_pos=self.start_pos,
							dialog=self.in_quote,
							new_paragraph=self.new_paragraph)
			sentences.append(sentence)
			sentext = ''
		return sentences
				
def text_to_sentences(text):
	tp = TextParser()
	s = tp.parse(text)
	return s

