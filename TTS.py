from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename
import pyttsx3
from tkinter import messagebox
converter = pyttsx3.init()
def convert():
    if len(t1.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Text Field can't be Empty!")
    else:
        if combo1.get() == 'Microsoft David (Language: English (United States))':
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        else:
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_MARK_11.0"
        converter.setProperty('voice', voice_id)
        if combo2.get() == 'Slow':
            converter.setProperty("rate", 100)
        elif combo2.get() == 'Fast':
            converter.setProperty("rate", 300)
        elif combo2.get() == 'Normal':
            converter.setProperty("rate", 200)
        else:
            converter.setProperty("rate", 0)
        converter.setProperty('volume', 100)
        text = t1.get(1.0, END)
        converter.say(text)
        converter.runAndWait()
def clear():
    if len(t1.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Text Field can't be Empty!")
    else:
        t1.delete(1.0, END)
def save_as():
    if len(t1.get('1.0', END)) <= 1:
        messagebox.showwarning("Warning!", "Text Field can't be Empty!")
    else:
        global file
        file = asksaveasfilename(initialfile='Untitled.mp3', defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if combo1.get() == 'Microsoft David (Language: English (United States))':
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
        else:
            voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            # voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enUS_MarkM"

        converter.setProperty('voice', voice_id)
        if combo2.get() == 'Slow':
            converter.setProperty("rate", 100)
        elif combo2.get() == 'Fast':
            converter.setProperty("rate", 300)
        elif combo2.get() == 'Normal':
            converter.setProperty("rate", 200)
        else:
            converter.setProperty("rate", 0)
        converter.setProperty('volume', 100)
        txt = t1.get(1.0, END)
        converter.save_to_file(txt, file)
        converter.runAndWait()
def exit1():
    root.destroy()
root = Tk()
root.iconbitmap("Images/icon.ico")
canvas_width = 1100
canvas_height = 700
root.geometry(f"{canvas_width}x{canvas_height}+110+0")
root.minsize(1100, 680)
root.title("TTS | Author: TW")
f1 = Frame(root, bg="#4682b4")
f1.pack(side=TOP, fill="x")
l1 = Label(f1, text="Text to Speech", font="Helvetica 16 bold", fg="white", bg="#4682b4", pady=10)
l1.pack(fill=BOTH)
l2 = Label(root, text="Speaker & Language", font="Helvetica 10 bold", fg="black", pady=10)
l2.pack(anchor="sw", padx=18)
l3 = Label(root, text="Speed", font="Helvetica 10 bold", fg="black", pady=10)
l3.place(x=598, y=50)
list1 = ["Microsoft David (Language: English (United States))", "Microsoft Zira (Language: English (United States))"]
combo1 = ttk.Combobox(root, values=list1, state="readonly", width=50)
combo1.current(0)
combo1.place(x=20, y=80)
list2 = ["Slow", "Normal", "Fast"]
combo2 = ttk.Combobox(root, values=list2, state="readonly", width=15)
combo2.current(1)
combo2.place(x=600, y=80)
t1 = Text(root, width=118, height=35, font=("Helvetica", 12))
t1.pack(padx=18, pady=40, fill=BOTH, ipady=223)
sb = Scrollbar(t1)
sb.pack(side=RIGHT, fill=Y)
sb.config(command=t1.yview)
t1.config(yscrollcommand=sb.set)
can = Canvas(root, height=20, width=100)
can.place(relx=0.5, rely=0.95, anchor=CENTER)
img1 = PhotoImage(file="Images/Button1.png")
img2 = PhotoImage(file="Images/Button2.png")
img3 = PhotoImage(file="Images/Button3.png")
img4 = PhotoImage(file="Images/Button4.png")
btn1 = Button(can, image=img1, borderwidth=0, command=convert, cursor='hand2')
btn2 = Button(can, image=img2, borderwidth=0, command=save_as, cursor='hand2')
btn3 = Button(can, image=img3, borderwidth=0, command=clear, cursor='hand2')
btn4 = Button(can, image=img4, borderwidth=0, command=exit1, cursor='hand2')
btn1.pack(side=LEFT, padx=40)
btn2.pack(side=LEFT, padx=40)
btn3.pack(side=LEFT, padx=40)
btn4.pack(side=LEFT, padx=40)
root.mainloop()
