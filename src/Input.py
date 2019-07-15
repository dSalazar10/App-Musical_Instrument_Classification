"""
MIT License

Copyright (c) 2019 Daniel Salazar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import Adafruit_BBIO.GPIO as GPIO
import pyaudio
import datetime
import wave
import time


class Button:
    def __init__(self):
        self.button = 'P8_17'
        self.button_setup()

    def button_setup(self):
        # setup button for input
        GPIO.setup(self.button, GPIO.IN)

    def is_pressed(self):
        return GPIO.input(self.button)

    def get_input(self):
        GPIO.wait_for_edge(self.button, GPIO.RISING)

    def cleanup(self):
        GPIO.cleanup()


class Mic:
    def __init__(self, lcd):
        self.lcd = lcd
        self.audio = pyaudio.PyAudio()
        self.mic_name = "AmazonBasics Portable USB Mic"
        self.device_index = self.mic_setup()
        if self.device_index == -1:
            self.lcd.mic_err()
            time.sleep(1)
            self.audio.terminate()
        self.sample_rate = 44100
        self.audio_format = pyaudio.paInt16
        self.audio_channel = 1
        self.chunk = 8192
        self.frames = []
        self.stream = None
        self.filenames = []
        self.counter = 0

    def mic_setup(self):
        if self.audio.get_device_info_by_index(1).get('name').startswith(self.mic_name):
            return 1
        for i in range(self.audio.get_device_count()):
            test_str = self.audio.get_device_info_by_index(i).get('name')
            if test_str.startswith(self.mic_name):
                return i
        self.lcd.mic_err()
        return -1

    # Instead of returning the stream, initialize the object's variable to the stream
    def start_stream(self):
        try:
            self.stream = self.audio.open(format=self.audio_format, rate=self.sample_rate, \
                                          channels=self.audio_channel, input_device_index=self.device_index, \
                                          input=True, frames_per_buffer=self.chunk)

            return True
        except:
            self.lcd.print("Stream Error\nReconnect Mic\n")
            time.sleep(1)
            return False

    def read_data(self):
        self.frames.append(self.stream.read(self.chunk, exception_on_overflow=False))

    def save_audio(self, audio_format=pyaudio.paInt16):
        self.stream.stop_stream()
        self.stream.close()
        file_name = "audio_test_" + datetime.datetime.now().strftime("%m-%d-%Y_%H:%M:%S") + "_.wav"
        wavefile = wave.open(file_name, 'wb')
        wavefile.setnchannels(self.audio_channel)
        wavefile.setsampwidth(self.audio.get_sample_size(audio_format))
        wavefile.setframerate(self.sample_rate)
        wavefile.writeframes(b''.join(self.frames))
        wavefile.close()
        self.filenames.append(file_name)
        self.counter += 1
        self.frames = []

    def cleanup(self):
        self.audio.terminate()
