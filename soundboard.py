import tkinter as tk
from tkinter import PhotoImage
import pygame
import os
from PIL import Image, ImageTk  # For handling background images

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Get the directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Find all .mp3 files in the current directory
sound_files = [file for file in os.listdir(current_directory) if file.endswith(".mp3")]

# Get the first .jpg file in the current directory for the background
background_image_path = None
for file in os.listdir(current_directory):
    if file.endswith(".jpg"):
        background_image_path = os.path.join(current_directory, file)
        break

# Create the main window
root = tk.Tk()
root.title("Soundboard")

# Set the exact window dimensions for a 3.5-inch screen (e.g., 480x320)
root.geometry("480x320")

# Load and set the background image if available
if background_image_path:
    bg_image = Image.open(background_image_path)
    bg_image = bg_image.resize((480, 320))  # Resize the image to fit the screen
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover the entire window

# Function to play sound
def play_sound(sound_name):
    sound_path = os.path.join(current_directory, sound_name)
    pygame.mixer.Sound(sound_path).play()

# Create buttons for each sound file with black background and red text
for i, sound_file in enumerate(sound_files):
    button = tk.Button(
        root,
        text=sound_file[:-4],  # Button text (remove file extension)
        width=10, height=2,  # Button size
        font=("Arial", 10),  # Font size
        bg="black", fg="red",  # Button colors
        command=lambda s=sound_file: play_sound(s)
    )
    button.grid(row=i // 2, column=i % 2, padx=5, pady=5)  # 2 buttons per row

# Run the Tkinter event loop
root.mainloop()
