import tkinter as tk
import tkinter.font as tkfont
from tkinterdnd2 import DND_TEXT, TkinterDnD as tkdnd
import subprocess as sp

global mustmove
global win

# var that tells moveit if to move
mustmove = False

def centerwin(win):
    x = (win.winfo_screenwidth() // 2) - (win.winfo_width() // 2)
    y = (win.winfo_screenheight() // 2) - (win.winfo_height() // 2)
    win.geometry(f"+{x}+{y}")

def moveit():
    global win
    global mustmove
    if mustmove:
        x = (win.winfo_pointerx()) - (win.winfo_width() // 2)
        y = (win.winfo_pointery()) - (win.winfo_height() // 2)
        win.geometry(f"+{x}+{y}")
    win.after(20, moveit)

def startmove(e):
    global mustmove
    mustmove = True

def stopmove(e):
    global mustmove
    mustmove = False

# start tkinter engine with open tkdnd root window
win = tkdnd.Tk()

# use a beautiful font
mfont = tkfont.Font(family="Comic Sans MS", size=24, weight="normal")

# window without system border exit on right click
win.overrideredirect(True)
win.attributes("-topmost", 1)
win.bind("<ButtonRelease-3>", lambda event : win.destroy())
win.bind("<ButtonPress-1>", startmove)
win.bind("<ButtonRelease-1>", stopmove)

# center window
win.after(100, lambda : centerwin(win))

frm = tk.Frame(win, highlightthickness=2)
frm.config(highlightbackground="#000000", highlightcolor="#000000")
frm.pack()

# our drag and drop label
lbl = tk.Label(frm, text="Drag'n'Drop YouTube Links here", font=mfont,
               border=16, relief=tk.FLAT, bg="#ffffff", fg="#f01010")
lbl.pack()

def ondrop(event):
    if event.data:
        sp.Popen(["mpv.exe", event.data])

lbl.drop_target_register(DND_TEXT)
lbl.dnd_bind("<<Drop>>", ondrop)

win.after(20, moveit)
win.mainloop()
