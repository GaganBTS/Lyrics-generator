import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from scrape import Lyrics_Scraping
def passon():
    if  song_entry.get == '' or artist_entry.get() == '':
        messagebox.showerror(title='ERROR',message='Something went wrong, try again.')
    else:
     name = song_entry.get()
     singer = artist_entry.get()
     song_lyrics = Lyrics_Scraping(name,singer)
     lyrics= song_lyrics.get_lyrics()
     if len(lyrics)==0:
         messagebox.showerror(title='ERROR', message='Something went wrong, try again.')
     else:
         text_area.delete(5.0, END)
         for l in lyrics[4:]:
            text_area.insert(END, f'{l}\n')

def clear():
    text_area.delete(0.0,tkinter.END)
# ----------------------------------------------ui------------------------------------ #
window = Tk()
window.title('Lyrics Generator')
window.config(width=500,height=700,bg='white',padx=50,pady=50)


# --------------------------------------labels----------------------------------------- #
title = Label(text='LYRICS',fg='purple',bg='white',font = ('Comic Sans MS',24,'bold'))
title.grid(column=1,row=0,pady=30)
song = Label(text='Song name ',bg='white',font=('Comic Sans MS',10,'normal'))
song.grid(column=0,row=1,padx=5)
artist = Label(text='Artist name ',bg='white',font=('Comic Sans MS',10,'normal'))
artist.grid(column=0,row=2,padx=5)
lyrics = Label(text='Lyrics',bg='white',font=('Comic Sans MS',10,'normal'))
lyrics.grid(column=0,row=4)


# ----------------------------------entries-------------------------------------------- #
song_entry = Entry(width=35)
song_entry.grid(column=1,row=1)
song_entry.focus()
artist_entry =Entry(width=35)
artist_entry.grid(column=1,row=2)
text_area = scrolledtext.ScrolledText(window,width=50,height=10,font=("Comic Sans MS",10))

text_area.grid(column=1,row=4)


# -----------------------------button-------------------------------- #
search = Button(window,text='SEARCH',bg='white',highlightthickness=0,font=('Comic Sans MS',10,'normal'),command =passon)
search.grid(column=1,row=3,pady=6)
clr = Button(window,text='CLEAR',bg='white',highlightthickness=0,font=('Comic Sans MS',10,'normal'),command =clear)
clr.grid(column=1,row=5,pady=6)


window.mainloop()
