from random import randrange


class CreatInsult():
	preface = None
	col_one = None
	col_two = None
	col_three = None
	txt_file = None
	phrase = None
	word_location = [-1, -1, -1, -1]

	def set_genre(self, txtlen, txtfile):
		self.preface = txtlen[0]
		self.col_one = txtlen[1]
		self.col_two = txtlen[2]
		self.col_three = txtlen[3]
		self.txt_file = txtfile

	def get_string(self):
		line_count = 0
		self.phrase = ""
		with open(self.txt_file) as file:
			for line in file:
				line = line[:-1]
				if line_count == 0:
					self.phrase += line
				if line_count == self.word_location[0]:
					self.phrase += line
				if line_count == self.word_location[1]:
					self.phrase += " " + line
				if line_count == self.word_location[2]:
					self.phrase += " " + line
				if line_count == self.word_location[3]:
					self.phrase += " " + line
				line_count += 1

		return self.phrase

	def set_word_location(self):
		self.word_location[0] = randrange(2, self.preface)
		self.word_location[1] = randrange(self.preface+1, self.col_one)
		self.word_location[2] = randrange(self.col_one+1, self.col_two)
		self.word_location[3] = randrange(self.col_two+1, self.col_three)
		print(self.word_location[0], " " , self.word_location[1] , " " , self.word_location[2] , " " , self.word_location[3] , "\n")
