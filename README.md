![](./images/LOGO.png)


# Embedded Machine Learning

The Music Box is stand-alone platform built around the Beaglebone Black
to record live music and classify the instrument that is playing in real-time.
The software is able to receive input with an integrated button, record
audio clips using an integrated mic, and display the resulting classification
in seconds with an integrated LCD screen. This is all housed neatly in a 3D
printed case.

## Table of Contents
* [Hardware](#hardware)
  - [Beagelbonee Black](#bbb)
  - [Button](#button)
  - [Mic](#mic)
  - [1602A LCD](#lcd)
  - [3D Printed Parts](#case)
  - [Post Wiring](#finished)
* [Software](#software)
* [Built With](#built)
* [Authors](#authors)

<a name="hardware"></a>
## Hardware

![](./images/BOM.png)

<a name="bbb"></a>
### Beaglebone Black
![](./images/BBB.jpg)
* The Beagle Bone Black (BBB) was utilized as this projects embedded platform.

<a name="button"></a>
### Tactile Button
![](./images/Button.jpg)
* A tactile button was integrated for user input.
* Pins used for Button:
  - Button Data = P8[17]
  - Button 3V = P9[3]
  - Button GND = P9[1]

<a name="mic"></a>
### Microphone
![](./images/Mic.jpg)
* A microphone was integrated for audio input.

<a name="lcd"></a>
### LCD Screen
![](./images/LCD.png)
* A 1602A LCD screen was integrated for user output.
* Pins used for LCD:
  - LCD Data = P8[12, 14, 16, 18]
  - LCD 5V = P9[8]
  - LCD GND = P9[2]

<a name="case"></a>
### 3D Printed Parts
* A 3D Printed case was made to house the components
  - ![](./images/Case.jpg)
* A 3D Printed bridge was made to support the button
  - ![](./images/Bridge.png)



<a name="finished"></a>
### Post Wiring 

* This is the result of soldering all the components to the BBB
  - Inside:
  - ![](./images/Music_Box_inside.jpg)
  - Outside:
  - ![](./images/Music_Box_outside.png)

<a name="software"></a>
## Software

<a name="built"></a>
## Built With
* [Adafruit Char LCD](https://github.com/adafruit/Adafruit_Python_CharLCD/blob/master/Adafruit_CharLCD/Adafruit_CharLCD.py) - 
this is used to interface with the 1602A LCD screen
* [Adafruit BBIO](https://pypi.org/project/Adafruit_BBIO/) - this is used to interface
 with the Beaglebone Black's GPIO pins
* [PyAudio](https://pypi.org/project/PyAudio/) - this is used to handle our audio I/O
* [DateTime](https://pypi.org/project/DateTime/) - this is used to add dates and times
to recorded audio file's names
* [Wave](https://pypi.org/project/Wave/) - this is used for audio file processing, setting
sample rates, setting channels, and setting sample size
* [Pickle](https://docs.python.org/3/library/pickle.html#module-pickle) - this is used to convert the
Machine Learning model into a byte stream to be saved to disk
* [LibROSA](https://librosa.github.io/librosa/index.html) - this is used for audio
analysis, trimming, onset detection, and collecting the [Mel-frequency Cepstrum Coefficients (MFCC)](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum)
* [NumPy](https://www.numpy.org) - this is used for manipulating the MFCC values
* [Scikit Learn](https://scikit-learn.org/stable/modules/svm.html) - this is used for the Support Vector Machine 
supervised learning model for classification of musical instruments
* [1602A LCD Case](https://www.thingiverse.com/thing:1873666) - this was used to house the hardware
* [Button Bridge](https://www.thingiverse.com/thing:1277483) - this was used to hol up the button inside the case

<a name="authors"></a>
## Authors
* **Daniel Salazar**
  - Hardware Analysis, Integration, and Soldering
  - 3D Printing
  - LCD Software
  - Machine Learning model selection, analysis, and training/testing
  
* **Thomas Martin**
  - Mic Software
  - Audio Preprocess Software
  - Button Software
  - Conversion of Machine Learning model to the embedded version and
  training/testing
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to Adafruit for providing the hardware driver code
* Thanks to [Rodger Doering](http://www.csueastbay.edu/directory/profiles/engr/doeringroger.html)
for his insight into the intricacies of Digital Signal Processing.
* Thanks to [Inés  Thiebaut](https://www.csueastbay.edu/directory/profiles/mus/thiebautines.html)
for her insight into Musical Instrument Classification.
