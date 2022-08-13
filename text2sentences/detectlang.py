from langdetect import detect_langs

def detect_lang(x):
	y = detect_langs(x)
	print(y)
	s = None
	for m in y:
		print(m, type(m),dir(m))
		if s == None:
			s = {
				'lang':m.lang,
				'score':m.prob
			}
		elif s['score'] < m.prob:
			s = {
				'lang':lang,
				'score':prob
			}
	return s
