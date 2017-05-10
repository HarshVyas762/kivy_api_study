from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.audio import SoundLoader

from tts import PlaySoundFile
from savefavorite import SaveFavorite
from sayit import SayIt


class MainScreen(Screen):
	pass


class InsultScreen(Screen):
	screen_name = ObjectProperty(0)
	screen_left = ObjectProperty(0)
	screen_right = ObjectProperty(0)
	generate_phrase = ObjectProperty(0)
	sound_button = ObjectProperty(0)
	mp3_file = "play_file.mp3"
	sound = False
	insult = None
	insult_page = ["shakespear", "pirate", "rude"]
	insult_text = ["shakespear.txt", "pirate.txt", "rude.txt", "favorite.txt"]
	file_len = [[4, 55, 106, 157], [5, 43, 77, 109], [7, 51, 72, 88]]
	which_screen = 0
	savefav = SaveFavorite()
	playspeech = PlaySoundFile()
	say = SayIt()


	def current_screen(self):
		if(self.which_screen == 2):
			self.screen_right.text = self.insult_page[1]
			self.screen_name.text = self.insult_page[self.which_screen]
			self.screen_left.text = self.insult_page[0]
		if(self.which_screen == 1):
			self.screen_right.text = self.insult_page[0]
			self.screen_name.text = self.insult_page[self.which_screen]
			self.screen_left.text = self.insult_page[2]
		if(self.which_screen == 0):
			self.screen_right.text = self.insult_page[2]
			self.screen_name.text = self.insult_page[self.which_screen]
			self.screen_left.text = self.insult_page[1]	

	def next_screen(self):
		self.which_screen -= 1
		if(self.which_screen < 0):
			self.which_screen = 2

		self.current_screen()

	def previous_screen(self):
		self.which_screen += 1		
		if(self.which_screen > 2):
			self.which_screen = 0

		self.current_screen()

	def current_insult(self):
		self.insult = self.say.get_current(self.file_len[self.which_screen], self.insult_text[self.which_screen])
		if self.insult:
			lang = self.insult[:5]

			self.generate_phrase.text = self.insult[5:]	
			if self.sound:
				self.playspeech.play_text(self.insult[5:], lang,  self.mp3_file)

	def previous_insult(self):
		self.insult = self.say.get_previous()
		if self.insult:
			lang = self.insult[:5]

			self.generate_phrase.text = self.insult[5:]
			if self.sound:
				self.playspeech.play_text(self.insult[5:], lang,  self.mp3_file)

	def play_button(self):
		if self.insult:
			lang = self.insult[:5]

			if self.sound:
				self.playspeech.play_text(self.insult[5:], lang,  self.mp3_file)

	def save_favorite(self):
		if self.insult:
			self.savefav.f_input(self.insult_text[3], self.insult, "w")

	def play_favorite(self):
		fav = self.savefav.f_output(self.insult_text[3])

		if fav:
			lang = fav[:5]

			self.generate_phrase.text = fav[5:]

			if self.sound:
				self.playspeech.play_text(fav[5:], lang, self.mp3_file)


	def sound_select(self):		
		if self.sound:			
			self.sound = False
			self.sound_button.color = 0.9, 0, 0.3, 1
		else:
			self.sound = True
			self.sound_button.color = 0, 0.9, 0.3, 1

class ScreenManagment(ScreenManager):
	pass


load_kivy_file = Builder.load_file("insultgen.kv")

class InsultGenApp(App):
	def build(self):
		return load_kivy_file


if __name__ == '__main__':
	InsultGenApp().run()