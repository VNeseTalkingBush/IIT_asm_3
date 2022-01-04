from tkinter import *

assistant = Tk()
assistant.title('Jeff')
assistant.geometry('320x550')
assistant.config(bg="gray")

img = PhotoImage(file="robot.png")
img_label = Label(self.assistant, image=self.img, bg='gray')
img_label.pack()

frame = Frame(self.assistant)
frame.pack()

questionField = Entry(self.assistant)

# designing scrollbar
scrollbar = Scrollbar(self.frame)
scrollbar.pack(side=RIGHT)
textarea = Text(self.frame, font=('Times new roman', 15, 'bold'), height=6, yscrollcommand=self.scrollbar.set)
textarea.pack(side=LEFT)
scrollbar.config(command=self.textarea.yview)

# Designing mic button and setting command for the button
mic_button_off = PhotoImage(file = "micoff.png")
mic_button_on = PhotoImage(file="micon.png")
mic = Button(frame, image=mic_button_on, height=6, width=8,
                  command=threading.Thread(target=speechToText).start)
mic.pack(side=LEFT)
mic.pack()


assistant.mainloop()