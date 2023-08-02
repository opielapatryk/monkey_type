#create layout in tkinter
#display random text (lorem ipsum dolor sit amet)
#if key press check key if == text[char] char font color = green point += 1 else font color = red 
#additional if key press ALWAYS timer start 00:60 seconds
#if time == 00:00 display popup with words per minute  

# Return a single random word
from random_word import RandomWords

words = []
for i in range(100):
    words.append(RandomWords().get_random_word())

"""set tkinter"""
from tkinter import *

win = Tk()  

"""centering window"""
window_height = 900
window_width = 1200

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

"""set and start timer when keypress"""
def timeout_message():
    popup = Toplevel()
    popup.title("Timeout")
    popup.geometry("{}x{}+{}+{}".format(300, 100, x_cordinate+450, y_cordinate+400))
    popup_label = Label(popup, text="Time's up!", font=("Arial", 20))
    popup_label.pack()
    popup.focus_set()
    
"""start_function"""
def start():
    """display text"""
    start_button.pack_forget()
    Label(text=words,wraplength=1200,font=("Arial",30)).pack()
    win.after(30000,timeout_message)    

"""bind start button"""
start_button = Button(text="Start", font=("Arial",30),command=start)
start_button.pack()


win.mainloop()