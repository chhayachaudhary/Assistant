from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("it's me Trc")
#width x height
window.geometry("690x600")
label2=Label(window,text="here are two flags")
label2.pack()

image=Image.open("C:/Users/chhay/Desktop/woman.jpeg")
photo=ImageTk.PhotoImage(image)
label1=Label(image=photo)
label1.pack()



window.mainloop()