from tkinter import Tk, Button, Label, messagebox
import random


def no():
	messagebox.showinfo('', 'I know you are gay, but Ilove you anyways')
	root.quit()


def motion_mouse(event):
	btn_no.place(x=random.randint(0, 500), y=random.randint(150, 500))


root = Tk()
root.geometry('1660x600')
root.title('survey')
root.resizable(width=False, height=False)
root.configure(bg='white')

Label(root, text='Are you gay?', font=('Arial', 20, 'bold'), bg='white').pack()

btn_no = Button(root, text='No', font=('Arial', 20, 'bold'))
btn_no.place(x=170, y=106)
btn_no.bind('<Enter>', motion_mouse)

Button(root, text='Yes', font=('Arial', 20, 'bold'), command=no).place(x=350, y=106)

root.mainloop()