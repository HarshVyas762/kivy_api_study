

class SaveFavorite():

	def f_output(self, file_l):
		fav = None
		with open(file_l) as file:
			for line in file:
				fav = line[:-1]
				
		return(fav)

	def f_input(self, file_l, save_l, aw):
		if not self.test_input(file_l, save_l):
			with open(file_l, aw) as file:
				file.write(save_l + "\n")

	def test_input(self, file_l, save_l):
		already_saved = False
		try:
			with open(file_l) as file:
				for line in file:
					line = line[:-1]
					if line == save_l:
						already_saved = True
		except FileNotFoundError:
			pass

		return(already_saved)



				
