from tkinter import *
from datetime import datetime

ws = Tk()
ws.geometry('400x450+1000+300')
ws.title('PythonGuides: Stopwatch')
ws.config(bg='#299617')
ws.resizable(0, 0)


def counter_label(lbl):
    def count():
        if running:
            global counter, start_time
            time_delta = datetime.now() - start_time
            display = get_hms_from_timedelta(time_delta)
            lbl['text'] = display
            print(display)
            lbl.after(1000, count)

    count()


def StartTimer(lbl):
    global running, start_time
    start_time = datetime.now()
    running = True
    counter_label(lbl)
    start_btn['state'] = 'disabled'
    stop_btn['state'] = 'normal'
    reset_btn['state'] = 'normal'


def StopTimer():
    global running
    start_btn['state'] = 'normal'
    stop_btn['state'] = 'disabled'
    reset_btn['state'] = 'normal'
    running = False


def ResetTimer(lbl):
    global counter, start_time
    counter = 0
    if running == False:
        reset_btn['state'] = 'disabled'
        lbl['text'] = '00:00:00'
    else:
        lbl['text'] = '00:00:00'
        # start_time = datetime.now()


def get_hms_from_timedelta(time_delta):
    hours = convert_to_string_leading_zero(time_delta.seconds // 3600)
    remaining_time = time_delta.seconds % 3600
    minutes = convert_to_string_leading_zero(remaining_time // 60)
    remaining_time = remaining_time % 60
    seconds = convert_to_string_leading_zero(remaining_time)
    display_str = hours + ':' + minutes + ':' + seconds
    return display_str


def convert_to_string_leading_zero(num):
    if num < 10:
        num_str = '0' + str(num)
    else:
        num_str = str(num)
    return num_str


# bg = PhotoImage(file='stopwatch.png')
img = Label(ws, bg='#299617')
img.place(x=75, y=50)

# Globals 
counter = 0
start_time = 0
running = False

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
