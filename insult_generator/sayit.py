from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from creatinsult import CreatInsult


class SayIt(BoxLayout):
	generat_phrase = ObjectProperty(0)
	insult = None
	text_file = None
	previous_phrase = ""
	current_phrase = ""

	def __init__(self, txtlen, txtfile):
		self.insult = CreatInsult(txtlen, txtfile)

	#insult.set_word_location()
	

	def get_phrase(self):
		self.insult.set_word_location()
		self.previous_phrase = self.current_phrase
		self.current_phrase = self.insult.get_string()
		
	def get_current(self):
		self.get_phrase()
		return self.current_phrase

	def get_previous(self):
		return self.previous_phrase

	def stop_play(self):
		self.current_phrase.stop()
		self.previous_phrase.stop()