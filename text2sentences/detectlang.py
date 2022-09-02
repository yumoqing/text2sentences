from langdetect import detect_langs

def detect_lang(x):
	try:
		y = detect_langs(x)
	except:
		y = None
	if y is None:
		return {
			'lang':'zh',
			'score':0
		}
	s = None
	for m in y:
		lang = m.lang.split('-')[0]
		if s == None:
			s = {
				'lang':lang,
				'score':m.prob
			}
		elif s['score'] < m.prob:
			s = {
				'lang':lang,
				'score':m.prob
			}
	return s
