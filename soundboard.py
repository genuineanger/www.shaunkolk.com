import tkinter as tk
import pygame
import os

# Initialize pygame mixer for sound playback
pygame.mixer.init()

# Path to the folder with sound files
sound_folder = "/home/admin/sounds/"
sound_files = []

# Load sound files from the folder
for file in os.listdir(sound_folder):
    if file.endswith(".wav") or file.endswith(".mp3"):
        sound_files.append(file)

# Create the main window
root = tk.Tk()
root.title("Soundboard")

# Function to play sound
def play_sound(sound_name):
    sound_path = os.path.join(sound_folder, sound_name)
    pygame.mixer.Sound(sound_path).play()

# Create buttons for each sound file
for i, sound_file in enumerate(sound_files):
    button = tk.Button(root, text=sound_file[:-4], width=10, height=2, font=("Arial", 10), command=lambda s=sound_file: play_sound(s))
    button.grid(row=i // 2, column=i % 2, padx=5, pady=5)  # 2 buttons per row

# Run the Tkinter event loop
root.mainloop()
