from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


from creatinsult import CreatInsult


class SayIt(BoxLayout):
	generat_phrase = ObjectProperty(0)
	insult = CreatInsult()
	previous_phrase = ""
	current_phrase = ""

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


class InsultGeneratorApp(App):
	def build(self):
		return SayIt()


if __name__ == '__main__':
	InsultGeneratorApp().run()