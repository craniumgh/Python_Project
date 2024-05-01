import tkinter as tk
from tkinter import messagebox, Scrollbar, Text
import lyricsgenius
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_lyrics():
    song_name = song.get().strip()  # Get the song name from the entry widget

    # Check if the user entered a song name
    if not song_name:
        messagebox.showerror("Error", "Please enter a song title.")
        return

    # Genius API token
    genius = lyricsgenius.Genius("AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg")

    try:
        # Search for the song lyrics
        song_lyrics = genius.search_song(song_name)

        # Check if the song was found
        if song_lyrics:
            # Display the lyrics and album cover in the window
            display_lyrics_with_cover(song_lyrics.lyrics, song_lyrics.song_art_image_url)
        else:
            messagebox.showerror("Error", "Lyrics not found for this song.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def display_lyrics_with_cover(lyrics, cover_url):
    # new window to display lyrics and cover photo
    lyrics_window = tk.Toplevel()
    lyrics_window.title("Lyrics and Album Cover")

    # Fetch the album cover image from the URL
    response = requests.get(cover_url)
    cover_image = Image.open(BytesIO(response.content))
    cover_photo = ImageTk.PhotoImage(cover_image)

    # label to display the album cover photo
    cover_label = tk.Label(lyrics_window, image=cover_photo)
    cover_label.image = cover_photo
    cover_label.pack(side="left", padx=10, pady=10)

    # widget to display the lyrics
    lyrics_text = Text(lyrics_window, wrap="word", height=20, width=50)
    lyrics_text.pack(side="left", fill="both", expand=True)

    # scrollbar for the text widget
    scrollbar = Scrollbar(lyrics_window, command=lyrics_text.yview)
    scrollbar.pack(side="right", fill="y")

    # get the text widget to use the scrollbar
    lyrics_text.config(yscrollcommand=scrollbar.set)

    # Insert lyrics into the text widget
    lyrics_text.insert("1.0", lyrics)

# Initialize Tkinter window
window = tk.Tk()
window.geometry('400x200')
window.title('Group Two')

# Label for entering song title
tk.Label(window, text="Enter song title:").pack(pady=5)

# Entry widget for entering the song name
song = tk.Entry(window, width=40)
song.pack()

# Button to trigger the get_lyrics function
tk.Button(window, text="Get Lyrics", command=get_lyrics).pack(pady=5)

window.mainloop()
