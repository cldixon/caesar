import string 

class Caesar:
	def __init__(self):
		self.whatami = "I am the Caesar Cypher."
		self.letters = list(string.ascii_lowercase)
		self.letter_index = self._generate_letter_index()


	def _generate_letter_index(self):
		'''Creates bijective mapping between
		alphabet letters (lowercase only) and
		their index.'''
		letter_idx = {l:i for i,l in enumerate(self.letters)}
		idx_letter = {i:l for i,l in enumerate(self.letters)}
		letter_idx.update(idx_letter)
		return letter_idx

	def _shift(self, letter, value):
		'''Provide letter and shift values
		as input. Outputs shifted letter.'''
		letter_idx = self.letter_index[letter]
		add_shift = (letter_idx + value) % 26
		return self.letter_index[add_shift]

	def _tokenize_message(self, message):
		'''Basic preparation of input message.'''
		return list(message)

	def _lowercase_tokens(self, tokens):
		'''Lowercases all tokens in tokenized message.'''
		return [t.lower() for t in tokens]

	def cypher(self, message, shift, keep_caps=False):
		'''Encrypts input message.'''
		tokenized = self._tokenize_message(message)
		processed = self._lowercase_tokens(tokenized)
		encrypted = [self._shift(l, shift) if l in self.letters else l for l in processed]
		# option to keep capitalized letters
		if keep_caps is True:
			caps_idx = [i for i in range(len(tokenized)) if tokenized[i] in string.ascii_uppercase]
			encrypted = [l.upper() if i in caps_idx else l for i,l in enumerate(encrypted)]
		return ''.join(encrypted)

	def decypher(self, message, shift, keep_caps=False):
		'''Decrypts input message.'''
		return self.cypher(message, -shift, keep_caps=keep_caps)
