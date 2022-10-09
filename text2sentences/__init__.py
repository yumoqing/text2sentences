from appPublic.uniqueID import getID
from .version import __version__
from .sentence import Sentence
from .detectlang import detect_lang
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
	def __init__(self, unilang=False):
		self.in_quote = False
		self.unilang = unilang
		self.quote = None
		self.start_pos = 0
		self.sentences = []
		self.sentence = ''
		self.new_paragraph = True
		
	def add_sentence(self, 
						start_pos,
						dialog=None,
						new_paragraph=False,
						semi_sentence=False):
		lang=None
		if self.unilang:
			lang = self.language['lang']
		if self.sentext != '':
			sentence = Sentence(self.sentext, 
							start_pos=self.start_pos,
							dialog=True,
							semi_sentence=semi_sentence,
							lang=lang,
							new_paragraph=self.new_paragraph)
			sentence.langdetect()
			sentence.set_lang(self.language['lang'])
			sentence.set_article_id(self.article_id)
			self.sentences.append(sentence)
		self.sentext = ''

	def check_text_language(self, text):
		x = text.replace('\r', '').replace('\n', ' ')
		self.language = detect_lang(x)

	def parse(self, text):
		self.article_id = getID()
		self.check_text_language(text)
		self.sentences = []
		self.sentext = ''
		for i, c in enumerate(text):
			if c in [' ', '　']:
				if self.sentext != '':
					self.sentext = f'{self.sentext} '
				continue

			if c == '\r':
				continue

			if c == '\n':
				if self.sentext != '':
					self.add_sentence(start_pos=self.start_pos,
									dialog=True,
									semi_sentence=False,
									new_paragraph=self.new_paragraph)
				self.new_paragraph = True
				continue

			if c in ['"', '“', '”']:
				if self.sentext != '':
					self.add_sentence(start_pos=self.start_pos,
									dialog=True,
									semi_sentence=False,
									new_paragraph=self.new_paragraph)
					self.new_paragraph = False
				if self.in_quote:
					self.in_quote = False
				else:
					self.in_quote = True
				continue

			if c in sc_punctuation and i < len(text)-1 and text[i+1] in [' ', '\r', '\n'] \
							or c in big_punctuation:
				if self.sentext != '':
					if c in [',','，','、']:
						semi = True
					else:
						semi = False
					self.add_sentence(start_pos=self.start_pos,
									dialog=self.in_quote,
									semi_sentence=semi,
									new_paragraph=self.new_paragraph)
					self.new_paragraph = False
				continue
			if self.sentext == '':
				self.start_pos = i
			self.sentext = f'{self.sentext}{c}'
		if self.sentext != '':
			self.add_sentence(start_pos=self.start_pos,
							dialog=self.in_quote,
							semi_sentence=False,
							new_paragraph=self.new_paragraph)
		return self.sentences
				
def text_to_sentences(text, unilang=False):
	tp = TextParser(unilang=unilang)
	s = tp.parse(text)
	return s

