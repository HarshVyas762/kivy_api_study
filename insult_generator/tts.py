from kivy.core.audio import SoundLoader

from gtts import gTTS


class TextToSpeech():
	tts = None

	def __init__(self):
		self.tts = gTTS(text = " ", lang = 'en-us')
		self.tts.save('play_file.mp3')

	def set_phrase(self, phrase, ln):
		self.tts = gTTS(text = phrase, lang = ln)
		self.save_to_file()

	def save_to_file(self):
		self.tts.save('play_file.mp3')


class PlaySoundFile():
	tts = TextToSpeech()
	sound = None

	def play_text(self, phrase, ln, sound_f):
		self.tts.set_phrase(phrase, ln)

		self.get_sound(sound_f)

		if not self.sound:
			pass
		else:
			self.sound.play()

	def stop_play(self):
		if self.sound:
			self.sound.stop()

	def get_sound(self, sound_f):		
		self.sound = SoundLoader.load(sound_f)