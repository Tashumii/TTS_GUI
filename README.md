# TTS_GUI
TTS WITH ADJUSTABLE SPEED RATE 


1. Importing Libraries
python
Copy code
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyttsx3
from PIL import Image, ImageTk
import threading
tkinter: Used to create the GUI (Graphical User Interface). It’s a standard Python library for creating desktop applications.
messagebox: Part of tkinter, used to show popup messages (alerts, warnings, etc.).
ttk: A themed widget set in tkinter for more modern-looking components like sliders.
pyttsx3: A library used for text-to-speech conversion. It helps turn typed text into spoken words.
PIL: Python Imaging Library (Pillow) for handling images (though you don't use it much in this code).
threading: Allows you to run functions in the background without blocking the main GUI, especially for time-consuming tasks like speech synthesis.
2. Text-to-Speech Function (text_to_speech)
python
Copy code
def text_to_speech():
    text = text_entry.get("1.0", tk.END).strip()  # Get text from the entry box
    if text:  # Check if text is provided
        try:
            engine = pyttsx3.init()  # Initialize pyttsx3 engine
            engine.setProperty('rate', rate_var.get())  # Set speech rate
            engine.setProperty('volume', volume_var.get() / 100)  # Set volume
            engine.say(text)  # Make the engine say the text
            engine.runAndWait()  # Wait until the speech is finished
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")
Getting Text: This line retrieves the text from the Text widget (text_entry), starting from the first character until the end.
Checking for Text: Before proceeding with TTS, it ensures the text is not empty.
Speech Engine: pyttsx3.init() initializes the speech engine. You can then adjust properties like speech rate (rate) and volume.
Speech: engine.say(text) converts the text to speech, and engine.runAndWait() makes the program wait until the speech is completed before continuing.
3. Clear Text Function
python
Copy code
def clear_text():
    text_entry.delete("1.0", tk.END)  # Deletes all the text in the text box
This function clears the text field when called. It deletes the content from the beginning ("1.0") to the end (tk.END).
4. Save Audio Function
python
Copy code
def save_to_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            engine = pyttsx3.init()  # Initialize pyttsx3 engine
            engine.setProperty('rate', rate_var.get())
            engine.setProperty('volume', volume_var.get() / 100)
            filename = "Text-to-speech-output.mp3"
            engine.save_to_file(text, filename)  # Saves the speech to an MP3 file
            engine.runAndWait()  # Wait until it's saved
            messagebox.showinfo("Success", f"Audio saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save audio: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")
Similar to text_to_speech, but instead of speaking the text, it saves the speech to an MP3 file.
engine.save_to_file(text, filename) takes care of saving the speech, and the runAndWait() method makes sure the file is fully saved before moving on.
5. Animate Icon Function
python
Copy code
def animate_icon():
    for _ in range(5):  # Loop for animation (5 times)
        icon_label.config(fg="blue")  # Change icon color to blue
        root.update_idletasks()  # Update the UI
        root.after(200)  # Wait for 200ms
        icon_label.config(fg="green")  # Change color back to green
        root.update_idletasks()  # Update the UI
        root.after(200)  # Wait again
This function creates a simple animation by changing the icon color from green to blue and back.
update_idletasks: Forces the UI to update after each change.
after: Pauses the execution for a set number of milliseconds (200ms here) to control the speed of the animation.
6. Creating the GUI
python
Copy code
root = tk.Tk()  # Create the main window
root.title("TTS Application")  # Set window title
root.geometry("600x500")  # Set window size
root.resizable(False, False)  # Prevent resizing
root = tk.Tk(): Creates the main application window.
geometry("600x500"): Sets the size of the window to 600x500 pixels.
resizable(False, False): Prevents the window from being resized.
7. Text Input Field
python
Copy code
tk.Label(root, text="Enter text below:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
text_entry = tk.Text(root, wrap="word", width=50, height=8)
text_entry.pack(padx=10, pady=5)
Label: Displays a label to instruct the user.
Text Widget: A multi-line text field where users can type the text to be converted to speech.
8. Sliders for Rate and Volume
python
Copy code
rate_var = tk.IntVar(value=150)  # Initial speech rate
volume_var = tk.IntVar(value=100)  # Initial volume

rate_frame = tk.Frame(root)
rate_frame.pack(pady=5)

volume_frame = tk.Frame(root)
volume_frame.pack(pady=5)

rate_label = tk.Label(rate_frame, text="Speech Rate:")
rate_label.pack(side="left")
rate_slider = ttk.Scale(rate_frame, from_=50, to=300, orient="horizontal", variable=rate_var)
rate_slider.pack(side="right", padx=10)

volume_label = tk.Label(volume_frame, text="Volume:")
volume_label.pack(side="left")
volume_slider = ttk.Scale(volume_frame, from_=0, to=100, orient="horizontal", variable=volume_var)
volume_slider.pack(side="right", padx=10)
rate_var and volume_var are variables used to store the values of the sliders (speech rate and volume).
Sliders allow users to adjust the rate and volume of speech in real-time.
ttk.Scale: A slider widget, where users can drag to select a value within a specified range.
9. Buttons for Actions
python
Copy code
speak_button = tk.Button(btn_frame, text="Speak", command=lambda: threading.Thread(target=text_to_speech).start(), bg="green", fg="white", font=("Arial", 12))
speak_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(btn_frame, text="Clear", command=clear_text, bg="red", fg="white", font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(btn_frame, text="Save to Audio", command=save_to_audio, bg="blue", fg="white", font=("Arial", 12))
save_button.grid(row=0, column=2, padx=10)
These buttons perform different actions:
Speak: Converts the text to speech. The threading.Thread ensures the app remains responsive while speaking.
Clear: Clears the text input field.
Save to Audio: Saves the speech as an MP3 file.
10. Icon Display
python
Copy code
icon_label = tk.Label(root, text="🔊", font=("roboto", 24), fg="green")
icon_label.pack(pady=10)
This is a simple label displaying an icon (🔊). It is used to show the animation effect in the app.
11. Main Application Loop
python
Copy code
root.mainloop()
This starts the tkinter event loop, making the application responsive to user interactions.
Tips for Building Similar Apps
Widgets: Get comfortable with basic tkinter widgets like Label, Button, Text, Scale, and Frame.
Event Handling: Understand how events (like button clicks) trigger functions.
Threading: For long-running tasks (like TTS), use threading to keep the GUI responsive.
Library Use: Explore other Python libraries for TTS, image manipulation, etc., to build more features.
