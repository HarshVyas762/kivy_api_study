from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty

# google text to speech api
from gtts import gTTS 


class TextToSpeech():
	tts = None

	def __init__(self):
		self.tts = gTTS(text = "text-to-speech", lang = 'en-us')
		self.tts.save('play_file.wav') # or mp3

	def set_speech(self, phrase):
		self.tts = gTTS(text = phrase, lang = 'en-us')

	def save_to_file(self):
		self.tts.save('play_file.wav')


class PlaySoundFile(Screen):
	speech_input = ObjectProperty()
	new_phrase = TextToSpeech()
	sound = None
	phrase = None

	def play_text(self):
		self.get_sound()

		if not self.sound:
			pass
		else:
			self.sound.play()

	def stop_play(self):
		self.sound.stop()

	def get_sound(self, fl = 'play_file.wav'):		
		self.sound = SoundLoader.load(fl)

	def get_speech(self):
		if not self.speech_input.text:
			self.phrase = "text-to-speech"
		else:
			self.phrase = self.speech_input.text
			
		self.set_phrase()
		self.get_sound()

	def set_phrase(self):
		self.new_phrase.set_speech(self.phrase)
		self.new_phrase.save_to_file()


class ScreenManagment(ScreenManager):
	pass

load_kivy_file = Builder.load_file("playaudio.kv")

class MainApp(App):
	def build(self):
		return load_kivy_file


if __name__ == "__main__":
	MainApp().run()