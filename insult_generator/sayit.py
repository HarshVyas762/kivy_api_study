from kivy.properties import ObjectProperty

from creatinsult import CreatInsult


class SayIt():

	insult = CreatInsult()
	text_file = None
	previous_phrase = ""
	current_phrase = ""

	#def set_insult(self, txtlen, txtfile):
	#	self.insult = CreatInsult(txtlen, txtfile)

	def get_phrase(self, txtlen, txtfile):
		self.insult.set_genre(txtlen, txtfile)
		self.insult.set_word_location()
		self.previous_phrase = self.current_phrase
		self.current_phrase = self.insult.get_string()
		
	def get_current(self, txtlen, txtfile):
		self.get_phrase(txtlen, txtfile)
		return self.current_phrase

	def get_previous(self):
		return self.previous_phrase

	def stop_play(self):
		self.current_phrase.stop()
		self.previous_phrase.stop()