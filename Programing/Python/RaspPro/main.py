from tkinter import *
from tkinter import messagebox
import tkinter as tk
import subprocess
import time
import sys
from persiantools.jdatetime import JalaliDate
import datetime
import urllib.request
from threading import Thread

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

def exit():
    sys.exit()

def sudo(cmd, terminal):

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, shell = True)
    p.poll()
    terminal.tag_config('warning', foreground="red")

    while True:
        line = p.stdout.readline()
        terminal.config(state=NORMAL)
        terminal.insert(tk.END, line)
        terminal.insert(tk.END, "-------\n", 'warning')
        terminal.see(tk.END)
        terminal.config(state=DISABLED)
        if not line and p.poll is not None: break

    while True:
        err = p.stderr.readline()
        terminal.insert(tk.END, err)
        terminal.see(tk.END)
        if not err and p.poll is not None: break
    terminal.insert(tk.END, '\n Finished')


def nmapscan():
    #clock.grid(row=0, column=1)
    clock.config(font=('times', 24, 'bold'))
    fm1.pack_forget()
    fm2.pack_forget()
    #frame.pack_forget()
    textfield = Text(window, font = "Arial 9", width=55, height=160,bg='BLACK',fg='GREEN')
    textfield.pack(side = LEFT)

    scrollbar = Scrollbar(window)
    scrollbar.pack(side=LEFT, fill=Y)

    # attach listbox to scrollbar
    textfield.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textfield.yview)

    t = Thread(target = lambda: sudo("/home/pi/Downloads/Project/firstUi/portScan.sh", textfield))
    t.start()

    exitbtn = Button(window, text="BACK",bg='#0059b3' , command=gohome)
    exitbtn.pack(side = RIGHT)

def gohome():
    startPage()

def webstats():
    try:
        urllib.request.urlopen("http://localhost").getcode()
        test = "SV UP"
        statuslab.config(fg="GREEN")
    except Exception as e:
        test = "SV Down"
        statuslab.config(fg="RED")
    statuslab.config(text=test)

def startweb():
    ps = subprocess.Popen("sudo python3 /home/pi/Downloads/WOL_CCTV/button.py", shell=True, stdout=subprocess.PIPE)
    statuslab.config(fg="GREEN", text="Start")


def stopweb():
    ps = subprocess.Popen("sudo kill -9 $(ps -ef | grep '/usr/bin/python3 /home/pi/Downloads/WOL_CCTV/button.py' | head -n1 | awk '{print $2}')", shell=True, stdout=subprocess.PIPE)
    ps.wait()
    output1, errors1 = ps.communicate()
    #stopweb.config(bg="RED")
    statuslab.config(fg="RED", text="Stop")


def status():
    p1 = subprocess.Popen("/opt/vc/bin/vcgencmd measure_temp", shell=True, stdout=subprocess.PIPE)
    p2 = subprocess.Popen("ifconfig | grep 'inet 192' | awk '{print $2}'", shell=True, stdout=subprocess.PIPE)
    p3 = subprocess.Popen("df -h | grep '/dev/root' | awk '{print $5}'", shell=True, stdout=subprocess.PIPE)

    p1.wait()

    output1, errors1 = p1.communicate()
    output2, errors2 = p2.communicate()
    output3, errors3 = p3.communicate()
    webstats()
    templab.config(text=output1)
    iplab.config(text=output2)
    usagelab.config(text=output3)
    templab.after(3000, status)


def startPage():

    global clock
    global window
    global frame
    global fm2
    global fm1
    global startweb
    global stopweb
    global statuslab
    global exitbtn
    global pdatelab
    global templab
    global iplab
    global usagelab

    window = Tk()
    frame = Frame(window)
    frame.pack()

    pdate = JalaliDate.today()


    #status = Label(window, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
    #status.grid(row=0, column=0)

    ########CLOCK########

    clock = Label(window, font=('times', 74, 'bold'), fg='white', bg='black')
    #clock.grid(row=0, column=1)
    clock.config(anchor=CENTER)

    pdatelab = Label(window, font=('times', 14, 'bold'), fg='white', bg='black')
    #clock.grid(row=0, column=1)
    pdatelab.config(text=pdate,anchor=CENTER)
    clock.pack()
    pdatelab.pack()
    tick()

    #######EXIT BTN##########
    fm1 = Frame(window)
    fm1.config(bg="black")

    exitbtn = Button(fm1, text="EXIT APP",bg='#0059b3' , command=exit)
    exitbtn.pack( side = TOP)

    nmapbtn = Button(fm1, text="nmap",bg='#0059b3', command=nmapscan)
    nmapbtn.pack( side = TOP)

    startweb = Button(fm1, text="Start WB",bg='#0059b3' , command=startweb)
    startweb.pack( side = TOP)

    stopweb = Button(fm1, text="Stop WB",bg='#0059b3', command=stopweb)
    stopweb.pack( side = TOP)

    statuslab = Label(fm1,font=('times', 14, 'bold'), background="black", fg="WHITE", anchor=W)
    statuslab.pack( side = TOP)
    webstats()

    fm1.pack(side=RIGHT, expand=YES)
    #######STATUS###########
    ###TEMP
    fm2 = Frame(window)
    fm2.config(bg="black")

    templab = Label(fm2,font=('times', 14, 'bold'), background="black", fg="#3471eb", anchor=W)
    templab.pack( side = TOP )
    iplab = Label(fm2,font=('times', 14, 'bold'), background="black", fg="#3471eb", anchor=W)
    iplab.pack( side = TOP )
    usagelab = Label(fm2,font=('times', 14, 'bold'), background="black", fg="#3471eb", anchor=W)
    usagelab.pack( side = TOP )

    fm2.pack(side=LEFT, expand=YES )

    status()
    #########################
    window.title("Welcome to LikeGeeks app")

    #window.geometry('600x500')
    #def clicked():
    #    messagebox.showinfo('Message title', 'Message content')
    #btn = Button(window,text='Click here', command=clicked)
    #btn.grid(column=0,row=0)

    window.attributes('-fullscreen',True)

    window.configure(bg='black')

    window.mainloop()


time1=''
startPage()
