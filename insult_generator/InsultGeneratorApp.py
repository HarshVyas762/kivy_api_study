from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from sayit import SayIt


class MainScreen(Screen):
	pass


class ShakespearScreen(Screen):
	sayit = SayIt()


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