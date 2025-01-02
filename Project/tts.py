import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyttsx3
from PIL import Image, ImageTk
import threading


#Functions  to modify the text to speech rate speed and volume of the speech
def text_to_speech():
    
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', rate_var.get())  # Set speech rate
            engine.setProperty('volume', volume_var.get() / 100)  # Set volume
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

def clear_text():
    text_entry.delete("1.0", tk.END)

def save_to_audio():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', rate_var.get())
            engine.setProperty('volume', volume_var.get() / 100)
            filename = "Text-to-speech-output.mp3"
            engine.save_to_file(text, filename)
            engine.runAndWait()
            messagebox.showinfo("Success", f"Audio saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save audio: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

def animate_icon():
    for _ in range(5):  # Simulate a simple animation (loop to toggle icon color)
        icon_label.config(fg="blue")
        root.update_idletasks()
        root.after(200)
        icon_label.config(fg="green")
        root.update_idletasks()
        root.after(200)

#GUI Frontend 
root = tk.Tk()
root.title("TTS Application")
root.geometry("600x500")
root.resizable(False, False)

# Add a text input field
tk.Label(root, text="Enter text below:", font=("Arial", 14), bg="#f0f0f0").pack(pady=10)
text_entry = tk.Text(root, wrap="word", width=50, height=8)
text_entry.pack(padx=10, pady=5)

# Speech rate and volume sliders
rate_var = tk.IntVar(value=150)
volume_var = tk.IntVar(value=100)

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

# Buttons for actions
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

speak_button = tk.Button(btn_frame, text="Speak", command=lambda: threading.Thread(target=text_to_speech).start(), bg="green", fg="white", font=("Arial", 12))
speak_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(btn_frame, text="Clear", command=clear_text, bg="red", fg="white", font=("Arial", 12))
clear_button.grid(row=0, column=1, padx=10)

save_button = tk.Button(btn_frame, text="Save to Audio", command=save_to_audio, bg="blue", fg="white", font=("Arial", 12))
save_button.grid(row=0, column=2, padx=10)

# Animated icon
icon_label = tk.Label(root, text="🔊", font=("roboto", 24), fg="green")
icon_label.pack(pady=10)

root.mainloop()
