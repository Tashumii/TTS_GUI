
# TTS - GUI

This project is a Python-based Text-to-Speech (TTS) Application that allows users to input text, listen to it spoken aloud, and save it as an audio file. The application features a user-friendly graphical interface created with Tkinter and uses the pyttsx3 library for text-to-speech conversion. It also includes customizable speech rate and volume settings. 




##  Feature

Text-to-Speech Conversion:
Input any text and have it read aloud using a synthesized voice.
Save to Audio:

Save the spoken output as an MP3 file for future use.
Customizable Speech Settings:

Adjust the speech rate (speed) and volume using sliders.

Clear Input:
Quickly clear the text input field with a single button.
Animated Visual Icon:

A simple animation adds visual feedback while the app is in use.


## How it works

Graphical User Interface (GUI):

Built with Tkinter, the GUI includes:
A text input field.
Sliders for speech rate and volume.
Buttons for speaking, clearing text, and saving audio.

Text-to-Speech Engine:
Uses the pyttsx3 library, which supports text-to-speech conversion without requiring an internet connection.
Allows fine-tuned control over speech properties like rate and volume.

Background Threading:
Speech playback runs in a separate thread to ensure the GUI remains responsive.

## Installation

Installation
Follow these steps to set up and run the project:

Prerequisites
Python 3.x installed on your system.
Required Python libraries: tkinter, pyttsx3, Pillow.

STEPS

cd tts-application


Install dependencies:


pip install pyttsx3 

pip install pillow

Run the application:

python app.py
## Usage


Input Text:

Type or paste your text into the provided text box.
Adjust Settings:

Use the sliders to modify the speech rate and volume to your liking.
Speak:

Click the Speak button to hear the text spoken aloud.

Save Audio:

Click the Save to Audio button to save the spoken text as an MP3 file in the current directory.

Clear Text:

Use the Clear button to reset the input field.
## Code Overview


Key Functions

text_to_speech:

Retrieves the text from the input box.
Configures the speech engine with the selected rate and volume.
Converts the text to speech.

clear_text:

Clears the text input field.

save_to_audio:

Saves the spoken version of the input text as an MP3 file.

animate_icon:

Simulates a simple animation by changing the icon color.
GUI Layout


Built using Tkinter:

Text Entry Field: For user input.
Sliders: Adjust speech rate (speed) and volume.
Buttons: Perform actions like speaking, saving, or clearing text.
Icon: Provides visual feedback during use.
## File structure

tts-application/

├── app.py      
         
├── README.md      
      
└──requirements.txt  
   
## Credits

Developed using Python.

GUI created with Tkinter.

Text-to-Speech powered by pyttsx3.