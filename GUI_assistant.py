import threading
from tkinter import *

class GUI:
    def __init__(self):
        self.assistant = Tk()
        self.assistant.title('Jeff')
        self.assistant.geometry('320x550')
        self.assistant.config(bg="gray")

        self.img = PhotoImage(file="robot.png")
        self.img_label = Label(self.assistant, image=self.img, bg='gray')
        self.img_label.pack()

        self.frame = Frame(self.assistant)
        self.frame.pack()

        self.questionField = Entry(self.assistant)

        # designing scrollbar
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.pack(side=RIGHT)
        self.textarea = Text(self.frame, font=('Times new roman', 15, 'bold'), height=6, yscrollcommand=self.scrollbar.set)
        self.textarea.pack(side=LEFT)
        self.scrollbar.config(command=self.textarea.yview)

        # Designing mic button and setting command for the button
        self.mic_button_off = PhotoImage(file = "micoff.png")
        self.mic_button_on = PhotoImage(file="micon.png")
        self.mic = Button(self.frame, image=self.mic_button_on, height=6, width=8,
                          command=threading.Thread(target=self.speechToText).start)
        self.mic.pack(side=LEFT)
        self.mic.pack()

    def run(self):
        self.assistant.mainloop()

start = GUI()
start.run()