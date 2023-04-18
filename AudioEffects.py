from pydub import AudioSegment
import numpy as np

class AudioEffects:
    def __init__(self, input_file):
        self.sound = AudioSegment.from_file(input_file, format="wav")

    def add_echo(self, output_file, delay_ms=500, intensity=0.6):
        echo_sound = self.sound[:delay_ms].fade_out(150).reverse().fade_out(delay_ms).reverse().fade_out(delay_ms).reverse()
        output_sound = self.sound.overlay(echo_sound, gain_during_overlay=-intensity)
        output_sound.export(output_file, format="wav")

    def reverse_audio(self, output_file):
        reversed_sound = self.sound.reverse()
        reversed_sound.export(output_file, format="wav")

    def dangle_audio(self, output_file, duration_ms=5000):
        silence = AudioSegment.silent(duration=duration_ms)
        output_sound = self.sound + silence
        output_sound.export(output_file, format="wav")

