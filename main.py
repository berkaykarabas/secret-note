import tkinter
from tkinter import *
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

screen = tkinter.Tk()
#screen format
screen.title("My Secret Notes")
screen.minsize(width=300,height=500)
FONT = ('Times New Roman', 12, 'normal')

def save_text():
   text_file = open("cryptofile.txt", "wb")
   encryp_text = my_text.get(1.0,END)
   key = my_masterkey.get()
   key = Fernet.generate_key()
   fernet = Fernet(key)
   cryp_text = fernet.encrypt(encryp_text.encode())
   text_file.write(cryp_text)
   text_file.close()
def decrypt_text():
   my_crypt_text = my_text.get(1.0,END)
   key = my_masterkey.get()
   key = Fernet.generate_key()
   fernet = Fernet(key)
   de_crypted = fernet.decrypt(my_crypt_text)
   open("cryptofile.txt","wb")
   my_crypt_text.write(de_crypted)

#add image
image_1 = Image.open("secret.png")
test = ImageTk.PhotoImage(image_1)
my_label_pic = tkinter.Label(image=test,)
my_label_pic.pack(side="top")

#label title information
my_info_label = tkinter.Label(text="Enter your title!",font=FONT)
my_info_label.pack()

#entry
my_title_entry = tkinter.Entry(width=25)
my_title_entry.pack()

#label text index
my_info_label = tkinter.Label(text="Enter your text (secret note)!",font=FONT)
my_info_label.pack()

#text
my_text = tkinter.Text(width=25, height=5)
my_text.pack()

#label master key information
my_info_master = tkinter.Label(text="Enter your master key!",font=FONT)
my_info_master.pack()

#entry2
my_masterkey = tkinter.Entry(width=25)
my_masterkey.pack()

#button1
my_button_1 = tkinter.Button(text="Save and Encrypt",command=save_text)
my_button_1.pack()

#button2
my_button_2 = tkinter.Button(text="Decrypt",command=decrypt_text)
my_button_2.pack()

screen.mainloop()