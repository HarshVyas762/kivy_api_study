from random import randrange




class CreatInsult():
	preface = None
	col_one = None
	col_two = None
	col_three = None
	txt_file = None
	phrase = None
	word_location = [-1, -1, -1, -1]

	def __init__(self):
		self.preface = 4
		self.col_one = 55
		self.col_two = 106
		self.col_three = 157
		

	def get_string(self):
	#	set_phrase = [False, False, False, False]
		line_count = 0
		self.phrase = ""
		with open("shakespear.txt") as file:
			for line in file:
				line = line[:-1]
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

		self.word_location[0] = randrange(0, self.preface)
		self.word_location[1] = randrange(self.preface+1, self.col_one)
		self.word_location[2] = randrange(self.col_one+1, self.col_two)
		self.word_location[3] = randrange(self.col_two+1, self.col_three)

		#for i in self.word_location:
		#S	print(i)










	def f_output():
		# open file
		with open("database.txt") as file:
			# print out each line in file
			for line in file:
				print(line)
				# close file