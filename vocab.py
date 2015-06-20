import csv

class Word:
	def __init__(self, name, part, inf=None, tran=0, tense=None, reflex=0):
		self.name = name
		self.part = part
		self.infinitive = inf
		self.transitive = tran
		self.tense = tense
		self.reflexive = reflex
	def __repr__(self):
		return self.name

class Language:
	def __init__(self):
		my_file = open('espanol.csv', 'rb')
		reader = csv.reader(my_file)
		self.words = []
		for row in reader:
			if row:
				self.words.append(row)
		my_file.close()
		self.language = []
		if self.words:
			for word in self.words:
				if word:
					temp_word = Word(word[0], word[1], word[2], word[3], word[4], word[5])
					self.language.append(temp_word)
		else:
			self.language=[]
		
	def add_word(self, m):
		self.words = [self.words, [m.name, m.part, m.infinitive, m.transitive, m.tense, m.reflexive]]
		
	def write_words(self):
		my_file = open('espanol.csv', 'wb')
		writer = csv.writer(my_file)
		writer.writerows(self.words)
		my_file.close()