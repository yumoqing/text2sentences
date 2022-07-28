from text2sentences import text_to_sentences
import sys
import codecs

def txtfile(fname, coding='utf-8'):
	with codecs.open(fname, 'r', coding) as f:
		return f.read()

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(f'Usage:\n{sys.argv[0]} txtfile')
		sys.exit(1)
	
	coding = 'utf-8'
	if len(sys.argv) > 2:
		coding = sys.argv[2]
	txt = txtfile(sys.argv[1], coding)
	sentences = text_to_sentences(txt)
	for s in sentences:
		print('sentence=', s.text, len(s.text), s.dialog, s.lang, s.start_pos, s.new_paragraph)
