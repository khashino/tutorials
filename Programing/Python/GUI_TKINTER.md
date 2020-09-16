### installation
Linux
```
sudo apt-get install python-tk
```
Mac
```
brew install tcl-tk
```

### usage
https://realpython.com/python-gui-tkinter/

https://likegeeks.com/python-gui-examples-tkinter-tutorial/

```
from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Welcome to LikeGeeks app")
selected = IntVar()
rad1 = Radiobutton(window,text='First', value=1, variable=selected)
rad2 = Radiobutton(window,text='Second', value=2, variable=selected)
rad3 = Radiobutton(window,text='Third', value=3, variable=selected)
def clicked():
   print(selected.get())
btn = Button(window, text="Click Me", command=clicked)
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)
btn.grid(column=3, row=0)
window.mainloop()
```
```
from tkinter import *

from tkinter import messagebox

window = Tk()

window.title("Welcome to LikeGeeks app")

#window.geometry('600x500')

#def clicked():
#    messagebox.showinfo('Message title', 'Message content')
#btn = Button(window,text='Click here', command=clicked)
#btn.grid(column=0,row=0)

window.attributes('-fullscreen',True)
window.configure(bg='black')
window.mainloop()
```
#### CLOCK
```
from tkinter import *
from tkinter import messagebox
import time
import sys

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)

window = Tk()

time1 = ''

#status = Label(window, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
#status.grid(row=0, column=0)

clock = Label(window, font=('times', 30, 'bold'), fg='white', bg='black')
#clock.grid(row=0, column=1)
clock.config(anchor=CENTER)
clock.pack()

tick()

window.title("Welcome to LikeGeeks app")

#window.geometry('600x500')

#def clicked():
#    messagebox.showinfo('Message title', 'Message content')
#btn = Button(window,text='Click here', command=clicked)
#btn.grid(column=0,row=0)

window.attributes('-fullscreen',True)

window.configure(bg='black')

window.mainloop()
```

