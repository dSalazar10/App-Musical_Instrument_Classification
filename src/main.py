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


# Load the LCD driver first due to Prediction taking a while
import Output
lcd = Output.CharLCD()
lcd.print("Loading...")
import time
import Input
import Prediction

"""
Configuration
"""
# Setup Compenents

button = Input.Button()
mic = Input.Mic(lcd)
predict = Prediction.Predict(lcd)

# Display Setup
# stretch goal: add a cool graphic loading message

"""
Event Loop
"""
done = False
count = 0
while not done:
    # Prompt user to 'Press Button' to record
    lcd.print("Press Button To\nStart Recording\n")
    
    button.get_input()
    time.sleep(0.15)
    
    # Record Audio if stream object created successfully
    if not mic.start_stream():
        break
    
    lcd.print("Press Button To\nStop Recording\n")
    
    while not button.is_pressed():
        mic.read_data()
        
    mic.save_audio()
    lcd.print("Predicting...\n")
    
    
    # Classify instrument(s) and display results
    instruments = predict.get_predictions(mic.filenames[mic.counter-1])
    if len(instruments) > 0:
        lcd.print("# of possible\ninstruments:" + str(len(instruments)))
        time.sleep(3)
        for i in range(0,len(instruments)):
            lcd.print(instruments[i])
            time.sleep(3)
    
    if count == 10:
        done = True
    count += 1

"""
Teardown
"""
lcd.Cleanup()
button.cleanup()
mic.cleanup()
