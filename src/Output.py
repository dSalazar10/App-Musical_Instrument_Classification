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

import Adafruit_CharLCD as LCD
import Adafruit_BBIO.GPIO as GPIO


# 1602A LCD
# 2 row x 16 column ASCII character display
class CharLCD:
    def __init__(self):
        self.lcd = LCD.Adafruit_CharLCD('P8_8', 'P8_10', 'P8_18', 'P8_16', 'P8_14', 'P8_12', 16, 2, 'P8_26')

    def print(self, msg):
        self.clear()
        self.lcd.message(msg)

    def mic_err(self):
        self.print("Failed to\nConnect to Mic\n")

    def rec_error(self):
        self.print("Failed to\nSave Audio\n")

    def len_error(self):
        self.print("Recording Length\nExceeded\n")

    def clear(self):
        self.lcd.clear()

    def cleanup(self):
        self.clear()
        GPIO.cleanup()
