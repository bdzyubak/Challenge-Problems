from tkinter import *
from datetime import datetime

ws = Tk()
ws.geometry('400x450+1000+300')
ws.title('PythonGuides: Stopwatch')
ws.config(bg='#299617')
ws.resizable(0, 0)
# Globals 
counter = 0
start_time = 0
running = False


def counter_label(lbl):
    def count():
        if running:
            display = get_hms_from_timedelta()
            lbl['text'] = display

            lbl.after(1000, count)

    count()


def StartTimer(lbl):
    counter_label(lbl)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'


def StopTimer():
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'


def ResetTimer(lbl):
    if running == False:
        reset_btn['state'] = 'disabled'
    lbl['text'] = '00:00:00'


def get_hms_from_timedelta(time_delta):
    return


# bg = PhotoImage(file='stopwatch.png')
img = Label(ws, bg='#299617')
img.place(x=75, y=50)

# GUI defaults
lbl = Label(
    ws,
    text="00:00:00",
    fg="black",
    bg='#299617',
    font="Verdana 40 bold"
)

label_msg = Label(
    ws, text="",
    fg="black",
    bg='#299617',
    font="Verdana 10 bold"
)

lbl.place(x=80, y=170)
label_msg.place(x=80, y=250)

start_btn = Button(
    ws,
    text='Start',
    width=15,
    command=lambda: StartTimer(lbl)
)

stop_btn = Button(
    ws,
    text='Stop',
    width=15,
    state='disabled',
    command=StopTimer
)

reset_btn = Button(
    ws,
    text='Reset',
    width=15,
    state='disabled',
    command=lambda: ResetTimer(lbl)
)

start_btn.place(x=30, y=390)
stop_btn.place(x=150, y=390)
reset_btn.place(x=270, y=390)

ws.mainloop()
