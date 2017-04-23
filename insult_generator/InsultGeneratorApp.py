from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from savefavorite import SaveFavorite
from sayit import SayIt



class MainScreen(Screen):
	pass


class ShakespearScreen(Screen):
	txt_len = [4, 55, 106, 157]
	txt_file = "shakespear.txt"
	savefav = SaveFavorite()
	sayit = SayIt(txt_len, txt_file)

class PirateScreen(Screen):
	txt_len = [5, 43, 77, 109]
	txt_file = "pirate.txt"
	savefav = SaveFavorite()
	sayit = SayIt(txt_len, txt_file )

class RudeScreen(Screen):
	txt_len = [7, 51, 72, 88]
	txt_file = "rude.txt"
	savefav = SaveFavorite()
	sayit = SayIt(txt_len, txt_file)

class FavoriteScreen(Screen):
	pass


class ScreenManagment(ScreenManager):
	pass






load_kivy_file = Builder.load_file("insultgenerator.kv")

class InsultGeneratorApp(App):
	def build(self):
		return load_kivy_file


if __name__ == '__main__':
	InsultGeneratorApp().run()