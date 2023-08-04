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
    popup_label = Label(popup, text=f"Time's up! \nPoints: {points}", font=("Arial", 20))
    popup_label.pack()
    popup.focus_set()
    
"""start_function"""

    
"""check if char equals string char"""
    
points = 0

def start():
    """display text"""
    start_button.pack_forget()
    text_widget = Text(win, wrap=WORD, font=("Arial", 25))
    text_widget.pack(fill=BOTH, expand=True)
    text_widget.insert('1.0', ' '.join(words))
    text_widget.config(state=DISABLED)

    
    win.after(30000,timeout_message)    

    """Read keypress if key equals char in words then make this char green and iterate through"""
    """Transform words to one string with spaces !!!"""
    words_string = ' '.join(words)
    wait_var = BooleanVar()
    

    def check_char(event):
        global points 
        char = event.char
        wait_var.set(True)     
        text_widget.tag_add("here", f"1.{words_string.index(i)}", f"1.{words_string.index(i) + 1}")
        if char == i:
            points = points + 1
            text_widget.tag_config("here", foreground="green")
            """Make char green"""
        else:
            text_widget.tag_config("here", foreground="red")
            """Make char red"""
    

    for i in words_string:
        win.bind("<Key>", check_char)
        wait_var.set(False)
        win.wait_variable(wait_var)
    

"""bind start button"""
start_button = Button(text="Start", font=("Arial",20),command=start)
start_button.pack()



win.mainloop()