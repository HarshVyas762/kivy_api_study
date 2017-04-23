

class SaveFavorite():

	def f_input(self, file_l, save_l, aw):
		with open(file_l, aw) as file:
			file.write(save_l + "\n")