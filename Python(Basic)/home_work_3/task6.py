def int_func(string):
	"""
	принимает строку и возвращает ее же но с заглавными буквами каждого слова
	:param string: str
	:return: str
	"""
	result = ' '.join([word.title() for word in string.split()])
	return result


assert int_func('text') == 'Text'
assert int_func('abraCadabra') == 'Abracadabra'

assert int_func('my text') == 'My Text'
assert int_func('abra cadabra') == 'Abra Cadabra'
